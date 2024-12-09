import os
from PIL import Image
from PIL.ExifTags import TAGS
import datetime
import shutil
try:
    import imagehash
except ImportError:
    print("請先安裝 imagehash 模組：")
    print("pip install imagehash")
    exit(1)


def get_image_date(image_path):
    """獲取圖片的拍攝日期或檔案創建日期"""
    try:
        # 嘗試從EXIF獲取拍攝日期
        with Image.open(image_path) as img:
            exif = img._getexif()
            if exif:
                for tag_id in exif:
                    tag = TAGS.get(tag_id, tag_id)
                    if tag == 'DateTimeOriginal':
                        date_str = exif[tag_id]
                        return datetime.datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
    except Exception:
        pass

    # 如果無法從EXIF獲取，使用檔案創建時間
    try:
        # 獲取檔案的創建時間和修改時間
        ctime = os.path.getctime(image_path)
        mtime = os.path.getmtime(image_path)
        # 使用較早的時間
        file_time = min(ctime, mtime)
        return datetime.datetime.fromtimestamp(file_time)
    except Exception:
        # 如果都失敗了，返回當前時間
        return datetime.datetime.now()


def generate_new_filename(original_path, date):
    """生成新的檔案名稱"""
    # 獲取原始檔案的副檔名
    ext = os.path.splitext(original_path)[1].lower()
    # 生成新的檔案名（日期_序號）
    base_name = date.strftime('%Y%m%d_%H%M%S')
    directory = os.path.dirname(original_path)
    
    # 處理同一時間的多個檔案
    counter = 1
    new_path = os.path.join(directory, f"{base_name}{ext}")
    while os.path.exists(new_path):
        new_path = os.path.join(directory, f"{base_name}_{counter}{ext}")
        counter += 1
    
    return new_path


def rename_file(old_path):
    """重命名檔案"""
    try:
        # 獲取圖片日期
        date = get_image_date(old_path)
        # 生成新檔案名
        new_path = generate_new_filename(old_path, date)
        # 重命名檔案
        shutil.move(old_path, new_path)
        return new_path
    except Exception as e:
        print(f"重命名檔案 {old_path} 時發生錯誤：{e}")
        return old_path


def delete_file(file_path):
    """安全地刪除檔案"""
    try:
        os.remove(file_path)
        return True
    except Exception as e:
        print(f"刪除檔案 {file_path} 時發生錯誤：{e}")
        return False


def find_duplicate_images(folder_path):
    # 檢查資料夾是否存在
    if not os.path.exists(folder_path):
        print(f"錯誤：資料夾 '{folder_path}' 不存在")
        return []

    print("正在重命名檔案...")
    
    # 用於存儲圖片哈希值的字典
    hash_dict = {}
    duplicates = []

    # 遍歷資料夾中的所有文件
    for root, _, files in os.walk(folder_path):
        for file in files:
            # 確保只處理圖片格式文件
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                file_path = os.path.join(root, file)

                try:
                    # 先重命名檔案
                    new_path = rename_file(file_path)
                    
                    # 計算圖片的感知哈希值
                    img = Image.open(new_path)
                    img_hash = imagehash.phash(img)

                    # 如果哈希值已存在於字典中，記錄為重複
                    if img_hash in hash_dict:
                        duplicates.append((hash_dict[img_hash], new_path))
                    else:
                        hash_dict[img_hash] = new_path
                except Exception as e:
                    print(f"處理文件 {file_path} 時發生錯誤：{e}")

    return duplicates


def handle_duplicates(duplicates):
    """處理重複檔案"""
    if not duplicates:
        print("\n未發現重複圖片。")
        return

    print("\n找到以下重複圖片：")
    for i, (original, duplicate) in enumerate(duplicates, 1):
        print(f"\n組別 {i}:")
        print(f"原始檔案: {original}")
        print(f"重複檔案: {duplicate}")
        print("-" * 50)

    while True:
        choice = input("\n是否要刪除所有重複檔案？(y/n): ").strip().lower()
        if choice in ['y', 'n']:
            break
        print("請輸入 'y' 或 'n'")

    if choice == 'y':
        deleted_count = 0
        for original, duplicate in duplicates:
            if delete_file(duplicate):
                deleted_count += 1
                print(f"已刪除: {duplicate}")
        
        print(f"\n完成！共刪除了 {deleted_count} 個重複檔案。")
    else:
        print("\n操作已取消，未刪除任何檔案。")


if __name__ == "__main__":
    # 讓使用者輸入資料夾路徑
    folder = input("請輸入要檢查的圖片資料夾路徑：").strip()
    
    print("正在搜尋重複圖片...")
    duplicates = find_duplicate_images(folder)
    
    handle_duplicates(duplicates)
