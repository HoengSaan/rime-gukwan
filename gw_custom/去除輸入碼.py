# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')  # 確保終端支持 UTF-8

def process_file(source_path, dest_path):
    """去除詞庫輸入碼"""
    with open(source_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    marker_found = False  

    for line in lines:
        if not marker_found:
            new_lines.append(line)
            if line.strip() == "...":
                marker_found = True
        else:
            new_line = line.split("\t", 1)[0] + "\n" if "\t" in line else line
            new_lines.append(new_line)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def main():
    source_folder = "Dict_Source"
    dest_folder = "Dict_Removed"
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    files_to_process = [f for f in os.listdir(source_folder) if f.endswith("dict.yaml")]

    if not files_to_process:
        print("\n錯誤：未在『Dict_Source』文件夾中找到 RIME 詞庫文件！")
        print("請將須去除輸入碼之詞庫放入『Dict_Source』。\n")
        input("按 Enter 鍵退出...")
        return

    print("\n找到以下文件:")
    for file in files_to_process:
        print(f" - {file}")

    choice = input("\n是否去除詞庫輸入碼？(y/n): ").strip().lower()
    if choice != 'y':
        print("已取消，腳本停止。")
        return

    for file in files_to_process:
        source_path = os.path.join(source_folder, file)
        dest_path = os.path.join(dest_folder, file)
        process_file(source_path, dest_path)
        print(f"詞庫 {file} 輸入碼已去除。")

    print("\n✅ 所有詞庫輸入碼已去除，請查看『Dict_Removed』資料夾。")
    print("菊韻不能使用簡筆詞庫，請使用『繁簡轉換.cmd』將詞庫轉成深筆。")
    print("請使用『詞庫調用.py』修改詞庫，以確保中州韻能正確調用新詞庫。")
    print("或自行創造新詞庫文件，並使用custom.yaml改變方案以調用新詞庫。\n")
    input("按 Enter 鍵退出...")

if __name__ == "__main__":
    main()
