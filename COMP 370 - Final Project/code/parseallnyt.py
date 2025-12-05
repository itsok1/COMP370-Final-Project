import json
import os
import csv

ARCHIVE_DIR = "nyt_archive"
OUTPUT_CSV = "zelensky_fixed.csv"

ZELENSKY_SPELLINGS = [
    "zelensky", "zelenskiy", "zelenskyy", "zelenskii", "zelenskyi",
    "volodymyr zelensky", "volodymyr zelenskyy", "volodymyr zelenskiy",
    "泽连斯基"
]

def fix_encoding_garbage(text):
    if not isinstance(text, str):
        return text

    replacements = {
        "â€™": "’", "â€œ": "“", "â€": "”",
        "â€“": "–", "â€”": "—", "â€¦": "…",
        "â€˜": "‘",

        "鈥檛": "’t",
        "鈥檚": "’s",
        "鈥�": "’",
        "鈥": "'",

        "ã": "。",
    }

    for bad, good in replacements.items():
        text = text.replace(bad, good)
    return text


def load_all_articles():
    all_articles = []
    for filename in os.listdir(ARCHIVE_DIR):
        if filename.endswith(".json"):
            path = os.path.join(ARCHIVE_DIR, filename)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if "response" in data and "docs" in data["response"]:
                    all_articles.extend(data["response"]["docs"])
            except:
                pass
    return all_articles


def filter_title_only(articles):
    spellings = [s.lower() for s in ZELENSKY_SPELLINGS]
    results = []

    for a in articles:
        title = a["headline"]["main"].lower()

        if any(sp in title for sp in spellings):
            results.append(a)

    return results


def export_csv(articles):
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "title", "short", "opening"])

        for a in articles:
            date = fix_encoding_garbage(a.get("pub_date", ""))
            title = fix_encoding_garbage(a["headline"].get("main", ""))
            short = fix_encoding_garbage(a.get("abstract") or a.get("snippet") or "")
            opening = fix_encoding_garbage(a.get("lead_paragraph", ""))

            writer.writerow([date, title, short, opening])


if __name__ == "__main__":
    all_articles = load_all_articles()
    title_only = filter_title_only(all_articles)
    export_csv(title_only)
    print(f"✔ FIXED CSV saved to {OUTPUT_CSV}")
