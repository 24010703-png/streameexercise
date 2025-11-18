import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("⚡ 포물선 운동 시뮬레이터")

st.write("""
발사 각도와 초기 속도를 조절해 공이 날아가는 궤적을 시각화해보세요!
""")

# 입력값
angle = st.slider("발사 각도 (도)", 0, 90, 45)
speed = st.slider("초기 속도 (m/s)", 1, 50, 20)

# 중력 가속도
g = 9.8

# 시간 계산
angle_rad = np.radians(angle)
t_flight = 2 * speed * np.sin(angle_rad) / g
t = np.linspace(0, t_flight, num=100)

# 포물선 좌표 계산
x = speed * np.cos(angle_rad) * t
y = speed * np.sin(angle_rad) * t - 0.5 * g * t**2

# 그래프 출력
fig, ax = plt.subplots()
ax.plot(x, y, label=f"{angle}도, {speed} m/s")
ax.set_xlabel("거리 (m)")
ax.set_ylabel("높이 (m)")
ax.set_title("포물선 운동")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# 풍선 효과
if st.button("성공! 🎈"):
    st.balloons()
    st.success("포물선 운동 시뮬레이션 완료!")

