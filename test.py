import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_yahoo_data():
    try:
        response = requests.get("https://www.yahoo.co.jp")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 見出し要素を取得
        headlines = soup.find_all(['h1', 'h2', 'h3'])
        print("見出し一覧:")
        for headline in headlines:
            print(f"- {headline.text.strip()}")
            
        # リンクを取得
        links = soup.find_all('a')
        print("\nリンク一覧:")
        for link in links:
            if link.get('href'):
                print(f"- {link.text.strip()}: {link['href']}")
                
        return response.text
    except requests.RequestException as e:
        print(f"エラーが発生しました: {e}")
        return None


if __name__ == "__main__":
    data = fetch_yahoo_data()
    if data:
        print("\nデータの取得に成功しました")
    else:
        print("データの取得に失敗しました")
