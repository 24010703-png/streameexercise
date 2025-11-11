
import streamlit as st
import random

st.title("⚽ 스트림릿 축구 게임 ⚽")

st.write("슛을 시도해서 골을 넣어보세요!")

# 사용자 이름 입력
player_name = st.text_input("플레이어 이름을 입력하세요:")

# 난이도 선택
difficulty = st.selectbox("난이도를 선택하세요:", ["쉬움", "보통", "어려움"])

# 난이도에 따라 골 성공 확률 설정
if difficulty == "쉬움":
    goal_chance = 0.8
elif difficulty == "보통":
    goal_chance = 0.5
else:
    goal_chance = 0.3

# 슛 버튼
if st.button("슛!"):
    if not player_name:
        st.warning("이름을 먼저 입력해주세요!")
    else:
        st.write(f"{player_name}님이 슛을 시도합니다...")
        st.progress(50)  # 간단한 연출
        if random.random() < goal_chance:
            st.success("🎉 골! 대단해요!")
        else:
            st.error("❌ 아쉽네요, 골 실패!")

# 점수판
if 'score' not in st.session_state:
    st.session_state.score = 0

if st.button("점수 추가"):
    st.session_state.score += 1

st.write(f"현재 점수: {st.session_state.score}")
