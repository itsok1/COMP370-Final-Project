
import requests
from bs4 import BeautifulSoup
import csv
import time
import json
import re
from datetime import datetime

# Headers like browser
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

base_url = "https://globalnews.ca/gnca-ajax-redesign/latest-stories/"
payload_template = (
    '{{"trackRegion":"archive-latestStories","version":"2","adEnabled":"1",'
    '"adPosition":{{"mobile":"14","desktop":"14"}},"adOffset":{{"mobile":1,"desktop":6}},'
    '"adFrequency":{{"mobile":6,"desktop":6}},"number":"11","action":"latest-stories",'
    '"loadMoreTarget":"archive-latestStories","queryType":"tag","queryValue":"volodymyr-zelenskyy",'
    '"tagFilter":"","postTypes":"post","loadMoreButton":"","analytics":{{"name":"load-more"}},'
    '"lastPostId":"{last_post_id}","page":"{page}"}}'
)

def clean_date(date_str):
    #Convert YYYY-MM-DD 
    if not date_str:
        return None
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.date().isoformat()
    except Exception:
        return date_str.split("T")[0]

def clean_title(title):
    #remove National | Globalnews.ca
    if not title:
        return None
    return re.sub(r"\s*-\s*[^|]*\|\s*Globalnews\.ca$", "", title).strip()

def get_article_metadata(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(resp.text, "html.parser")

        # Title
        meta_title = soup.find("meta", property="og:title")
        title = meta_title["content"] if meta_title else None
        title = clean_title(title)

        # Date
        meta_date = soup.find("meta", property="article:published_time")
        date = meta_date["content"] if meta_date else None

        if not date:
            for tag in soup.find_all("script", type="application/ld+json"):
                try:
                    data = json.loads(tag.string or "{}")
                except Exception:
                    continue
                if isinstance(data, dict):
                    if "datePublished" in data:
                        date = data["datePublished"]
                        break
                    if "@graph" in data:
                        for node in data["@graph"]:
                            if isinstance(node, dict) and "datePublished" in node:
                                date = node["datePublished"]
                                break
        date = clean_date(date)

        # Short opening 
        meta_desc = soup.find("meta", property="og:description")
        if not meta_desc:
            meta_desc = soup.find("meta", attrs={"name": "description"})
        short_opening = meta_desc["content"].strip() if meta_desc and meta_desc.get("content") else None

        return [date, title, short_opening, url]
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return [None, None, None, url]

#Collect 100
all_urls = []
last_post_id = "11027882" 
page = 1

while len(all_urls) < 100:
    url = base_url + payload_template.format(last_post_id=last_post_id, page=page)
    resp = requests.get(url, headers=HEADERS, timeout=15)
    soup = BeautifulSoup(resp.text, "html.parser")

    items = soup.select("ul#stream-1 li.c-posts__item a.c-posts__inner")
    if not items:
        break

    page_urls = [a.get("href") for a in items if a.get("href")]
    all_urls.extend(page_urls)

    last_post_id = page_urls[-1].split("/")[4]
    page += 1
    time.sleep(0.5)

results = []
for url in all_urls[:100]:
    results.append(get_article_metadata(url))
    time.sleep(0.3)

# Saving
with open("zelensky_globalnews.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "title", "short_opening", "url"])
    writer.writerows(results)


