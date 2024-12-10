# Python 專案集合

這是一個包含多個 Python 工具和應用的專案集合。每個子專案都是獨立的，並配有自己的文檔和環境設置。

## 專案結構
```
python/
├── image_tools/                 # 圖片處理工具集
│   ├── duplicate_finder/       # 重複圖片檢測工具
│   └── image_converter/        # 圖片轉換工具（開發中）
│
├── web_tools/                  # 網頁相關工具（計劃中）
├── data_analysis/             # 數據分析工具（計劃中）
└── utils/                     # 通用工具（計劃中）
```

## 已完成的專案

### 1. 重複圖片檢測工具 (duplicate_finder)
- 位置：`image_tools/duplicate_finder/`
- 功能：自動檢測和清理重複圖片
- [查看詳細說明](image_tools/duplicate_finder/README.md)

## 環境要求
- Python 3.6+
- 每個子專案都有自己的虛擬環境和依賴要求

## 使用指南

1. 克隆專案：
```bash
git clone git@github.com:BD-Danielle/python.git
```

2. 選擇要使用的子專案，進入相應目錄：
```bash
cd python/image_tools/duplicate_finder
```

3. 按照子專案的 README.md 進行設置和使用

## 開發規範
- 每個子專案都應該有自己的：
  - README.md
  - requirements.txt
  - 虛擬環境 (venv/)
- 使用虛擬環境進行開發
- 保持代碼風格一致性

## 貢獻指南
1. Fork 本專案
2. 創建你的特性分支
3. 提交你的改動
4. 發起 Pull Request

## 作者
[CYL]

## 授權
This project is licensed under the GNU GPL v3 License.
See [LICENSE](LICENSE) for more information.