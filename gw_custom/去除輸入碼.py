#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import shutil

def copy_folder(src, dst):
    """
    複製資料夾。使用 copytree，若目的資料夾已存在則合併內容（需要 Python 3.8+）。
    """
    try:
        shutil.copytree(src, dst, dirs_exist_ok=True)
    except Exception as e:
        print(f"複製資料夾 {src} 到 {dst} 時出錯：{e}")
        sys.exit(1)

def copy_file(src, dst):
    """
    複製單個文件。
    """
    try:
        shutil.copy2(src, dst)
    except Exception as e:
        print(f"複製文件 {src} 到 {dst} 時出錯：{e}")
        sys.exit(1)

def main():
    # 取得當前腳本所在的目錄
    base_dir = os.path.abspath(os.path.dirname(__file__))
    gw_install = os.path.join(base_dir, "gw_install")
    if not os.path.exists(gw_install):
        os.makedirs(gw_install)
    
    # 1. 詢問是否開始腳本
    start = input("是否開始腳本？(y/n): ").strip().lower()
    if start != 'y':
        print("用戶取消，退出腳本。")
        sys.exit(0)
    
    # 2. 複製指定文件夾到 gw_install
    mandatory_dirs = ["en_dicts", "gw_dicts", "lua", "opencc"]
    optional_dirs = ["ext_dicts"]
    
    # 複製必需的文件夾
    for folder in mandatory_dirs:
        src_folder = os.path.join(base_dir, folder)
        if not os.path.isdir(src_folder):
            print(f"錯誤：缺少必需文件夾 \"{folder}\"，請檢查文件完整性。")
            sys.exit(1)
        dst_folder = os.path.join(gw_install, folder)
        copy_folder(src_folder, dst_folder)
        print(f"文件夾 \"{folder}\" 複製完成。")
    
    # 複製可選文件夾 ext_dicts（如果存在）
    for folder in optional_dirs:
        src_folder = os.path.join(base_dir, folder)
        if os.path.isdir(src_folder):
            dst_folder = os.path.join(gw_install, folder)
            copy_folder(src_folder, dst_folder)
            print(f"可選文件夾 \"{folder}\" 複製完成。")
        else:
            print(f"可選文件夾 \"{folder}\" 不存在，跳過此步驟。")
    
    # 3. 複製指定文件到 gw_install
    files_to_copy = [
        "emoji_cantonese.recipe.yaml",
        "emoji_cantonese_suggestion.yaml",
        "gukwan.schema.yaml",
        "gukwan-extended.dict.yaml",
        "jyut6ping3-gw.schema.yaml",
        "jyut6ping3-gw-cp.schema.yaml",
        "symbols-gukwan.yaml"
    ]
    for file_name in files_to_copy:
        src_file = os.path.join(base_dir, file_name)
        if not os.path.isfile(src_file):
            print(f"錯誤：缺少文件 \"{file_name}\"，請檢查文件完整性。")
            sys.exit(1)
        dst_file = os.path.join(gw_install, file_name)
        copy_file(src_file, dst_file)
        print(f"文件 \"{file_name}\" 複製完成。")
    
    # 4. 詢問用戶是否使用 TRIME 同文輸入法，如果是則複製菊韻.trime.yaml
    use_trime = input("是否使用 TRIME 同文輸入法？(y/n): ").strip().lower()
    if use_trime == 'y':
        trime_file = "菊韻.trime.yaml"
        src_trime = os.path.join(base_dir, trime_file)
        if not os.path.isfile(src_trime):
            print(f"錯誤：缺少文件 \"{trime_file}\"，請檢查文件完整性。")
            sys.exit(1)
        dst_trime = os.path.join(gw_install, trime_file)
        copy_file(src_trime, dst_trime)
        print(f"文件 \"{trime_file}\" 複製完成。")
    else:
        print("未選用 TRIME 同文輸入法，跳過相關文件複製。")
    
    # 5. 掃描 gw_dialects 目錄下以 schema.yaml 結尾的文件
    gw_dialects_dir = os.path.join(base_dir, "gw_dialects")
    if os.path.isdir(gw_dialects_dir):
        schema_files = [f for f in os.listdir(gw_dialects_dir) if f.endswith("schema.yaml")]
        if schema_files:
            dialects = {}
            print("請選擇需要的方言文件（將顯示文件名稱及其內容中的 'name:' 值）：")
            for idx, filename in enumerate(schema_files):
                src_filepath = os.path.join(gw_dialects_dir, filename)
                name_val = None
                with open(src_filepath, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip().startswith("name:"):
                            # 過濾掉 "name:" 並去掉首尾空白
                            name_val = line.strip().split("name:", 1)[1].strip()
                            break
                if not name_val:
                    name_val = "未知名稱"
                dialects[idx] = (filename, name_val)
                print(f"{idx}: {filename} -> {name_val}")
            choice = input("請輸入選項編號：").strip()
            try:
                choice = int(choice)
                if choice not in dialects:
                    raise ValueError
            except ValueError:
                print("無效的選擇，退出腳本。")
                sys.exit(1)
            selected_file = dialects[choice][0]
            src_selected = os.path.join(gw_dialects_dir, selected_file)
            dst_selected = os.path.join(gw_install, selected_file)
            copy_file(src_selected, dst_selected)
            print(f"已複製方言文件: {selected_file}")
        else:
            print("在 gw_dialects 目錄中未找到符合要求的 schema.yaml 文件，跳過此步驟。")
    else:
        print("未找到 gw_dialects 文件夾，跳過此步驟。")
    
    # 6. 處理 gw_custom 文件夾中的詞庫文件
    gw_custom_dir = os.path.join(base_dir, "gw_custom")
    if os.path.isdir(gw_custom_dir):
        data_dir = os.path.join(gw_custom_dir, "data")
        dictionary_dir = os.path.join(gw_custom_dir, "Dictionary")
        if os.path.isdir(data_dir):
            use_preconfigured = input("檢測到 gw_custom/data 文件夾，是否使用已配置好的詞庫文件？(y/n): ").strip().lower()
            if use_preconfigured == 'y':
                # 複製 data 目錄所有內容到 gw_install
                for item in os.listdir(data_dir):
                    src_item = os.path.join(data_dir, item)
                    dst_item = os.path.join(gw_install, item)
                    if os.path.isdir(src_item):
                        copy_folder(src_item, dst_item)
                    else:
                        copy_file(src_item, dst_item)
                print("已複製 gw_custom/data 內所有文件到 gw_install。")
            else:
                if os.path.isdir(dictionary_dir):
                    for item in os.listdir(dictionary_dir):
                        src_item = os.path.join(dictionary_dir, item)
                        dst_item = os.path.join(gw_install, item)
                        if os.path.isdir(src_item):
                            copy_folder(src_item, dst_item)
                        else:
                            copy_file(src_item, dst_item)
                    print("已複製 gw_custom/Dictionary 內所有文件到 gw_install。")
                else:
                    print("錯誤：在 gw_custom 內未找到 Dictionary 文件夾。")
                    sys.exit(1)
        else:
            print("gw_custom 內未發現 data 文件夾。您可以使用自帶腳本增加自己的詞庫來改善打字體驗。")
            if os.path.isdir(dictionary_dir):
                for item in os.listdir(dictionary_dir):
                    src_item = os.path.join(dictionary_dir, item)
                    dst_item = os.path.join(gw_install, item)
                    if os.path.isdir(src_item):
                        copy_folder(src_item, dst_item)
                    else:
                        copy_file(src_item, dst_item)
                print("已複製 gw_custom/Dictionary 內所有文件到 gw_install。")
            else:
                print("錯誤：在 gw_custom 內未找到 Dictionary 文件夾。")
                sys.exit(1)
    else:
        print("未找到 gw_custom 文件夾，跳過此步驟。")
    
    # 7. 詢問用戶選擇漢英混打等級
    print("\n輸入法提供兩個等級的漢英混打:")
    print("  1. Easy English Nano（最基本，不大影響打字）")
    print("  2. Easy English Super（進階英文輸入，對打字有些影響）")
    english_choice = input("請選擇(輸入1或2): ").strip()
    if english_choice == '1':
        ee_dir = os.path.join(gw_custom_dir, "Easy English Nano")
    elif english_choice == '2':
        ee_dir = os.path.join(gw_custom_dir, "Easy English Super")
    else:
        print("無效選擇，退出腳本。")
        sys.exit(1)
    
    if os.path.isdir(ee_dir):
        for item in os.listdir(ee_dir):
            src_item = os.path.join(ee_dir, item)
            dst_item = os.path.join(gw_install, item)
            if os.path.isdir(src_item):
                copy_folder(src_item, dst_item)
            else:
                copy_file(src_item, dst_item)
        print(f"已複製 \"{os.path.basename(ee_dir)}\" 內的所有內容到 gw_install。")
    else:
        print(f"錯誤：未找到文件夾 \"{os.path.basename(ee_dir)}\"。")
        sys.exit(1)
    
    # 8. 提示用戶完成部署
    print("\n所有步驟已完成。")
    print("請打開輸入法調整設置，選擇菊韻方案，並重新部署。")
    
    # 增加 input 使腳本窗口不立即關閉
    input("按 Enter 鍵退出...")

if __name__ == "__main__":
    main()
