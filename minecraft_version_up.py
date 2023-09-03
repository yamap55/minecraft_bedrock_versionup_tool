#! /usr/bin/python3
from logging import basicConfig, DEBUG, getLogger
import argparse
import shutil
from datetime import datetime
import shutil
from pathlib import Path
import urllib.request
import zipfile
from typing import Tuple, List

basicConfig(level=DEBUG, format='{asctime} [{levelname:.4}] {name}: {message}', style='{')
logger = getLogger(__name__)
WORK_DIR = Path("/home/opc")
MINECRAFT_DIR = WORK_DIR / "minecraft"
BACKUP_DIR = WORK_DIR / "bk"
OVERWRITE_SETTING_FILES = ["permissions.json", "server.properties", "allowlist.json"]

def post_process(old_minecraft_path: Path, module_path: Path, bk_dir: Path):
    def zip_dir(target_dir_path: str, bk_path: Path):
        target_path = Path(target_dir_path)
        shutil.make_archive(bk_path / target_path.name, format='zip', root_dir=target_path.parent, base_dir=target_path.name)

    logger.info(f"backup dir zip.")
    zip_dir(old_minecraft_path, bk_dir)
    shutil.rmtree(old_minecraft_path)
    shutil.move(module_path, bk_dir)

def pre_process(work_dir: Path, minecraft_dir: Path) -> Tuple[Path, Path]:

    def get_minecraft_module(minecraft_module_name: str, base_path: Path) -> Path:
        logger.info(f"get minecraft module. {minecraft_module_name}")
        url = f"https://minecraft.azureedge.net/bin-linux/{minecraft_module_name}"
        destination = base_path / minecraft_module_name

        urllib.request.urlretrieve(url, destination)
        return destination

    def get_current_date():
        return datetime.now().strftime('%Y%m%d')

    def backup_directory(target_dir: Path, backup_dir: Path):
        logger.info(f"backup minecraft dir. {backup_dir}")
        shutil.copytree(target_dir, backup_dir)

    minecraft_module_name = f"bedrock-server-{version}.zip"
    module_path = get_minecraft_module(minecraft_module_name, work_dir)

    backup_dir = work_dir / f"minecraft_bk_{get_current_date()}"
    backup_directory(minecraft_dir, backup_dir)
    return module_path, backup_dir

def main_process(module_path: Path, backup_dir: Path, minecraft_dir: Path, overwrite_setting_files: List[str]):
    def copy_and_overwrite_minecraft_setting_files(dir: Path, file_names: List[str]):
        logger.info(f"copy minecraft module to minecraft dir.")
        for file_name in file_names:
            shutil.copy2(dir / file_name, minecraft_dir / file_name)

    def unzip_minecraft_module(module_path: Path, extract_path: Path):
        logger.info(f"unzip minecraft module. {module_path}")
        with zipfile.ZipFile(module_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

    unzip_minecraft_module(module_path, minecraft_dir)
    copy_and_overwrite_minecraft_setting_files(
        backup_dir,
        overwrite_setting_files
    )

def main(version: str):
    logger.info(f"start minecraft version up. version: {version}, work_dir: {WORK_DIR}, minecraft_dir: {MINECRAFT_DIR}")

    # 前処理
    module_path, backup_dir = pre_process(WORK_DIR, MINECRAFT_DIR)
    
    # 本処理
    main_process(module_path, backup_dir, MINECRAFT_DIR, OVERWRITE_SETTING_FILES)

    # 後処理
    post_process(backup_dir, module_path, BACKUP_DIR)

    logger.info("minecraft version up finished.")
    logger.info("please shutdown now. `sudo shutdown -r now`")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Minecraft version up")
    parser.add_argument(
        'version',
        type=str,
        help='Please specify the version of Minecraft to be updated. https://www.minecraft.net/ja-jp/download/server/bedrock',
    )
    args = parser.parse_args()
    version = args.version
    main(version)
