import streamlit as st

st.title("🔮 미래 예측 설문조사")

st.write("""
다섯 가지 질문에 답하면 당신에게 어울리는 미래를 추천해드립니다!
""")

# 질문과 선택지
questions = [
    "1. 새로운 기술을 배우는 것을 좋아하나요?",
    "2. 사람들과 협력하는 것을 좋아하나요?",
    "3. 문제를 논리적으로 해결하는 편인가요?",
    "4. 창의적인 아이디어를 내는 것을 즐기나요?",
    "5. 모험을 즐기는 편인가요?"
]

# 선택지 점수
options = {
    "전혀 아니다": 0,
    "약간 그렇다": 1,
    "그렇다": 2,
    "매우 그렇다": 3
}

# 사용자 응답 저장
scores = []
for q in questions:
    choice = st.radio(q, options.keys(), key=q)
    scores.append(options[choice])

# 결과 계산
if st.button("결과 보기 🔮"):
    total_score = sum(scores)
    
    # 미래 추천
    if total_score <= 4:
        st.subheader("당신은 안정적이고 계획적인 삶을 선호하는 타입입니다.")
        st.write("추천 미래: 연구원, 분석가, 데이터 전문가")
    elif total_score <= 8:
        st.subheader("당신은 균형 잡힌 타입입니다.")
        st.write("추천 미래: 프로젝트 매니저, 엔지니어, 디자이너")
    elif total_score <= 12:
        st.subheader("당신은 창의적이고 도전적인 타입입니다.")
        st.write("추천 미래: 스타트업 창업, 발명가, 콘텐츠 크리에이터")
    else:
        st.subheader("당신은 모험과 혁신을 즐기는 타입입니다!")
        st.write("추천 미래: 탐험가, 혁신가, 미래 기술 개발자")
    
    st.balloons()



