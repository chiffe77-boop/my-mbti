import streamlit as st
import random

mbti_pokemon = {
    "INTJ": [
        {"name": "메타그로스", "desc": "뛰어난 지능과 전략적 사고를 가진 강철/에스퍼 타입. 계획적이고 완벽주의적인 INTJ와 잘 어울려요."},
        {"name": "자바크로스", "desc": "냉철하고 강력한 힘을 지닌 포켓몬으로, 독립적인 INTJ의 성향을 닮았어요."},
    ],
    "INTP": [
        {"name": "누리레온", "desc": "지적 호기심이 많고 이론을 탐구하는 성향이 INTP와 닮았어요."},
        {"name": "메타몽", "desc": "무한한 가능성과 변화를 탐구하는 모습이 INTP의 열린 사고와 잘 맞아요."},
    ],
    "ENTJ": [
        {"name": "리자몽", "desc": "강한 리더십과 카리스마를 지닌 포켓몬으로 타고난 지휘관 ENTJ와 어울려요."},
        {"name": "펄기아", "desc": "압도적인 존재감과 지배력을 가진 전설의 포켓몬이에요."},
    ],
    "ENTP": [
        {"name": "장크로다일", "desc": "재치있고 도전적인 성격이 아이디어 뱅크 ENTP와 잘 맞아요."},
        {"name": "저리더프", "desc": "창의적이고 예측불가한 매력이 ENTP를 닮았어요."},
    ],
    "INFJ": [
        {"name": "라티아스", "desc": "신비롭고 통찰력 있는 에스퍼 타입으로 이상주의자 INFJ와 어울려요."},
        {"name": "무우마직", "desc": "깊은 내면과 신비로움을 지닌 포켓몬이에요."},
    ],
    "INFP": [
        {"name": "이브이", "desc": "무한한 가능성을 품은 순수한 존재로, 몽상가 INFP를 닮았어요."},
        {"name": "라프라스", "desc": "따뜻하고 온화한 성품이 INFP의 감수성과 잘 맞아요."},
    ],
    "ENFJ": [
        {"name": "루카리오", "desc": "타인을 이끌고 돕는 것을 좋아하는 리더형 포켓몬이에요."},
        {"name": "가디안", "desc": "우아하면서도 보호본능이 강한 모습이 ENFJ와 닮았어요."},
    ],
    "ENFP": [
        {"name": "피카츄", "desc": "밝고 에너지 넘치는 성격이 활발한 ENFP와 완벽하게 어울려요."},
        {"name": "부스터", "desc": "열정적이고 활기찬 에너지가 ENFP를 닮았어요."},
    ],
    "ISTJ": [
        {"name": "핫삼", "desc": "원칙을 중시하고 성실한 강철 타입 포켓몬이에요."},
        {"name": "딱구리", "desc": "묵묵히 자기 할 일을 해내는 성실함이 ISTJ와 잘 맞아요."},
    ],
    "ISFJ": [
        {"name": "밀로틱", "desc": "따뜻하고 헌신적인 성품이 수호자형 ISFJ를 닮았어요."},
        {"name": "치라챠무", "desc": "다정하고 보살핌이 많은 모습이 ISFJ와 어울려요."},
    ],
    "ESTJ": [
        {"name": "갸라도스", "desc": "강력한 힘과 통솔력을 지닌 포켓몬으로 관리자형 ESTJ와 어울려요."},
        {"name": "번치코", "desc": "체계적이고 조직적인 힘이 ESTJ를 닮았어요."},
    ],
    "ESFJ": [
        {"name": "픽시", "desc": "다정하고 사교적인 매력이 사교형 ESFJ와 잘 맞아요."},
        {"name": "마임맨", "desc": "사람들과 어울리기 좋아하는 친근함이 ESFJ를 닮았어요."},
    ],
    "ISTP": [
        {"name": "다크라이", "desc": "조용하지만 강력한 힘을 숨긴 모습이 ISTP와 닮았어요."},
        {"name": "괴력몬", "desc": "실전적이고 손재주가 좋은 포켓몬이에요."},
    ],
    "ISFP": [
        {"name": "덩쿠리", "desc": "자연과 조화를 이루는 예술가적 감성이 ISFP를 닮았어요."},
        {"name": "글레이시아", "desc": "고요하고 아름다운 매력이 ISFP와 어울려요."},
    ],
    "ESTP": [
        {"name": "윈디", "desc": "활동적이고 대담한 성격이 모험가형 ESTP를 닮았어요."},
        {"name": "부스터", "desc": "즉흥적이고 열정적인 에너지가 ESTP와 잘 맞아요."},
    ],
    "ESFP": [
        {"name": "또가스", "desc": "화려하고 주목받길 좋아하는 모습이 ESFP를 닮았어요."},
        {"name": "블래키", "desc": "자유분방하고 매력적인 존재감이 ESFP와 어울려요."},
    ],
}

st.set_page_config(page_title="MBTI 포켓몬 추천기", page_icon="✨")

st.title("✨ MBTI 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 추천해드려요!")

mbti_list = list(mbti_pokemon.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

if st.button("포켓몬 추천받기 🎉"):
    pokemon = random.choice(mbti_pokemon[selected_mbti])
    st.subheader(f"{selected_mbti} 유형에게 추천하는 포켓몬은...")
    st.markdown(f"### 🔥 {pokemon['name']}")
    st.write(pokemon["desc"])
    st.balloons()
