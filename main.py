import streamlit as st
import pandas as pd
import numpy as np

# 웹 앱 제목
st.title("🎉 랜덤 데이터 시각화 & 축하 풍선! 🎈")

st.write("""
이 앱은 랜덤 데이터를 생성하고, 
버튼을 누르면 차트와 함께 풍선이 날아갑니다!
""")

# 랜덤 데이터 생성 함수
def generate_data(rows=20):
    data = pd.DataFrame({
        "X": np.arange(1, rows + 1),
        "Y": np.random.randint(10, 100, size=rows)
    })
    return data

# 버튼 클릭 시 데이터 생성 및 시각화
if st.button("데이터 생성 & 시각화"):
    df = generate_data()
    st.line_chart(df.set_index("X"))  # X축을 인덱스로 설정
    st.success("데이터가 성공적으로 시각화되었습니다! 🎉")
    st.balloons()  # 풍선 효과

# 데이터 확인용 테이블
if st.checkbox("생성된 데이터 보기"):
    df = generate_data()
    st.dataframe(df)
