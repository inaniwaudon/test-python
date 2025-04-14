import requests


def fetch_example_data():
    try:
        response = requests.get("https://example.com")
        response.raise_for_status()  # HTTPエラーが発生した場合に例外を発生させる
        return response.text
    except requests.RequestException as e:
        print(f"エラーが発生しました: {e}")
        return None


if __name__ == "__main__":
    data = fetch_example_data()
    if data:
        print("データの取得に成功しました")
        print(data)
    else:
        print("データの取得に失敗しました")
