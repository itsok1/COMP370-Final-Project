# -*- coding: utf-8 -*-
import time
import csv
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup, NavigableString
import re
from bs4 import NavigableString

# 正则匹配 NPR 日期格式，如 "February 20, 2025"
DATE_REGEX = re.compile(r"[A-Za-z]+ \d{1,2}, \d{4}")

BASE_URL = "https://www.npr.org/search?query=zelenskyy&sortType=bestMatch&page={}"




# 多种日期格式
DATE_REGEXES = [
    re.compile(r"[A-Za-z]+ \d{1,2}, \d{4}"),                    # November 17, 2025
    re.compile(r"\d{4}-\d{2}-\d{2}"),                           # 2025-11-17
    re.compile(r"[A-Za-z]+ \d{1,2}, \d{4}\s*\d{1,2}:\d{2}"),    # November 17, 2025 4:53
]


def match_date(text):
    """尝试所有正则"""
    if not text:
        return None
    for reg in DATE_REGEXES:
        m = reg.search(text)
        if m:
            return m.group(0)
    return None


def extract_date_near(a):
    """终极版：从 NPR 搜索结果中找日期"""

    # ------------ 1. 在 <a> 的父级块内找时间 ------------
    parent = a.find_parent(["article", "div"])
    if parent:
        for node in parent.find_all(["time", "span", "p", "div"]):
            text = node.get_text(" ", strip=True)
            found = match_date(text)
            if found:
                return found

    # ------------ 2. 检查兄弟节点 ------------
    for sib in a.next_siblings:
        text = sib.get_text(" ", strip=True) if not isinstance(sib, NavigableString) else str(sib).strip()
        found = match_date(text)
        if found:
            return found

    # ------------ 3. 在 input, meta 的 value 中找 ------------
    for tag in a.find_parent(["div", "article"]).find_all(["input", "meta"]):
        val = tag.get("value") or tag.get("content")
        if val:
            found = match_date(val)
            if found:
                return found

    # ------------ 4. 在更上层的块查找 ------------
    block = a.find_parent("article") or a.find_parent("div")
    if block:
        text = block.get_text(" ", strip=True)
        found = match_date(text)
        if found:
            return found

    # ------------ 5. 最后兜底：全文搜索附近 ------------
    all_text = a.find_parent("body").get_text(" ", strip=True)[:3000]
    found = match_date(all_text)
    if found:
        return found

    return None



def extract_articles_from_html(html):
    """从浏览器渲染后的 HTML 中提取文章"""
    soup = BeautifulSoup(html, "html.parser")
    results = []

    # NPR 文章链接都以 https://www.npr.org/20xx 开头
    for a in soup.select('a[href^="https://www.npr.org/20"]'):
        url = a["href"]

        # 排除栏目页（一般以 / 结尾）
        if url.endswith("/"):
            continue

        title = a.get_text(strip=True)
        if not title:
            continue

        # 提取日期
        date = extract_date_near(a)

        results.append({
            "url": url,
            "title": title,
            "date": date
        })

    return results


def extract_opening(browser, url):
    """稳定提取 NPR 正文前 1～2 段"""

    page = browser.new_page()
    try:
        page.goto(url, timeout=20000)
        page.wait_for_timeout(2000)
    except:
        return ""

    soup = BeautifulSoup(page.content(), "html.parser")

    # 1️⃣ 优先抓 storytext
    paragraphs = soup.select("div[data-testid='storytext'] p")

    # 2️⃣ fallback：抓 article 下的 <p>（但避免抓 authors / summary）
    if not paragraphs:
        paragraphs = soup.select("article p")

    clean_paras = []
    for p in paragraphs:
        text = p.get_text(strip=True)

        # 过滤掉非正文段落
        if not text:
            continue
        if text.startswith("By "):
            continue
        if text.startswith("Subscribe"):
            continue
        if "Up First" in text and len(text) < 200:
            continue
        if "NPR" in text and len(text) < 200:
            continue

        clean_paras.append(text)

        if len(clean_paras) >= 2:
            break

    page.close()

    return " ".join(clean_paras)



def main():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()

        all_articles = []
        seen = set()

        MAX_ARTICLES = 200
        page_num = 1

        while len(all_articles) < MAX_ARTICLES:

            url = BASE_URL.format(page_num)
            print(f"打开第 {page_num} 页: {url}")

            page.goto(url)
            page.wait_for_timeout(2500)

            # 点击 Cookie 弹窗（JS 强制）
            try:
                page.evaluate("""
                    const btn = [...document.querySelectorAll('button')]
                        .find(b => b.textContent.trim() === 'Allow All');
                    if (btn) btn.click();
                """)
            except:
                pass

            html = page.content()
            items = extract_articles_from_html(html)

            if not items:
                print("此页无文章 → 停止")
                break

            # 添加去重后的文章
            for it in items:
                if it["url"] not in seen:
                    seen.add(it["url"])
                    all_articles.append(it)

                if len(all_articles) >= MAX_ARTICLES:
                    break

            print(f"当前总数: {len(all_articles)} 篇\n")

            page_num += 1
            time.sleep(1)

        print("开始抓正文开头……")

        for i, art in enumerate(all_articles):
            print(f"[{i+1}/{len(all_articles)}] {art['url']}")
            art["opening"] = extract_opening(browser, art["url"])
            time.sleep(1)

        # 保存 CSV
        with open("npr_zelensky_bestmatch_200.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "title", "url", "opening"])
            for a in all_articles:
                writer.writerow([a["date"], a["title"], a["url"], a["opening"]])

        print("\n🎉 完成！已保存到 npr_zelensky_bestmatch_200_1.csv")
        browser.close()


if __name__ == "__main__":
    main()
