#!/bin/bash

set -e

# 現在の日付を変数に格納
current_date=$(/bin/date '+%Y%m%d%H%M%S')

# パス変数の設定
main_dir="/home/ubuntu"
minecraft_dir="${main_dir}/minecraft"
backup_dir="${main_dir}/bk/worlds"
backup_file="${backup_dir}/worlds_${current_date}.zip"

# バックアップを作成
cd "${minecraft_dir}"
zip -r "${backup_file}" worlds

# 1週間以上古いバックアップを削除
find ${backup_dir} -type f -name "worlds_*.zip" -mtime +7 -delete
