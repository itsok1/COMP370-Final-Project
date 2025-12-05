import requests
import time
import json
import os

API_KEY = "auOvOAhTQMcRbvG5VPEp3hnBYn0vO9fZ"

YEARS = [2022, 2023, 2024, 2025]  # 你要下载的年份
MONTHS = range(1, 13)  # 1–12 月

BASE_URL = "https://api.nytimes.com/svc/archive/v1/{year}/{month}.json"

SAVE_DIR = "nyt_archive"
os.makedirs(SAVE_DIR, exist_ok=True)

def download_archive(year, month):
    url = BASE_URL.format(year=year, month=month)
    params = {"api-key": API_KEY}

    print(f"📦 Downloading {year}-{month} ...")

    try:
        r = requests.get(url, params=params, timeout=30)
        data = r.json()
    except Exception as e:
        print(f"❌ Error fetching {year}-{month}: {e}")
        return

    filename = f"{SAVE_DIR}/{year}_{month}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

    print(f"✅ Saved: {filename}")

for year in YEARS:
    for month in MONTHS:
        download_archive(year, month)
        time.sleep(6)  # 避免限流（NYT API 必须休息 6 秒）
