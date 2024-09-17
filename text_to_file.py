from datetime import datetime

def save_text(content):
    """
    將文字內容儲存到以當前日期命名的 txt 檔案中。

    參數:
    content (str): 要儲存的文字內容
    """
    # 取得當前日期，並格式化為想要的檔名格式
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # 定義檔名，使用日期和時間當作檔名
    filename = f"{current_datetime}.txt"

    # 將文字儲存為 .txt 檔案
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"檔案已儲存為 {filename}")