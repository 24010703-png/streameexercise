# 파일명: app.py
import streamlit as st

# 제목
st.title("간단한 스트림릿 예제")

# 입력
number = st.number_input("숫자를 입력하세요", value=0)

# 버튼
if st.button("제곱 계산"):
    result = number ** 2
    st.write(f"{number}의 제곱은 {result}입니다.")

