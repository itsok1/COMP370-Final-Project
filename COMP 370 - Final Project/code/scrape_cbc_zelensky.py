import requests
import csv
import time
from datetime import datetime

GRAPHQL_URL = "https://www.cbc.ca/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

GRAPHQL_QUERY_TEMPLATE = """
query AllSearchItems($searchQuery: String!) {{
  allSearchItems(query: $searchQuery, section: "news", contentType: "", sort: "newest", page: {page}, target: WEB, boosts: ["title^5","tags.generic^7","tags.collections^7","tags.location^4","tags.organization^3","tags.person^5","description","body","url"]) {{
    nodes {{
      title
      description
      url
      publishedAt
      contentType
    }}
    totalCount
  }}
}}
"""

def fetch_page(page_num):
    query = GRAPHQL_QUERY_TEMPLATE.format(page=page_num)
    payload = {
        "query": query,
        "variables": {
            "searchQuery": "zelensky"
        }
    }
    response = requests.post(GRAPHQL_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["data"]["allSearchItems"]["nodes"]

def scrape_articles(max_articles=100):
    all_articles = []
    page = 1
    while len(all_articles) < max_articles:
        articles = fetch_page(page)
        if not articles:
            break
        
        filtered = [
            a for a in articles
            if (a.get("contentType") in ["story", "article"]) and (
                "zelensky" in (a.get("title") or "").lower() or
                "zelensky" in (a.get("description") or "").lower() or
                "zelenskyy" in (a.get("title") or "").lower() or
                "zelenskyy" in (a.get("description") or "").lower()
            )
        ]
        all_articles.extend(filtered)
        page += 1
        time.sleep(0.7)
    return all_articles[:max_articles]

def save_to_csv(articles, filename="zelensky_cbc4.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "title", "short_opening", "url"])
        for a in articles:
            # Convert to YYYY-MM-DD
            try:
                date_str = datetime.fromtimestamp(int(a.get("publishedAt", 0)) / 1000).strftime("%Y-%m-%d")
            except Exception:
                date_str = ""
            title = (a.get("title") or "").strip()
            desc = (a.get("description") or "").strip()
            url = (a.get("url") or "").strip()
            writer.writerow([date_str, title, desc, url])

if __name__ == "__main__":
    articles = scrape_articles()
    save_to_csv(articles)

