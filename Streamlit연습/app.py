import streamlit as st
import sqlite3

# SQLite 데이터베이스 연결 (여기선 DB 파일을 메모리에만 유지)
conn = sqlite3.connect('feedback.db')
c = conn.cursor()

# 테이블이 없다면 테이블 생성
c.execute('''CREATE TABLE IF NOT EXISTS feedback (name TEXT, message TEXT)''')

# 페이지 제목
st.title("개발자에게 바라는 점")

# 화면 나누기 (운동 종류는 왼쪽, 피드백은 오른쪽)
col1, col2 = st.columns([3, 1])

# col1: 운동의 종류 섹션
with col1:
    st.header("🏋️‍♂️ 운동의 종류")
    
    # 이름 입력란 추가 (운동 섹션과 함께)
    name = st.text_input("이름을 입력해주세요.", "")

    st.subheader("1. 데드리프트 (Deadlift)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Deadlift_sumo_variation.jpg/220px-Deadlift_sumo_variation.jpg", width=300)
    st.write("데드리프트는 전신을 사용하여 힘을 기를 수 있는 운동으로, 특히 하체와 허리를 강화하는 데 효과적입니다.")
    
    st.subheader("2. 벤치 프레스 (Bench Press)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Bench_press_aka.jpg/220px-Bench_press_aka.jpg", width=300)
    st.write("벤치 프레스는 가슴과 어깨 근육을 강화하는 운동으로, 상체 힘을 기르는 데 매우 중요한 운동입니다.")
    
    st.subheader("3. 스쿼트 (Squat)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Squat_%28PSF%29.jpg/220px-Squat_%28PSF%29.jpg", width=300)
    st.write("스쿼트는 하체와 코어 근육을 강화하는 운동으로, 체중을 지탱하는 데 필수적인 운동입니다.")
    
    # 추가적인 운동 소개 또는 더 많은 내용 등을 추가할 수 있음
    st.write("이 외에도 다양한 운동들이 있습니다. 나만의 운동 루틴을 찾아보세요!")

# col2: 개발자에게 바라는 점 섹션
with col2:
    st.header("💬 개발자에게 바라는 점")
    
    # 실명 여부 체크박스
    real_name = st.checkbox("실명으로 제출하기")
    
    # 실명 체크박스를 체크한 경우 이름 입력란 숨기기
    if real_name:
        name = "실명 제출"  # 실명 체크 시 이름은 따로 받지 않음
    else:
        # 익명 체크박스 해제 시 이름 입력란 표시
        name = st.text_input("이름 (익명으로 제출할 경우 입력 안 해도 됩니다.)", "익명")  # 기본값을 "익명"으로 설정

    # 개발자에게 바라는 점 내용 받기
    message = st.text_area("개발자에게 바라는 점을 작성해주세요.", key="message")
    
    # 제출 버튼
    if st.button("제출하기"):
        if message.strip() == "":
            st.warning("내용을 작성해주세요.")
        else:
            # 데이터베이스에 저장
            c.execute("INSERT INTO feedback (name, message) VALUES (?, ?)", (name, message))
            conn.commit()
            # 성공 메시지 표시
            st.success("바라는 점이 성공적으로 제출되었습니다!")

# 데이터베이스에 저장된 내용 표시 (디버그용)
with st.expander("제출된 피드백 보기"):
    c.execute("SELECT * FROM feedback")
    rows = c.fetchall()
    for row in rows:
        st.write(f"**{row[0]}**: {row[1]}")
