# Poker Notion Tracker

Poker Notion Tracker は、ポーカーセッションの結果をターミナルから入力し、Notionデータベースへ自動記録する Python 製CLIツールです。

実収支、EV収支、EV Gap、bb/100、ティルト度、A-gameスコア、メモ、セッション日付を一元管理できます。

## 概要

このツールでは、以下のようなポーカーセッション情報を記録できます。

- ハンド数
- 実収支 [bb]
- EV収支 [bb]
- EV Gap
- Actual bb/100
- EV bb/100
- Tilt Level
- A-Game Score
- Memo
- Session Date

入力したデータは Notion API を通じて、自分のNotionデータベースに自動で追加されます。

## 作成背景

既存のポーカートラッキングソフトでは、オールイン時点の勝率を基準にEVが計算されるため、プリフロップやフロップでの相手の大きなミスが十分に反映されないことがあります。

その結果、正しい判断をしていても、短期的な分散やEV表示によってメンタルに悪影響が出ることがあります。

この課題を解決するために、自分自身でセッションデータを蓄積し、実収支・EV収支・メンタル状態を長期的に分析できる仕組みとして、このツールを開発しました。

## 主な機能

- ターミナルからポーカーセッション情報を入力
- Notionデータベースへ自動記録
- EV Gap の自動計算
- Actual bb/100 の自動計算
- EV bb/100 の自動計算
- Tilt Level の記録
- A-Game Score の記録
- Memo の記録
- Session Date の自動記録
- 入力バリデーション
  - ハンド数は1以上のみ
  - Tilt Level は1〜5のみ
  - A-Game Score は1〜5のみ
- Notion APIエラー時の初心者向け説明表示

## 使用技術

- Python
- Notion API
- python-dotenv
- requests
- Git / GitHub
- PowerShell

## Notionデータベースの列構成

Notion側には、以下の列を作成する必要があります。

| 列名 | 種類 |
|---|---|
| Name | タイトル |
| Session Date | 日付 |
| Hands | 数値 |
| Actual bb | 数値 |
| EV bb | 数値 |
| EV Gap | 数値 |
| Actual bb/100 | 数値 |
| EV bb/100 | 数値 |
| Tilt Level | 数値 |
| A-Game Score | 数値 |
| Memo | テキスト |

列名は Pythonコード内の `properties` と完全一致している必要があります。  
大文字小文字、スペース、スラッシュ、ハイフンも一致必須です。

## セットアップ方法

### 1. リポジトリをクローン

```powershell
git clone https://github.com/xiuwukaben/poker-notion-tracker.git
cd poker-notion-tracker
```

### 2. 仮想環境を作成

```powershell
python -m venv .venv
```

### 3. 仮想環境のPythonでライブラリをインストール

```powershell
.\.venv\Scripts\pip.exe install -r requirements.txt
```

### 4. `.env` を作成

`.env.example` を参考にして、`.env` ファイルを作成します。

```env
NOTION_TOKEN=your_notion_integration_token_here
NOTION_DATABASE_ID=your_notion_database_id_here
```

実際の `.env` には、自分のNotion内部インテグレーションシークレットとデータベースIDを入力します。

## 使い方

以下のコマンドで実行します。

```powershell
.\.venv\Scripts\python.exe main.py
```

実行すると、ターミナル上で以下の情報を入力します。

```text
Hands:
Actual bb:
EV bb:
Tilt Level:
A-Game Score:
Memo:
```

入力が完了すると、Notionデータベースにセッション記録が追加されます。

## 構文チェック

コードの構文チェックは以下で行います。

```powershell
.\.venv\Scripts\python.exe -m py_compile main.py
```

## 今後の改善予定

- Stakes の追加
- Game Type の追加
- CSV出力
- matplotlib によるグラフ化
- Streamlit によるWebアプリ化
- 分散分析
- モンテカルロシミュレーション
- note記事化

## 注意事項

`.env` にはNotion APIトークンなどの秘密情報が含まれるため、GitHubには絶対にアップロードしないでください。

このリポジトリでは、以下のファイル・フォルダを `.gitignore` に追加しています。

```gitignore
.env
.venv/
__pycache__/
*.pyc
```