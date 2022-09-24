# Webスクレイピング活用アプリ

## 環境
- Google Cloud
- Googleスプレッドシート
- Python 3.9.1
    - altair
    - BeautifulSoup
    - datetime
    - dotenv
    - gspread
    - pandas
    - streamlit

<br>

セキュリティを考慮して、KEYやアカウントの情報をGit管理から除外
- .env
    ```
        SP_SHEET_KEY = 'Key情報'
        SP_SHEET = 'Googleスプレッドシート名'
    ```
- service_account.json
    - Google Cloudで作成したキーを「service_account.json」にリネームしたファイル

