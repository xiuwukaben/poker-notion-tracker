# Poker Notion Tracker

Poker Notion Tracker は、ポーカーセッションの結果をターミナルから入力し、Notion データベースに自動記録する Python 製の CLI ツールです。

## 作った理由

既存のポーカートラッキングソフトでは、オールイン時点の EV 計算だけではセッション全体の判断や相手の大きなミスプレイを十分に反映できないことがあります。

そこで、実収支・EV収支・EV差分・bb/100・メンタル状態を自分で記録し、長期的に分析できる仕組みを作るために開発しました。

## 主な機能

- ハンド数の記録
- 実収支 bb の記録
- EV収支 bb の記録
- EV Gap の自動計算
- Actual bb/100 の自動計算
- EV bb/100 の自動計算
- Tilt Level の記録
- A-Game Score の記録
- メモの記録
- Notion API への自動 POST

## 使用技術

- Python
- requests
- python-dotenv
- Notion API

## Notion データベースの列構成

Notion 側には以下の列を作成してください。

| 列名 | 種類 |
|---|---|
| Name | タイトル |
| Hands | 数値 |
| Actual bb | 数値 |
| EV bb | 数値 |
| EV Gap | 数値 |
| Actual bb/100 | 数値 |
| EV bb/100 | 数値 |
| Tilt Level | 数値 |
| A-Game Score | 数値 |
| Memo | テキスト |

## セットアップ

### 1. 仮想環境を作成

```powershell
py -m venv .venv

```

### 2. 必要ライブラリをインストール

```powershell
.\.venv\Scripts\pip.exe install requests python-dotenv
```

### 3. `.env` を作成

`.env.example` をコピーして `.env` を作成し、Notion のトークンとデータベース ID を設定してください。

```env
NOTION_TOKEN=your_notion_integration_token_here
NOTION_DATABASE_ID=your_notion_database_id_here
```

### 4. 実行

```powershell
.\.venv\Scripts\python.exe main.py
```

## 入力例

```text
ハンド数: 1000
実収支 [bb]: 50
EV収支 [bb]: 20
ティルト度 [1-5]: 2
A-gameスコア [1-5]: 4
メモ: 集中してプレイできた
```

## 出力される指標

たとえば以下の入力の場合、

```text
Hands = 1000
Actual bb = 50
EV bb = 20
```

以下が自動計算されます。

```text
EV Gap = 30
Actual bb/100 = 5
EV bb/100 = 2
```

## 今後の改善予定

- セッション日付の自動記録
- レート・ゲームタイプの追加
- CSV 出力
- グラフ化
- Streamlit による Web アプリ化
- 分散・下振れ分析
- モンテカルロシミュレーション