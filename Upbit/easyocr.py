import easyocr

# EasyOCR Reader 초기화
reader = easyocr.Reader(['en', 'ko'])  # 영어와 한국어 지원

# 이미지 파일 경로
image_path = 'example_image.jpg'  # 분석할 이미지 경로

# 텍스트 읽기
results = reader.readtext(image_path)

# 결과 출력
for (bbox, text, confidence) in results:
    print(f"텍스트: {text}, 신뢰도: {confidence:.2f}")
