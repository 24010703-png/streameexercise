import streamlit as st
import pandas as pd
import numpy as np

st.title("⚡ 포물선 운동 시뮬레이터 (Matplotlib 없이)")

st.write("""
발사 각도와 초기 속도를 조절해서 포물선 운동을 관찰해보세요!
""")

# 사용자 입력
angle = st.slider("발사 각도 (도)", 0, 90, 45)
speed = st.slider("초기 속도 (m/s)", 1, 50, 20)

# 중력
g = 9.8
angle_rad = np.radians(angle)

# 시간 계산
t_flight = 2 * speed * np.sin(angle_rad) / g
t = np.linspace(0, t_flight, 100)

# 포물선 좌표 계산
x = speed * np.cos(angle_rad) * t
y = speed * np.sin(angle_rad) * t - 0.5 * g * t**2

# 데이터프레임 생성
data = pd.DataFrame({
    "거리 (m)": x,
    "높이 (m)": y
})

# 차트 시각화 (Streamlit 내장)
st.line_chart(data.set_index("거리 (m)"))

# 풍선 버튼
if st.button("성공! 🎈"):
    st.balloons()
    st.success("포물선 운동 시뮬레이션 완료!")


