# -*- coding: utf-8 -*-

# 필요한 라이브러리 임포트
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 간단한 데이터 생성 (예: 공부 시간 vs 시험 점수)
data = {
    '공부시간': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    '시험점수': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)

# X(특징)와 Y(목표 변수) 나누기
X = df[['공부시간']]  # 공부시간은 특징(features)
y = df['시험점수']    # 시험점수는 목표 변수(target)

# 데이터 분리 (훈련 데이터 80%, 테스트 데이터 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 선형 회귀 모델 만들기
model = LinearRegression()

# 모델 훈련
model.fit(X_train, y_train)

# 예측하기
y_pred = model.predict(X_test)

# 예측 결과 시각화
plt.scatter(X_test, y_test, color='blue', label='실제값')
plt.plot(X_test, y_pred, color='red', label='예측값')
plt.title('선형 회귀 예측 결과')
plt.xlabel('공부시간')
plt.ylabel('시험점수')
plt.legend()
plt.show()

# 모델 평가 (MSE, Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
