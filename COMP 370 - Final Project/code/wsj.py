import requests
import pandas as pd
import time

def wsj_search_json(query="zelensky", max_results=200):
    results = []
    page = 1

    while len(results) < max_results:
        url = f"https://www.wsj.com/search/term.json?query={query}&page={page}"
        print("抓取:", url)

        # 发送请求
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        
        # 解析 JSON
        try:
            data = resp.json()
        except:
            print("无法解析 JSON，可能被阻挡或访问失败")
            break

        # 提取搜索结果
        hits = (
            data.get("data", {})
                .get("items", [])
        )

        if not hits:
            print("没有更多结果")
            break

        # 保存条目
        for item in hits:
            results.append({
                "date": item.get("pubDate", ""),
                "url": item.get("url", ""),
                "title": item.get("headline", ""),
                "opening": item.get("summary", "")
            })

            if len(results) >= max_results:
                break

        page += 1
        time.sleep(0.5)   # 防止过快请求

    return pd.DataFrame(results)


# -------------------------
# 主程序执行
# -------------------------

df = wsj_search_json("zelensky", 200)

print(df)
df.to_csv("wsj_zelensky_200.csv", index=False)

print("\n文件已保存: wsj_zelensky_200.csv")
