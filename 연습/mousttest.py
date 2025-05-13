import pytesseract
import pyautogui
import mss
import time
import threading
import tkinter as tk
from tkinter import messagebox
from PIL import Image

# Tesseract 경로 지정 (필요시)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR 자동화 프로그램")
        self.root.geometry("300x150")

        # 상태 변수
        self.running = False

        # 실행 버튼
        self.start_button = tk.Button(root, text="실행", command=self.start, width=20)
        self.start_button.pack(pady=20)

        # 종료 버튼
        self.stop_button = tk.Button(root, text="종료", command=self.stop, width=20)
        self.stop_button.pack(pady=5)

    def capture_screen(self):
        # 화면 캡처
        with mss.mss() as sct:
            screenshot = sct.grab(sct.monitors[1])
            img = Image.frombytes('RGB', (screenshot.width, screenshot.height), screenshot.rgb)
            return img

    def find_text_and_click(self):
        while self.running:
            # 화면 캡처
            img = self.capture_screen()

            # 이미지에서 텍스트 추출
            text = pytesseract.image_to_string(img)

            # "NEXT"가 텍스트에 포함되어 있는지 확인
            if "NEXT" in text:
                print("Found 'NEXT' in the text!")

                # 이미지에서 문자 위치 추출
                boxes = pytesseract.image_to_boxes(img)
                for b in boxes.splitlines():
                    b = b.split()
                    char = b[0]
                    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

                    # "NEXT" 텍스트의 위치 찾기
                    if char in "NEXT":
                        print(f"Character '{char}' found at: ({x}, {y})")

                # 클릭할 위치 설정 (예시로 화면 중앙)
                width, height = img.size
                click_x = width // 2  # 화면 중앙 클릭 (예시로)
                click_y = height // 2

                # 마우스 클릭
                pyautogui.click(click_x, click_y)
                print(f"Clicked at position: ({click_x}, {click_y})")

            time.sleep(10)  # 10초마다 화면 캡처

    def start(self):
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)  # 실행 버튼 비활성화
            self.stop_button.config(state=tk.NORMAL)  # 종료 버튼 활성화

            # OCR 모니터링을 별도의 스레드에서 실행
            self.thread = threading.Thread(target=self.find_text_and_click)
            self.thread.daemon = True
            self.thread.start()
            print("프로그램 실행 중...")

    def stop(self):
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)  # 실행 버튼 활성화
            self.stop_button.config(state=tk.DISABLED)  # 종료 버튼 비활성화
            print("프로그램 종료")

            # 스레드 종료 대기
            self.thread.join()

# GUI 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()
