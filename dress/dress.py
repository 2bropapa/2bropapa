import cv2
from PIL import Image
import pytesseract
import pandas as pd
import re

# Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 이미지에서 텍스트 추출 함수
def extract_text_from_image(image_path):
    try:
        # Pillow로 이미지 열기
        img = Image.open(image_path)
    except Exception as e:
        raise FileNotFoundError(f"이미지를 열 수 없습니다: {e}")
    
    # Tesseract OCR을 사용하여 텍스트 추출
    text = pytesseract.image_to_string(img, lang='eng')
    return text

# 텍스트에서 글자와 숫자 분리 함수
def separate_text_and_numbers(text):
    letters = re.findall(r'[a-zA-Z]+', text)  # 글자만 추출
    numbers = re.findall(r'\d+', text)        # 숫자만 추출
    return letters, numbers

# DataFrame 생성 함수
def create_dataframe(letters, numbers):
    max_length = max(len(letters), len(numbers))
    letters += [''] * (max_length - len(letters))  # 길이 맞추기
    numbers += [''] * (max_length - len(numbers))
    df = pd.DataFrame({'Letters': letters, 'Numbers': numbers})
    return df

# 메인 실행 코드
def process_image_to_dataframe(image_path):
    # 이미지에서 텍스트 추출
    extracted_text = extract_text_from_image(image_path)
    
    # 텍스트에서 글자와 숫자 분리
    letters, numbers = separate_text_and_numbers(extracted_text)
    
    # DataFrame 생성
    df = create_dataframe(letters, numbers)
    return df

# 이미지 파일 경로 지정
image_path = './test.jpg'

# 이미지 처리 및 DataFrame 생성
df = process_image_to_dataframe(image_path)
print(df)