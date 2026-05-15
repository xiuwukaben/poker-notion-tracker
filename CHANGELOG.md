# Changelog

このファイルでは、Poker Notion Tracker の主な変更履歴を記録します。

## v0.1.0 - First working version

### Added

- ターミナルからポーカーセッション情報を入力するCLI機能
- Notion APIを使ったNotionデータベースへの自動記録
- ハンド数の記録
- 実収支 [bb] の記録
- EV収支 [bb] の記録
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
- `.env` による秘密情報管理
- `.env.example` の追加
- `.gitignore` による秘密情報・仮想環境・キャッシュファイルの除外
- `requirements.txt` による依存ライブラリ管理
- READMEへのセットアップ方法・使い方・実行例の追加

### Notes

このバージョンは、Poker Notion Tracker の最初の動作版です。

CLIからセッション情報を入力し、Notionに記録するところまでをPhase 1 / v0.1として完成扱いにします。

## Planned

今後の改善候補です。

- Stakes の追加
- Game Type の追加
- CSV出力
- matplotlib によるグラフ化
- Streamlit によるWebアプリ化
- 分散分析
- モンテカルロシミュレーション
- note記事化