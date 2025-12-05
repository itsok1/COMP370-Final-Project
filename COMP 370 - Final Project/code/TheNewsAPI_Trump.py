import requests
import pandas as pd
import time

API_KEY = "7azyFcrQk8KqPH7AQjsMpd0CjRbfN8JZyr6v4NHR"   # 重要：用你重置后的 key
QUERY = "Donald Trump"

articles = []

for page in range(1, 41):   # 40页 ≈ 1000篇
    url = (
        f"https://api.thenewsapi.com/v1/news/all?"
        f"api_token={API_KEY}&search={QUERY}"
        "&language=en&countries=us,ca&page=" + str(page)
    )
    
    r = requests.get(url).json()
    
    if "data" not in r or len(r["data"]) == 0:
        break
    
    articles.extend(r["data"])
    print(f"Fetched page {page}, total {len(articles)} articles")
    
    time.sleep(0.3)   # 免费版限速，避免429

df = pd.DataFrame(articles)
df.to_csv("trump_news.csv", index=False)

print("Done! Collected", len(df), "articles.")
