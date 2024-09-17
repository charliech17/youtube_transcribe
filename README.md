# Python 下載youtube音檔，並將音訊轉成逐字稿

## 簡介
下載youtube影片為音訊檔，並將文字轉成逐字稿。


## 使用教學

### 步驟ㄧ: 下載需要的東西

#### 1. poetry
這個程式庫使用poetry管理套件，如果你還沒有安裝過，需要先下載poetry，如何下載詳見官網。
https://python-poetry.org/docs/

有poetry之後，需要執行poetry install，下載所需要的套件。

#### 2: ffmpeg
需要在電腦安裝ffmpeg(如果之前沒有安裝過的話)，並於`1_download`中的--ffmpeg-location指定他的路徑，這樣才能才能在下載後將webm格式檔案轉成wav檔案，供後續轉成逐字稿。

mac上可以直接執行以下指令安裝
```
brew install ffmpeg
```

window需要再查查看如何下載。

#### 3.  openai-whisper
如果你想用ai_transcribe.py來取得逐字稿的話，需要執行以下指令，下載whisper套件。如果你要用google_transcribe來取得逐字稿的話就不用下載這個，但是google_transcribe似乎較不準確，實驗結果發現他容易漏掉一些文字。

我自己實驗，whisper要安裝在全域才能成功，用poetry add下載會失敗。執行以下指令進行下載
```
pip install -U openai-whisper
```

### 步驟二: 執行`1_download.py` 將要產生逐字稿的影片下載，並轉成wav格式。

### 步驟三: 執行 `2_ai_transcribe` 或是 `3_google_transcribe` 來產生逐字稿。
(建議使用  `2_ai_transcribe` 測試起來比較精確。)

