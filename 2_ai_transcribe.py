import whisper

audio_file = input('請輸入要產生逐字稿的檔案名稱(包含副檔名):\n')

model = whisper.load_model("base")  # 可选模型：tiny, base, small, medium, large

result = model.transcribe('TED_TALK.wav', language='en')

print("\nThe resultant text from video is: \n")
print(result['text'])