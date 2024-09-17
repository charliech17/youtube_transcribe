import whisper
import text_to_file
import warnings

audio_file = input('請輸入要產生逐字稿的檔案名稱(包含副檔名):\n')
print('需要一些時間....')
# 忽略UserWarning
warnings.filterwarnings("ignore", message=".*It is possible to construct malicious pickle data.*")
warnings.filterwarnings("ignore", message=".*FP16 is not supported on CPU.*")


model = whisper.load_model("base")  # 可选模型：tiny, base, small, medium, large

result = model.transcribe(audio_file, language='en')

text_to_file.save_text(result['text'])