import streamlit as st
import pandas as pd
import numpy as np

# 페이지 제목
st.title("간단한 Streamlit 홈페이지")
st.write("이 예제는 좌우 화면을 나누어 콘텐츠를 배치한 코드입니다.")

# 화면을 좌우로 나누기
col1, col2, col3 = st.columns(3)

# 왼쪽 화면
with col1:
    st.header("왼쪽 화면")
    
    # 사용자 입력
    name = st.text_input("이름을 입력하세요:")
    if name:
        st.write(f"안녕하세요, {name}님! 반갑습니다!")
    
    # 버튼 클릭 이벤트
    if st.button("왼쪽 버튼 클릭"):
        st.write("왼쪽 버튼을 클릭했습니다!")

# 오른쪽 화면
with col2:
    st.header("오른쪽 화면")
    
    # 데이터 시각화
    st.subheader("랜덤 데이터 시각화")
    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )
    st.line_chart(data)

    # 이미지 업로드
    st.subheader("이미지 업로드")
    uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="업로드된 이미지", use_column_width=True)
with col3:
    st.header("왼쪽 화면")
    
    # 사용자 입력
    name = st.text_input("이름을 입력하세요:")
    if name:
        st.write(f"안녕하세요, {name}님! 반갑습니다!")
    
    # 버튼 클릭 이벤트
    if st.button("왼쪽 버튼 클릭"):
        st.write("왼쪽 버튼을 클릭했습니다!")
