# minecraft_bedrock_versionup_tool

本リポジトリはMinecraft統合版のサーバを運営している際に、Minecraftのバージョンアップをするスクリプトを格納しています

## 環境
- Python: 3.6以上
  - 3.6.8でのみ動作確認済み
- Oracle Linux 8

## 実行方法
- `python minecraft_version_up.py ${version}`
- 例: `python minecraft_version_up.py 1.20.15.01`

※バージョンは https://www.minecraft.net/ja-jp/download/server/bedrock で確認可能

## 注意事項
- 以下のPATHを前提としていますので必要があれば変更してください
  - 作業ディレクトリ: `/home/opc`
  - Minecrftディレクトリ: `/home/opc/minecraft`
  - バックアップディレクトリ: `/home/opc/bk`
