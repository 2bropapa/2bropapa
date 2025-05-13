import streamlit as st
import sqlite3

# 간단한 인증
password = st.text_input("관리자 비밀번호", type="password")
if password != "1234":  # ⚠️ 배포 전엔 반드시 안전하게 관리하세요!
    st.warning("접근 권한이 없습니다.")
    st.stop()

# DB 연결
conn = sqlite3.connect('feedback.db', check_same_thread=False)
c = conn.cursor()

st.title("👨‍💻 고객의 소리 확인")

feedbacks = c.execute("SELECT name, message, timestamp FROM feedback ORDER BY timestamp DESC").fetchall()

for f in feedbacks:
    st.write(f"🗓️ {f[2]} | 🙋‍♂️ {f[0] if f[0] else '익명'}")
    st.info(f[1])
