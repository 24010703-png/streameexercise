import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🎯 대포 발사 포물선 시뮬레이터")

# --- Sidebar Controls ---
st.sidebar.header("🔧 조작 메뉴")
angle = st.sidebar.slider("발사 각도 (degrees)", 0, 90, 45)
speed = st.sidebar.slider("발사 속도 (m/s)", 1, 100, 40)
target_x = st.sidebar.slider("목표물 x 위치 (m)", 10, 200, 80)
g = 9.8  # 중력가속도

# --- Physics ---
theta = np.radians(angle)
v0x = speed * np.cos(theta)
v0y = speed * np.sin(theta)

# 최대 도달 시간
t_flight = (v0y + np.sqrt(v0y**2 + 2 * g * 0)) / g * 2
t = np.linspace(0, t_flight, 300)

# 궤적 계산
x = v0x * t
y = v0y * t - 0.5 * g * t**2
y = np.maximum(y, 0)

# --- Plot ---
fig, ax = plt.subplots()
ax.plot(x, y, label="포탄 궤적")

# 목표물 표시
ax.scatter([target_x], [0], color="red", s=100, label="🎯 목표물")

ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("포물선 대포 발사 궤적")
ax.legend()

st.pyplot(fig)

# --- Hit detection ---
# 목표물 크기 범위
target_width = 2.0
hit = np.any((x > target_x - target_width) & (x < target_x + target_width) & (y < 1))

if hit:
    st.success("🎉 명중 성공!")
else:
    st.error("💥 명중 실패! 각도와 속도를 조절하세요.")
