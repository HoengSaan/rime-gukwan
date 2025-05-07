# -*- coding: utf-8 -*-
import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')  # 確保終端支持 UTF-8

import os
import shutil

def check_folders(script_dir, target_dir):
    print("\n=== 第一步：複製必要文件 ===")
    required_folders = ["en_dicts", "gw_dicts", "lua", "opencc"]
    missing_folders = [folder for folder in required_folders if not os.path.exists(os.path.join(script_dir, folder))]

    if missing_folders:
        print(f"\n錯誤：缺少以下文件夾：{', '.join(missing_folders)}")
        print("請檢查文件完整性，或重新下載菊韻。\n")
        input("按 Enter 鍵退出...")
        exit()

    copied_folders = []
    for folder in required_folders + ["ext_dicts"]:
        source = os.path.join(script_dir, folder)
        if os.path.exists(source):
            shutil.copytree(source, os.path.join(target_dir, folder), dirs_exist_ok=True)
            copied_folders.append(folder)

    print("\n基底詞庫與腳本已成功複製至 gw_install：")
    for folder in copied_folders:
        print(f"- {folder}")

def check_files(script_dir, target_dir):
    required_files = [
        "emoji_cantonese.recipe.yaml", "emoji_cantonese_suggestion.yaml", "gukwan.schema.yaml",
        "gukwan-extended.dict.yaml", "jyut6ping3-gw.schema.yaml", "jyut6ping3-gw-cp.schema.yaml",
        "symbols-gukwan.yaml"
    ]
    missing_files = [file for file in required_files if not os.path.exists(os.path.join(script_dir, file))]

    if missing_files:
        print(f"\n錯誤：缺少以下文件：{', '.join(missing_files)}")
        print("請檢查文件完整性，或重新下載菊韻。\n")
        input("按 Enter 鍵退出...")
        exit()

    copied_files = []
    for file in required_files:
        shutil.copy(os.path.join(script_dir, file), os.path.join(target_dir, file))
        copied_files.append(file)

    print("\n基底方案已成功複製至 gw_install：")
    for file in copied_files:
        print(f"- {file}")

def handle_trime(script_dir, target_dir):
    print("\n=== 第二步：選擇同文主題 ===")
    print("\n使用菊韻自帶主題可改善同文打字體驗。")
    print("主題文件僅支持 TRIME 同文輸入法（Android），其他用家請跳過。")

    choice = input("\n是否需要 TRIME 主題？(y/n): ").strip().lower()

    if choice not in ['y', 'n']:
        print("\n無效輸入，默認不使用 TRIME 主題。")
        choice = 'n'

    if choice == 'y':
        trime_file = os.path.join(script_dir, "菊韻.trime.yaml")
        if os.path.exists(trime_file):
            shutil.copy(trime_file, os.path.join(target_dir, "菊韻.trime.yaml"))
            print("\n已選擇使用 TRIME 主題，菊韻.trime.yaml 已成功複製至 gw_install。\n")
        else:
            print("\n錯誤：缺少 菊韻同文主題文件")
            print("請檢查文件完整性，或重新下載菊韻。\n")
            input("按 Enter 鍵退出...")
            exit()
    else:
        print("\n你選擇了不使用 TRIME 主題，不進行任何文件複製。")

import os
import shutil

def handle_dialects(script_dir, target_dir):
    print("\n=== 第三步：選擇方言點方案 ===")
    dialect_dir = os.path.join(script_dir, "gw_dialects")
    if not os.path.exists(dialect_dir):
        print("\n錯誤：找不到 gw_dialects 文件夾")
        print("請檢查文件完整性，或重新下載菊韻。\n")
        input("按 Enter 鍵退出...")
        exit()

    dialect_files = [f for f in os.listdir(dialect_dir) if f.endswith("schema.yaml")]

    dialect_names = []
    for file in dialect_files:
        with open(os.path.join(dialect_dir, file), 'r', encoding='utf-8') as f:
            for line in f:
                if "name:" in line:
                    dialect_names.append((file, line.split("name:")[-1].strip()))
                    break

    if not dialect_names:
        print("\n錯誤：未找到任何方言點方案")
        print("請檢查文件完整性，或重新下載菊韻。\n")
        input("按 Enter 鍵退出...")
        exit()

    print("\n廣州話（穗港澳）不需要任何方言點方案，請直接撳 '0' 跳過")
    print("構擬音僅供高級用家使用，一般用家毋須選擇。")
    print("可用的方案：")
    print("0. 不選擇任何方言點方案")
    for i, (file, name) in enumerate(dialect_names):
        print(f"{i+1}. {name} ({file})")

    choices = input("\n選擇所需方案文件（用逗號分隔，輸入0跳過）：").strip().split(",")
    
    selected_files = []
    for choice in choices:
        if choice == "0":
            print("\n你選擇了不使用任何方言點方案，跳過此步驟。")
            return
        
        if not choice.isdigit():
            print(f"警告：'{choice}' 不是有效選擇。")
            continue
        
        index = int(choice) - 1
        if index < 0 or index >= len(dialect_names):
            print(f"警告：'{choice}' 超出範圍。")
            continue
        
        selected_files.append(dialect_names[index][0])

    if not selected_files:
        print("\n未選擇任何方言點方案，跳過此步驟。")
        return

    print("\n已選擇方案：")
    for file in selected_files:
        print(f"- {file}")

    for file in selected_files:
        shutil.copy(os.path.join(dialect_dir, file), os.path.join(target_dir, file))

    print("\n方言點方案已成功複製至 gw_install！")

def handle_custom(script_dir, target_dir):
    print("\n=== 第四步：複製詞庫文件 ===")
    custom_dir = os.path.join(script_dir, "gw_custom")
    data_dir = os.path.join(custom_dir, "data")
    dictionary_dir = os.path.join(custom_dir, "Dictionary")
    required_dict_files = [
        "gukwan.dict.yaml", "gukwan-alt.dict.yaml", "gukwan-alt-asp.dict.yaml",
        "gukwan-asp.dict.yaml", "jyut6ping3-gw.dict.yaml"
    ]

    # 檢查 data 文件夾是否存在並完整
    if os.path.exists(data_dir):
        missing_data_files = [file for file in required_dict_files if not os.path.exists(os.path.join(data_dir, file))]
        
        if missing_data_files:
            print("\n警告：已配置的詞庫文件不完整，缺少以下文件：")
            for file in missing_data_files:
                print(f"- {file}")
            print("\n將使用默認詞庫。\n")
            copy_dir = dictionary_dir
        else:
            use_existing = input("\n是否使用已配置好的詞庫文件？(y/n): ").strip().lower() == 'y'
            copy_dir = data_dir if use_existing else dictionary_dir
    else:
        print("\n並無已配置詞庫文件，將直接使用默認詞庫")
        print("用家可使用 'gw_custom' 內建腳本添增私家詞庫，改善打字體驗。")
        copy_dir = dictionary_dir

    # 檢查 Dictionary 文件夾是否存在並完整
    if os.path.exists(copy_dir):
        missing_dict_files = [file for file in required_dict_files if not os.path.exists(os.path.join(copy_dir, file))]
        
        if missing_dict_files:
            print("\n錯誤：默認詞庫文件不完整，缺少以下文件：")
            for file in missing_dict_files:
                print(f"- {file}")
            print("請檢查文件完整性或重新下載菊韻。\n")
            input("按 Enter 鍵退出...")
            exit()

        copied_files = []
        for file in os.listdir(copy_dir):
            shutil.copy(os.path.join(copy_dir, file), os.path.join(target_dir, file))
            copied_files.append(file)

        print("\n已成功複製以下詞庫文件至 gw_install！：")
        for file in copied_files:
            print(f"- {file}")

    else:
        print("\n錯誤：找不到 Dictionary 文件夾")
        print("請檢查文件完整性或重新下載菊韻。\n")
        input("按 Enter 鍵退出...")
        exit()


def handle_easy_english(script_dir, target_dir):
    print("\n=== 第四步：選擇漢英混打等級 ===\n")
    print("【Nano】僅提供最基本英文混合輸入功能，只支持最常見英文單詞")
    print("【Super】使用40萬大詞庫，提供進一步英文混合輸入功能，但對打字體驗有少許影響")
    print("【None】不開啓漢英混打輸入功能\n")

    custom_dir = os.path.join(script_dir, "gw_custom")
    choice = input("請選擇漢英混打等級 (Nano/Super/None): ").strip().lower()

    if choice not in ["nano", "super", "none"]:
        print("\n未選擇任何等級，默認選擇 Easy English Nano。")
        choice = "nano"

    if choice == "none":
        print("\n已選擇不使用漢英混打，將不進行任何文件複製。")
        print("注意：若程序文件夾已有 'gukwan-melt-eng' 方案文件，則漢英混打不能被關閉")
        return

    folder = "Easy English Nano" if choice == "nano" else "Easy English Super"
    source = os.path.join(custom_dir, folder)

    if os.path.exists(source):
        copied_files = []
        for file in os.listdir(source):
            shutil.copy(os.path.join(source, file), os.path.join(target_dir, file))
            copied_files.append(file)

        print(f"\n已選擇 {folder}")

    else:
        print(f"\n錯誤：缺少 {folder} 文件夾")
        print("請檢查文件完整性，或重新下載菊韻。\n")
        input("按 Enter 鍵退出...")
        exit()

def main():
    print("提示：運行腳本將覆蓋 gw_install 相關文件。")
    script_dir = os.getcwd()
    target_dir = os.path.join(script_dir, "gw_install")
    
    if input("\n是否開始腳本？(y/n): ").strip().lower() != 'y':
        exit()

    os.makedirs(target_dir, exist_ok=True)
    
    check_folders(script_dir, target_dir)
    check_files(script_dir, target_dir)
    handle_trime(script_dir, target_dir)
    handle_dialects(script_dir, target_dir)
    handle_custom(script_dir, target_dir)
    handle_easy_english(script_dir, target_dir)

    print("\n=== ✅ 設定完成 ===\n")
    print("請將 gw_install 內所有文件複製至程序文件夾。然後進入輸入法選擇菊韻方案，竝重新部署。\n")
    input("按 Enter 鍵退出...")

if __name__ == "__main__":
    main()
