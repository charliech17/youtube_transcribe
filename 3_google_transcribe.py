import speech_recognition as sr

audio_file = input('請輸入要產生逐字稿的檔案名稱(包含副檔名)')
# audio_file = 'TED_TALK.wav'  # 替换为您的音频文件名
r = sr.Recognizer()



with sr.AudioFile(audio_file) as source:
    total_duration = source.DURATION  # 获取音频总时长

offset = 0  # 起始偏移时间（秒）
increment = 50  # 每个片段的时长（秒），建议小于60秒

texts = []

while offset < total_duration:
    with sr.AudioFile(audio_file) as source:
        # 设置偏移和时长，读取音频片段
        audio_data = r.record(source, offset=offset, duration=increment)
    try:
        # 调用 Google Speech Recognition API
        text = r.recognize_google(audio_data, language='en-US')
        texts.append(text)
        print(f"Processed segment from {offset} to {offset + increment} seconds")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    # 更新偏移时间
    offset += increment

# 合并所有文本
full_text = '\n\t  '.join(texts)
print("\nThe resultant text from video is: \n")
print(full_text)
