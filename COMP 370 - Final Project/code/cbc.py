from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)  # 手动看页面
    page = browser.new_page()
    
    url = "https://www.cbc.ca/search?q=zelensky&page=1"
    print("访问:", url)

    page.goto(url, wait_until="networkidle")
    
    # 打印最终渲染后的 DOM 前 2000 字
    html = page.content()
    print(html[:2000])

    # 保存一份 HTML 文件用于分析
    with open("cbc_rendered.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("完整HTML已保存为 cbc_rendered.html")

    browser.close()
