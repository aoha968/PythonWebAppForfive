from bs4 import BeautifulSoup
import requests
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import datetime
from gspread_dataframe import set_with_dataframe
import altair as alt

# .env ファイルをロードして環境変数へ反映
import os
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os
SP_SHEET_KEY = os.getenv('SP_SHEET_KEY')
SP_SHEET = os.getenv('SP_SHEET')

def get_data_udemy():
    url = "https://scraping-for-beginner.herokuapp.com/udemy"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    n_subscriber = soup.find('p', {'class': 'subscribers'}).text
    n_subscriber =  int(n_subscriber.split('：')[1])

    n_review = soup.find('p', {'class': 'reviews'}).text
    n_review =  int(n_review.split('：')[1])
    return {
        'n_subscriber': n_subscriber,
        'n_review': n_review
    }

def main():
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    credentials = Credentials.from_service_account_file(
        'service_account.json',
        scopes=scopes
    )

    gc = gspread.authorize(credentials)

    sh = gc.open_by_key(SP_SHEET_KEY)

    worksheet = sh.worksheet(SP_SHEET)

    data = worksheet.get_all_values()
    df = pd.DataFrame(data[1:], columns=data[0])

    data_udemy = get_data_udemy()
    today = datetime.date.today().strftime('%Y/%m/%d')

    data_udemy['date'] = today
    df = df.append(data_udemy, ignore_index=True)

    set_with_dataframe(worksheet, df, row=1, col=1)

if __name__ == '__main__':
    main()
