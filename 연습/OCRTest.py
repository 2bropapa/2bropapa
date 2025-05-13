import pytesseract

# Tesseract 경로 지정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 나머지 코드
from PIL import Image

image_path = 'test3.jpg'  # OCR을 실행할 이미지 파일 경로
img = Image.open(image_path)

# Tesseract를 사용하여 이미지에서 텍스트 추출
text = pytesseract.image_to_string(img)

# 추출된 텍스트 출력
print("추출된 텍스트:")
print(text)