# -*- coding: utf-8 -*-
import requests
import csv
import time

GRAPHQL_URL = "https://www.reuters.com/graphql"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def fetch_search_page(query, offset):
    """
    Fetch Reuters search results from GraphQL endpoint.
    """
    graphql_query = {
        "query": """
        query Search($query:String!, $offset:Int!) { 
            search(query: $query, offset: $offset, limit: 20) { 
                results { 
                    url
                    title
                    published
                }
            }
        }
        """,
        "variables": {
            "query": query,
            "offset": offset
        }
    }

    resp = requests.post(GRAPHQL_URL, headers=HEADERS, json=graphql_query)

    if resp.status_code != 200:
        raise RuntimeError(f"GraphQL query failed: {resp.status_code}, {resp.text}")

    data = resp.json()
    return data["data"]["search"]["results"]


def fetch_article_opening(url):
    """
    Because the GraphQL API does not directly return article text,
    we fetch the article page HTML and extract first paragraph manually.
    """
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
    except:
        return ""

    if r.status_code != 200:
        return ""

    # simple extraction
    import re
    paragraphs = re.findall(r"<p.*?>(.*?)</p>", r.text)
    clean = [re.sub("<.*?>", "", p).strip() for p in paragraphs]
    clean = [p for p in clean if len(p) > 30]  # filter too-short
    return " ".join(clean[:2])


def main():
    QUERY = "zelenskiy"
    MAX_ARTICLES = 200

    all_articles = []
    seen = set()
    offset = 0

    print("开始使用 Reuters GraphQL API 抓取数据...")

    while len(all_articles) < MAX_ARTICLES:
        print(f"offset = {offset}")

        results = fetch_search_page(QUERY, offset)
        if not results:
            print("无更多结果，停止。")
            break

        for item in results:
            url = item["url"]
            if not url.startswith("http"):
                url = "https://www.reuters.com" + url

            if url not in seen:
                seen.add(url)
                all_articles.append({
                    "title": item["title"],
                    "date": item["published"],
                    "url": url,
                })

            if len(all_articles) >= MAX_ARTICLES:
                break

        offset += 20
        time.sleep(0.2)

    print(f"共抓到 {len(all_articles)} 篇文章。")
    print("开始抓取 opening 段落...")

    for i, art in enumerate(all_articles):
        print(f"[{i+1}/{len(all_articles)}] {art['url']}")
        art["opening"] = fetch_article_opening(art["url"])
        time.sleep(0.2)

    # 保存输出
    with open("reuters_graphql_200.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "title", "url", "opening"])
        for a in all_articles:
            writer.writerow([a["date"], a["title"], a["url"], a["opening"]])

    print("\n🎉 完成！文件已保存为 reuters_graphql_200.csv")


if __name__ == "__main__":
    main()
