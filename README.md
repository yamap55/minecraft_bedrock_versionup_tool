# minecraft_bedrock_versionup_tool

本リポジトリはMinecraft統合版のサーバを運営している際に、Minecraftのバージョンアップをするスクリプトを格納しています

## 環境
- Python: 3.6以上
  - 3.6.8, 3.10.12で動作確認済み
- Ubuntu 22.04

## 実行方法
1. Minecraftを停止
2. `python3 minecraft_version_up.py ${version}`
   - 例: `python3 minecraft_version_up.py 1.20.15.01`
3. Minecraftを起動
   - 良い機会なのでサーバーを再起動しても良いかもしれません
   - `sudo shutdown -r now`

※バージョンは https://www.minecraft.net/ja-jp/download/server/bedrock で確認可能

## 注意事項
- 以下のPATHを前提としていますので必要があれば変更してください
  - 作業ディレクトリ: `/home/ubuntu`
  - Minecraftディレクトリ: `/home/ubuntu/minecraft`
  - バックアップディレクトリ: `/home/ubuntu/bk`
