# -*- coding: utf-8 -*-
import os
import shutil
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')  # 確保終端支持 UTF-8

def check_required_dictionary_files():
    required_files = [
        "gukwan.dict.yaml",
        "gukwan-alt.dict.yaml",
        "gukwan-asp.dict.yaml",
        "gukwan-alt-asp.dict.yaml",
        "jyut6ping3-gw.dict.yaml"
    ]
    dictionary_folder = "Dictionary"
    missing = []
    for filename in required_files:
        path = os.path.join(dictionary_folder, filename)
        if not os.path.isfile(path):
            missing.append(path)
    if missing:
        print("錯誤：在 '{}' 下找不到以下文件：".format(dictionary_folder))
        for f in missing:
            print("  - " + f)
        sys.exit(1)
    return required_files, dictionary_folder

def search_dict_yaml_files():
    search_dirs = ["Dict_Converted", "Dict_Removed"]
    found_files = []
    for folder in search_dirs:
        pattern = os.path.join(folder, "*dict.yaml")
        files = glob.glob(pattern)
        if files:
            for f in files:
                found_files.append((folder, f))
    if not found_files:
        print("錯誤：在 'Dict_Converted' 同 'Dict_Removed' 中找不到任何詞庫文件（以 'dict.yaml' 結尾）")
        sys.exit(1)
    return found_files

def prompt_select_files(found_files):
    print("\n在 'Dict_Converted' & 'Dict_Removed' 找到以下詞庫：")
    print("菊韻不能使用簡體詞庫，請確保詞庫爲繁體（OpenCC 標準），否則菊韻無法正常調用。\n")
    for idx, (folder, full_path) in enumerate(found_files, start=1):
        print("  {}. [{}] {}".format(idx, folder, os.path.basename(full_path)))
    
    choice = input("\n是否添加全部詞庫？(y/n)：").strip().lower()
    if choice == "y":
        return found_files
    else:
        indices = input("\n請輸入要添加詞庫之編號（逗號分隔，例如 1,3）：")
        try:
            selected_indices = [int(x.strip()) for x in indices.split(",") if x.strip().isdigit()]
        except Exception:
            print("輸入不正確，腳本停止。")
            sys.exit(1)
        selected = []
        for num in selected_indices:
            if num < 1 or num > len(found_files):
                print("錯誤：編號 {} 超出範圍。".format(num))
                sys.exit(1)
            selected.append(found_files[num - 1])
        return selected

def copy_selected_files(selected_files):
    data_folder = "data"
    ext_dicts_folder = os.path.join(data_folder, "ext_dicts")
    os.makedirs(ext_dicts_folder, exist_ok=True)
    
    for src_folder, src_path in selected_files:
        dest_path = os.path.join(ext_dicts_folder, os.path.basename(src_path))
        shutil.copy(src_path, dest_path)
        print("已複製 {} 到 {}".format(src_path, dest_path))
    return data_folder, ext_dicts_folder

def modify_templates(required_files, dictionary_folder, selected_files, data_folder):
    for tmpl_filename in required_files:
        tmpl_path = os.path.join(dictionary_folder, tmpl_filename)
        try:
            with open(tmpl_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            print("讀取 {} 時發生錯誤: {}".format(tmpl_path, e))
            sys.exit(1)
        
        # 找到第一個內容為 "..."（去除空白）的行
        insert_index = None
        for idx, line in enumerate(lines):
            if line.strip() == "...":
                insert_index = idx
                break
        if insert_index is None:
            print("錯誤：在模版文件 {} 中找不到 '...' 那一行。".format(tmpl_path))
            sys.exit(1)
        
        # 為每一個選擇的文件生成插入行
        insertion_lines = []
        for src_folder, src_path in selected_files:
            base = os.path.basename(src_path)
            if base.endswith(".dict.yaml"):
                base_no_suffix = base[:-len(".dict.yaml")]
            else:
                base_no_suffix = base
            insertion_lines.append("  - ex_dicts/{}\n".format(base_no_suffix))
        
        # 將插入的內容加入原來的文件內容中
        new_lines = lines[:insert_index] + insertion_lines + lines[insert_index:]
        dest_template_path = os.path.join(data_folder, tmpl_filename)
        try:
            with open(dest_template_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
        except Exception as e:
            print("寫入 {} 時發生錯誤: {}".format(dest_template_path, e))
            sys.exit(1)
        print("已修改模版文件並保存到 {}".format(dest_template_path))

def main():
    # 步驟 1：檢查 Dictionary 目錄下必須存在的四個文件
    required_files, dictionary_folder = check_required_dictionary_files()
    
    # 步驟 2：在 Dict_Converted 與 Dict_Removed 中查找以 dict.yaml 結尾的文件
    found_files = search_dict_yaml_files()
    
    # 步驟 3 & 4：列出找到的文件並詢問使用者選擇添加哪些文件
    selected_files = prompt_select_files(found_files)
    
    # 步驟 5：創建 data/ext_dicts 並將選擇的文件複製過去
    data_folder, ext_dicts_folder = copy_selected_files(selected_files)
    
    # 步驟 6：根據 Dictionary 中的模板文件進行插入修改，
    # 修改後的文件存放在 data 目錄下
    modify_templates(required_files, dictionary_folder, selected_files, data_folder)
    
    # 步驟 7：完成後通知使用者
    print("\n✅ 詞庫已完成修改，請將data內所有文件放置於中州韻程序文件夾，竝重新部署，以調用新詞庫。")
    input("按 Enter 鍵退出...")

if __name__ == "__main__":
    main()