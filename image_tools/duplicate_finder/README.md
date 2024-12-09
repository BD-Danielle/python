# 重複圖片檢測與清理工具

這個工具可以幫助你找出並管理資料夾中的重複圖片。它能夠：
- 自動檢測重複圖片
- 基於圖片拍攝時間重新命名檔案
- 選擇性刪除重複檔案

## 環境需求
- Python 3.6 或更高版本
- 支援的作業系統：Windows, macOS, Linux

## 安裝步驟

1. 克隆或下載專案： 
```bash
git clone [專案網址]
cd [專案資料夾]
```
2. 創建虛擬環境：
```bash
# 創建虛擬環境
python3 -m venv venv

# 啟動虛擬環境
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```
3. 安裝依賴套件：
```bash
# 使用 requirements.txt 安裝所有必要的套件
pip install -r requirements.txt
```

## 使用方法

1. 確保虛擬環境已啟動（終端機前方應顯示 `(venv)`）

2. 執行程式：
```bash
python find_duplicate_images.py
```

3. 根據提示輸入要檢查的圖片資料夾路徑

4. 程式會：
   - 重新命名所有圖片（基於拍攝時間）
   - 顯示找到的重複圖片
   - 詢問是否要刪除重複檔案

## 功能說明

- 支援的圖片格式：PNG, JPG, JPEG, BMP, GIF
- 使用感知哈希算法比對圖片
- 保留最早的檔案，刪除重複檔案
- 基於 EXIF 數據或檔案創建時間重命名

## 注意事項

- 建議在執行刪除操作前備份重要資料
- 程式會保留原始檔案，只刪除重複的檔案
- 每次使用前都需要啟動虛擬環境

## 退出程式

1. 程式執行完成後，可以退出虛擬環境：
```bash
deactivate
```

2. 如果不再需要使用虛擬環境，可以刪除虛擬環境目錄：
```bash
rm -rf venv
```

## 常見問題

Q: 為什麼需要虛擬環境？
A: 虛擬環境可以確保專案的依賴不會與系統其他 Python 專案衝突。

Q: 如何確認我在虛擬環境中？
A: 終端機提示符前方應該顯示 `(venv)`。

Q: 找不到某些套件？
A: 確保你已啟動虛擬環境並執行 `pip install -r requirements.txt`。

## 作者
[CYL]

## 授權
This project is licensed under the GNU GPL v3 License.

Copyright (c) 2024 CYL

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation.

See [LICENSE](LICENSE) for more information.

```tree
python/
├── README.md                    # 主目錄說明文件
│
├── image_tools/                 # 圖片處理相關專案
│   ├── duplicate_finder/       # 重複圖片檢測專案
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── venv/
│   │   └── find_duplicate_images.py
│   │
│   └── image_converter/        # 圖片轉換專案（示例）
│       ├── README.md
│       ├── requirements.txt
│       ├── venv/
│       └── convert_images.py
│
├── web_tools/                  # 網頁相關專案
│   ├── web_scraper/
│   └── api_tester/
│
├── data_analysis/             # 數據分析專案
│   ├── data_cleaner/
│   └── visualizer/
│
└── utils/                     # 通用工具
    ├── file_handlers/
    └── common_functions/
```
