import os
from datetime import datetime

import requests
from dotenv import load_dotenv


load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

NOTION_API_URL = "https://api.notion.com/v1/pages"
NOTION_VERSION = "2022-06-28"


def validate_env() -> None:
    """環境変数が正しく設定されているか確認する。"""
    if not NOTION_TOKEN:
        raise ValueError("NOTION_TOKEN が .env に設定されていません。")

    if not NOTION_DATABASE_ID:
        raise ValueError("NOTION_DATABASE_ID が .env に設定されていません。")


def input_rating(prompt: str) -> int:
    """1〜5の整数入力を受け取る。"""
    while True:
        value = input(prompt)
        try:
            rating = int(value)
        except ValueError:
            print("1〜5の整数で入力してください。例: 3")
            continue

        if 1 <= rating <= 5:
            return rating

        print("1〜5の範囲で入力してください。例: 3")


def input_positive_int(prompt: str) -> int:
    """1以上の整数入力を受け取る。"""
    while True:
        value = input(prompt)
        try:
            number = int(value)
        except ValueError:
            print("1以上の整数で入力してください。例: 1000")
            continue

        if number >= 1:
            return number

        print("0以下は入力できません。1以上の整数で入力してください。")


def input_float(prompt: str) -> float:
    """小数も含めた数値入力を受け取る。"""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("数値で入力してください。例: -245.5")


def print_notion_error(response: requests.Response) -> None:
    """Notion APIのエラー内容を初心者にも分かりやすく表示する。"""
    print("Notion API エラー:")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 400:
        print("原因候補: Notionデータベースの列名または列の種類が、Pythonコードと一致していない可能性があります。")
        print("確認する列名: Name, Session Date, Hands, Actual bb, EV bb, EV Gap, Actual bb/100, EV bb/100, Tilt Level, A-Game Score, Memo")
    elif response.status_code == 401:
        print("原因候補: NOTION_TOKEN が間違っている、または無効になっている可能性があります。")
    elif response.status_code == 403:
        print("原因候補: NotionデータベースがIntegrationに共有されていない可能性があります。")
    elif response.status_code == 404:
        print("原因候補: NOTION_DATABASE_ID が間違っている、または対象データベースが見つかっていない可能性があります。")
    elif response.status_code == 429:
        print("原因候補: Notion APIへのリクエスト回数が多すぎます。少し待ってから再実行してください。")
    else:
        print("原因候補: 想定外のエラーです。Notion APIのレスポンス本文を確認してください。")

    print("Notionからの詳細メッセージ:")
    print(response.text)


def create_poker_session(
    hands: int,
    actual_bb: float,
    ev_bb: float,
    tilt_level: int,
    a_game_score: int,
    memo: str,
) -> dict:
    """Notionデータベースにポーカーセッションを1件追加する。"""

    # セッション分析用の派生指標を計算する。
    ev_gap = actual_bb - ev_bb
    actual_bb_per_100 = actual_bb / hands * 100
    ev_bb_per_100 = ev_bb / hands * 100

    # Notionで日付フィルターを使えるように、セッション日付を保存する。
    session_datetime = datetime.now()
    session_title = session_datetime.strftime("Poker Session %Y-%m-%d %H:%M")
    session_date = session_datetime.strftime("%Y-%m-%d")
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }

    # Notionデータベースの列構成に合わせて送信用データを作成する。
    payload = {
        "parent": {
            "database_id": NOTION_DATABASE_ID,
        },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": session_title,
                        }
                    }
                ]
            },
            "Session Date": {
                "date": {
                    "start": session_date,
                }
            },
            "Hands": {
                "number": hands,
            },
            "Actual bb": {
                "number": actual_bb,
            },
            "EV bb": {
                "number": ev_bb,
            },
            "EV Gap": {
                "number": ev_gap,
            },
            "Actual bb/100": {
                "number": actual_bb_per_100,
            },
            "EV bb/100": {
                "number": ev_bb_per_100,
            },
            "Tilt Level": {
                "number": tilt_level,
            },
            "A-Game Score": {
                "number": a_game_score,
            },
            "Memo": {
                "rich_text": [
                    {
                        "text": {
                            "content": memo,
                        }
                    }
                ]
            },
        },
    }

    response = requests.post(
        NOTION_API_URL,
        headers=headers,
        json=payload,
        timeout=10,
    )

    if response.status_code >= 400:
        print_notion_error(response)
        response.raise_for_status()

    return response.json()


def main() -> None:
    validate_env()

    print("=== Poker Notion Tracker ===")

    hands = input_positive_int("ハンド数: ")
    actual_bb = input_float("実収支 [bb]: ")
    ev_bb = input_float("EV収支 [bb]: ")
    tilt_level = input_rating("ティルト度 [1-5]: ")
    a_game_score = input_rating("A-gameスコア [1-5]: ")
    memo = input("メモ: ")

    result = create_poker_session(
        hands=hands,
        actual_bb=actual_bb,
        ev_bb=ev_bb,
        tilt_level=tilt_level,
        a_game_score=a_game_score,
        memo=memo,
    )

    print("Notionへの記録が完了しました。")
    print(f"Page ID: {result.get('id')}")


if __name__ == "__main__":
    main()