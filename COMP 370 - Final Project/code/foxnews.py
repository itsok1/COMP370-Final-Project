from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


START_URL = "https://www.foxnews.com/search-results/search#q=zelensky"


def open_driver():
    # 如果你本机是新版 Chrome + Selenium 4.6+，这样写就行
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver


def click_load_more_until_end(driver, max_clicks=300):
    wait = WebDriverWait(driver, 10)

    for i in range(max_clicks):
        try:
            # 找到包含“Load More”文字的按钮
            btn = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(., 'Load More') or contains(., 'Load more')]")
                )
            )
        except Exception:
            print("找不到 Load More 按钮了，可能已经到底。")
            break

        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", btn)
            time.sleep(0.5)
            btn.click()
            print(f"点击第 {i+1} 次 Load More")
            time.sleep(2.5)  # 等待新内容加载
        except Exception as e:
            print("点击 Load More 出错，尝试结束：", e)
            break


def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []

    # 筛标题：链接指向具体文章，并且文本不是“world / politics / fox-news.video”等栏目词
    # 你的页面里文章标题链接长这样：
    # <a href="https://www.foxnews.com/world/zelenskyy-speaks-...">Zelenskyy speaks ...</a>
    article_links = soup.find_all("a", href=True)

    blacklist = {"world", "politics", "fox-news.video",
                 "U.S.", "opinion", "media", "entertainment"}

    seen = set()

    for a in article_links:
        text = a.get_text(strip=True)
        href = a["href"]

        # 只要真正有标题文本的链接
        if not text:
            continue

        # 排除栏目标签
        if text.lower() in {b.lower() for b in blacklist}:
            continue

        # 只要 foxnews 正文或 video 链接
        if not href.startswith("http"):
            href = "https://www.foxnews.com" + href

        if "foxnews.com" not in href:
            continue

        # 只保留和 Zelensky 有关的链接（保险起见）
        if "zelensk" not in text.lower() and "zelensk" not in href.lower():
            continue

        key = (href, text)
        if key in seen:
            continue
        seen.add(key)

        # 找时间：在 HTML 片段中，时间是紧挨在栏目链接后面的 “May 16 / February 28 / 4 days ago ...”
        # 我们粗暴一点，从这一块外层的文本里用简单 split 提一下
        time_str = ""
        parent = a.parent
        if parent:
            # 往前找同级节点里的日期字符串
            prev_text = parent.get_text(" ", strip=True)
            # 里面可能包含：world May 16 标题 ...
            # 简单做法：把标题去掉，剩下的非栏目词当作日期
            if text in prev_text:
                prev_text = prev_text.replace(text, "")
            # 再把常见栏目词删掉
            for b in blacklist:
                prev_text = prev_text.replace(b, "")
            time_str = prev_text.strip()

        # snippet：在很多卡片中，标题之后紧跟着一段说明文字
        snippet = ""
        if parent:
            # 在 parent 之后找第一个非空文本节点
            nxt = parent.next_sibling
            while nxt and snippet == "":
                if isinstance(nxt, str):
                    s = nxt.strip()
                    if s:
                        snippet = s
                        break
                elif hasattr(nxt, "get_text"):
                    s = nxt.get_text(" ", strip=True)
                    if s:
                        snippet = s
                        break
                nxt = nxt.next_sibling

        results.append({
            "url": href,
            "title": text,
            "time": time_str,
            "snippet": snippet
        })

    return results


def main():
    driver = open_driver()
    driver.get(START_URL)

    # 先把第一页的内容全部加载完，然后不断点 Load More
    click_load_more_until_end(driver, max_clicks=300)

    html = driver.page_source
    driver.quit()

    articles = parse_page(html)
    print(f"总共抓到 {len(articles)} 篇含 Zelensky 的文章")

    # 简单打印前几条
    for art in articles[:10]:
        print("----")
        print("Title:", art["title"])
        print("Time :", art["time"])
        print("URL  :", art["url"])
        print("Snippet:", art["snippet"][:200])


if __name__ == "__main__":
    main()
