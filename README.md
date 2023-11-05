# minecraft_server_bedrock_tools

本リポジトリはMinecraft統合版のサーバを運営している際に、Minecraftのバージョンアップ、バックアップを行うスクリプトを格納しています

## 環境
- Python: 3.6以上
  - 3.6.8, 3.10.12で動作確認済み
- Ubuntu 22.04

## バージョンアップツール
1. Minecraftを停止
2. `python3 minecraft_version_up.py ${version}`
   - 例: `python3 minecraft_version_up.py 1.20.15.01`
3. Minecraftを起動
   - 良い機会なのでサーバーを再起動しても良いかもしれません
   - `sudo shutdown -r now`

※バージョンは https://www.minecraft.net/ja-jp/download/server/bedrock で確認可能

## バックアップツール
※cronで動かすことを想定しています

1. 実行権限を与える
   - `chmod +x worlds_backup.script.sh`
2. cronの設定
   - `crontab ./my_crontab_file`

## 注意事項
- 以下のPATHを前提としていますので必要があれば変更してください
  - 作業ディレクトリ: `/home/ubuntu`
  - Minecraftディレクトリ: `/home/ubuntu/minecraft`
  - バックアップディレクトリ: `/home/ubuntu/bk`
  - 本スクリプトが配置されるディレクトリ: `/home/ubuntu/tools`
