import streamlit as st
import pandas as pd
import numpy as np

# 웹 앱의 제목 설정
st.title("간단한 Streamlit 데이터 시각화 예제")

st.write("""
이 앱은 사용자가 입력한 숫자를 기반으로 랜덤 데이터를 생성하고 
선 차트(Line Chart)를 그립니다.
""")

# 사이드바에 사용자 입력 위젯 추가
st.sidebar.header("설정")
data_points = st.sidebar.slider("데이터 포인트 수 선택", min_value=10, max_value=100, value=20, step=10)

# 데이터 생성
chart_data = pd.DataFrame(
    np.random.randn(data_points, 3), # 랜덤 데이터 생성
    columns=['a', 'b', 'c']
)

# 데이터프레임 표시
st.subheader("랜덤 데이터 (DataFrame)")
st.dataframe(chart_data)

# 선 차트 시각화
st.subheader("선 차트 (Line Chart)")
st.line_chart(chart_data)

# 버튼 추가 및 풍선 효과
if st.button("풍선 날리기! 🎈"):
    st.balloons()
    st.success("데이터 시각화 완료!")
