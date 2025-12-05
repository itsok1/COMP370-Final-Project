import requests
import time
import csv

API_KEY = "auOvOAhTQMcRbvG5VPEp3hnBYn0vO9fZ"
QUERY = "Zelensky OR Zelenskiy OR Zelenskyy OR Зеленський "
URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

# ---------------------------------
# STEP 1: get meta (official method)
# ---------------------------------

def get_meta():
    params = {
        "q": QUERY,
        "page": 0,
        "api-key": API_KEY
    }
    r = requests.get(URL, params=params)
    data = r.json()

    # If NYT blocks request → no response/meta
    if "response" not in data:
        print("❌ Cannot get meta, NYT API returned:")
        print(data)
        return None
    
    meta = data["response"].get("meta", None)
    print("🔎 Meta info:", meta)
    return meta

meta = get_meta()

# If meta is None → NYT quota exceeded or key blocked
if meta is None:
    print("🚫 NYT API quota exceeded or invalid response. Try again after quota resets.")
    exit()

# Total number of hits from NYT official meta
hits = meta["hits"]
pages_needed = hits // 10 + 1
print(f"📌 Total articles NYT has: {hits}, need pages: {pages_needed}")

# ---------------------------------
# STEP 2: fetch all pages safely
# ---------------------------------

results = []

def fetch_page(page):
    params = {
        "q": QUERY,
        "page": page,
        "api-key": API_KEY
    }
    r = requests.get(URL, params=params)
    data = r.json()

    # Handle quota or invalid response
    if "response" not in data:
        print(f"⚠️ Page {page} ERROR:")
        print(data)
        return []

    docs = data["response"].get("docs", [])
    return docs


# Loop through ONLY valid pages
for page in range(pages_needed):
    print(f"\n📄 Fetching page {page}/{pages_needed-1} ...")

    docs = fetch_page(page)
    print(f"   → Got {len(docs)} articles")

    results.extend(docs)

    # NYT limit: 1 request every ~6 seconds
    time.sleep(6)

print(f"\n✅ Total articles collected: {len(results)}")

# ---------------------------------
# STEP 3: save csv
# ---------------------------------

filename = "zelensky_articles.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["headline", "pub_date", "abstract", "web_url", "section_name"])

    for doc in results:
        writer.writerow([
            doc.get("headline", {}).get("main", ""),
            doc.get("pub_date", ""),
            doc.get("abstract", ""),
            doc.get("web_url", ""),
            doc.get("section_name", "")
        ])

print(f"💾 Saved to {filename}")
