# -*- coding: utf-8 -*-
import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')  # 確保終端支持 UTF-8

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

    print("\n以下方案已成功複製至 gw_install：")
    for file in selected_files:
        print(f"- {file}")

    for file in selected_files:
        shutil.copy(os.path.join(dialect_dir, file), os.path.join(target_dir, file))


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
            print("\n警告：已配置詞庫文件不完整，缺少以下文件：")
            for file in missing_data_files:
                print(f"- {file}")
            print("\n將使用默認詞庫。")
            copy_dir = dictionary_dir
        else:
            use_existing = input("\n是否使用已配置詞庫文件？(y/n): ").strip().lower() == 'y'
            copy_dir = data_dir if use_existing else dictionary_dir
    else:
        print("\n並無已配置詞庫文件，將直接使用默認詞庫")
        print("用家可使用 'gw_custom' 內建腳本添增詞庫，改善打字體驗。")
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
    print("\n=== 第五步：選擇漢英混打等級 ===\n")
    print("【Nano】僅提供最基本英文混合輸入功能，只支持最常見英文單詞")
    print("【Super】使用40萬大詞庫，提供進一步英文混合輸入功能，但對打字體驗有少許影響")
    print("【None】不複製漢英混打方案\n")

    custom_dir = os.path.join(script_dir, "gw_custom")
    choice = input("請選擇漢英混打等級 (Nano/Super/None): ").strip().lower()

    if choice not in ["nano", "super", "none"]:
        print("\n未選擇任何等級，默認選擇 Easy English Nano。")
        choice = "nano"

    if choice == "none":
        print("\n已選擇不複製漢英混打，將不進行任何文件複製。")
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

import os

def handle_switches(target_dir):
    print("\n=== 第六步：配置輸入法默認選項 ===")
    schema_path = os.path.join(target_dir, "gukwan.schema.yaml")

    # 讀取文件內容
    with open(schema_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    explanations = {
        "ascii_mode": "「粵文模式」・「英文模式」",
        "full_shape": "「半角字形」・「全角字形」",
        "simplification": "「深筆字」・「簡筆字」",
        "ascii_punct": "「中式標點」・「西式標點」",
        "emoji_cantonese_suggestion": "「無繪文字」・「有繪文字」（粵語表情建議功能）"
    }

    new_lines = []
    inside_switches = False
    selected_options = {}

    for i, line in enumerate(lines):
        stripped_line = line.strip()
        
        if stripped_line.startswith("switches:"):
            inside_switches = True  # 進入 switches 節點
            new_lines.append(line)
            continue
        
        if inside_switches:
            if "name:" in stripped_line:
                switch_name = stripped_line.split(":")[1].strip()
                if switch_name in explanations:
                    print(f"\n{switch_name}: {explanations[switch_name]}")

                    reset_index = None
                    if i + 1 < len(lines) and "reset:" in lines[i + 1].strip():
                        reset_index = i + 1
                        current_reset = lines[i + 1].strip()
                        if "#reset:" in current_reset:
                            default_choice = "保留上一次狀態"
                        else:
                            default_choice = "reset: 0" if "reset: 0" in current_reset else "reset: 1"

                    print("1. 默認開啓第一選項 (reset: 0)")
                    print("2. 默認開啓第二選項 (reset: 1)")
                    print("3. 保留上一次狀態 (#reset: 0)")
                    choice = input(f"請輸入選擇編號，不輸入則使用默認選項 [默認: {default_choice}]: ").strip()

                    if choice == "1":
                        selected_reset = "reset: 0"
                    elif choice == "2":
                        selected_reset = "reset: 1"
                    elif choice == "3":
                        selected_reset = "# reset: 0"
                    else:
                        selected_reset = current_reset  # 保留原始設定

                    selected_options[switch_name] = selected_reset

                    if reset_index:
                        lines[reset_index] = f"    {selected_reset}\n"

            elif stripped_line == "":
                inside_switches = False  # 離開 switches 區塊

        new_lines.append(line)

    # 將修改後的內容寫回 YAML 文件
    with open(schema_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print("\n輸入法配置已更新：")
    for name, option in selected_options.items():
        print(f"- {name}: {option}")

def handle_mixed_language(target_dir):
    print("\n=== 第七步：配置漢英混打 ===")
    schema_path = os.path.join(target_dir, "gukwan.schema.yaml")

    # 讀取文件內容
    with open(schema_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 詢問用戶是否開啟漢英混打
    choice = input("\n是否開啟漢英混打？(y/n): ").strip().lower()

    if choice == 'y':
        print("\n已選擇開啟漢英混打，保持現有設置。")
        print("請確保之前第五步有複製漢英混打文件，或將無法使用漢英混打。")
        return

    elif choice == 'n':
        modified_lines = []
        for line in lines:
            stripped_line = line.strip()

            # 需要註釋掉的項目
            keywords = [
                "- gukwan-melt-eng",
                "- table_translator@gukwan-melt-eng",
                "- lua_filter@*autocap_filter",
                "- lua_filter@*en_spacer"
            ]

            # 如果行內有關鍵字，則加上 #
            if any(keyword in stripped_line for keyword in keywords) and not stripped_line.startswith("#"):
                modified_lines.append("#" + line)
            else:
                modified_lines.append(line)

        # 將修改後的內容寫回 YAML 文件
        with open(schema_path, 'w', encoding='utf-8') as f:
            f.writelines(modified_lines)

        print("\n已成功禁用漢英混打功能！")

    else:
        print("\n無效輸入，保持現有設置。")

import os

def explain_three_spelling():
    print("\n=== 第八步：三拼設置 ===")
    print("菊韻三拼輸入能幫閣下增快打字速度，同時亦支持傳統全拼輸入——即聲母+韻母+聲調。\n")

    more_info = input("是否需要更多說明？(y/n): ").strip().lower()
    if more_info == 'y':
        print("\n菊韻三拼，兼具靈活與精確，習之則捷，棄之亦無礙。使用三拼不礙使用『傳統全拼』——聲母+韻母+聲調，自由掌控輸入方式。")
        print("三拼直覺易學，令閣下更快找到字詞！無論你是習慣省略還是精準輸入，都能隨心所欲。")
        print("\n### 子音（聲母）###")
        print("- 不區分平翹日以之方言（多數方言）")
        print("  - 以 'q' 輸入 'kw'，如「裙」 'kwan' 則爲 'qan'")
        print("  - 以 'x' 輸入 'gw'，如「轟」 'gwang' 則爲 'xar'")
        print("  - 以 'r' 輸入 'ng'，如「我」 'ngo' 則爲 'ngo'（不支持單獨成韻）")
        print("- 區分平翹日以之方言（僅 'gukwan-default'）")
        print("  - 以'z'輸入'zh'（實質模糊音，默認關閉）")
        print("  - 以'c'輸入'ch'（實質模糊音，默認關閉）")
        print("  - 以's'輸入'sh'（實質模糊音，默認關閉）")
        print("  - 以 'q' 輸入 'kw'")
        print("  - 以 'x' 輸入 'gw'")
        print("  - 以'r'輸入'ng'｜'ngi'｜'nj'：如「言」'ngin'則爲'rin'，如「仍」'njing'則爲'rir'")
        print("\n### 母音（韻母）###")
        print("- 無韻尾情況（如'laa'，'loe') 等）")
        print("  - 以'a'輸入'aa'：如「瓜」'gwaa'則爲'xa'（此選項關閉將影響打字，故不關閉）")
        print("  - 以'y'輸入'yu'（'jyu'）：如「擧」'gyu'則爲'gy'（此選項關閉將影響打字，故不關閉）")
        print("- 有韻尾情況（如'laang' ，'loeng' 等）")
        print("  - 以'e'輸入'oe'：如「涼」'loeng'則爲'ler'")
        print("  - 以'r'輸入'aa'：如「逛」'gwaang'則爲'xrr'")
        print("  - 以'y'輸入'yu'（'jyu'）:如「血」'hyut'則爲'hyt'（此選項關閉將影響打字，故不關閉）")
        print("  - 以'u'輸入'eo'：如「論」'leon'則爲'lun'")
        print("\n- 以下三拼僅部分方案適用")
        print("  - 以'r/e'輸入'ae'：如「斬」'zhaem'則爲'z(h)aam'｜'z(h)rm'｜'z(h)em'（僅'gukwan-default'）")
        print("  - 以'u'輸入'oo'【僅限'ooi'】：如「淚」'looi'則爲'lui'")
        print("  - 以'o'輸入'oo'【僅限'oong/ook'】：如「朗」'loong'則爲'lor'")

def handle_three_spelling(target_dir):
    explain_three_spelling()

    choice = input("\n是否要使用三拼？(y/n): ").strip().lower()

    if choice == "y" or choice not in ["y", "n"]:
        print("\n已選擇使用三拼，保持現有設置。")
        return

    print("\n已選擇關閉三拼，將禁用相關功能。")

    # 排除不需要更改的文件
    excluded_files = [
        "gukwan.schema.yaml",
        "gukwan-melt-eng.schema.yaml",
        "jyut6ping3-gw.schema.yaml",
        "jyut6ping3-gw-cp.schema.yaml"
    ]

    # 需要修改的 derive 設定
    derive_keywords = [
        "- derive/^kw/q/",
        "- derive/^gw/x/",
        "- derive/^nj/r/",
        "- derive/^ng([aeiouy])/r$1/",
        "- derive/([aeiouy])ng/$1r/",
        "- derive/aa([iumnptkr]|ng)/r$1/",
        "- derive/oe(ng|k|r)/e$1/",
        "- derive/eo([ntiy])/u$1/",
        "- derive/oo(i|y)/u$1/"
    ]

    modified_files = []

    for file_name in os.listdir(target_dir):
        if file_name.endswith(".yaml") and file_name not in excluded_files:
            file_path = os.path.join(target_dir, file_name)

            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            modified_lines = []
            modified = False

            for line in lines:
                stripped_line = line.strip()
                if any(keyword in stripped_line for keyword in derive_keywords) and not stripped_line.startswith("#"):
                    modified_lines.append("#" + line)  # 註釋掉
                    modified = True
                else:
                    modified_lines.append(line)

            if modified:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(modified_lines)

                modified_files.append(file_name)

    if modified_files:
        print("\n已成功禁用三拼功能，修改的文件如下：")
        for file in modified_files:
            print(f"- {file}")
    else:
        print("\n未修改任何文件。\n")

def main():
    print("歡迎使用菊韻方案自定義腳本")
    print("提示：運行腳本將覆蓋 gw_install 相關文件。")
    script_dir = os.getcwd()
    target_dir = os.path.join(script_dir, "gw_install")
    
    if input("\n是否開始腳本？(y/n): ").strip().lower() != 'y':
        exit()

    os.makedirs(target_dir, exist_ok=True)

    only_standard_cantonese = input("\n是否只需要標準粵拼（rime-cantonese菊韻版｜廣州話）方案？(y/n): ").strip().lower() == 'y'

    check_folders(script_dir, target_dir)
    check_files(script_dir, target_dir)
    handle_trime(script_dir, target_dir)

    if only_standard_cantonese:
        print("\n=== 第三步：選擇方言點方案 ===")
        print("由於閣下選擇只需要標準方案，故跳過此步。")
    else:
        handle_dialects(script_dir, target_dir)

    handle_custom(script_dir, target_dir)
    handle_easy_english(script_dir, target_dir)
    handle_switches(target_dir)
    handle_mixed_language(target_dir)

    if only_standard_cantonese:
        print("\n=== 第八步：三拼設置 ===")
        print("由於閣下選擇只需要標準方案，故跳過此步。")
    else:
        handle_three_spelling(target_dir)

    print("\n=== ✅ 菊韻設定完成 ===\n")
    print("請將 gw_install 內所有文件複製至程序文件夾。然後進入輸入法選擇菊韻方案，竝重新部署。\n")
    print("提示：請確保閣下已安裝 rime-cantonese，此爲菊韻必選前置方案。缺少 rime-cantonese 菊韻將無法使用。\n")
    input("按 Enter 鍵退出...")

if __name__ == "__main__":
    main()
