import streamlit as st
import random

# 포켓몬 도감번호로 공식 아트워크 이미지 URL을 만드는 함수
def pokemon_image_url(dex_id: int) -> str:
    return (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        f"sprites/pokemon/other/official-artwork/{dex_id}.png"
    )

# MBTI별 추천 포켓몬 데이터 (이름, 도감번호, 설명)
mbti_pokemon = {
    "INTJ": [
        {"name": "메타그로스", "id": 376, "desc": "뛰어난 지능과 전략적 사고를 가진 강철/에스퍼 타입. 계획적이고 완벽주의적인 INTJ와 잘 어울려요."},
        {"name": "뮤츠", "id": 150, "desc": "냉철한 판단력과 압도적인 능력을 지닌 전설의 포켓몬이에요."},
    ],
    "INTP": [
        {"name": "메타몽", "id": 132, "desc": "무한한 가능성과 변화를 탐구하는 모습이 INTP의 열린 사고와 잘 맞아요."},
        {"name": "뮤", "id": 151, "desc": "호기심 가득한 신비로운 존재로, 탐구심 강한 INTP를 닮았어요."},
    ],
    "ENTJ": [
        {"name": "리자몽", "id": 6, "desc": "강한 리더십과 카리스마를 지닌 포켓몬으로 타고난 지휘관 ENTJ와 어울려요."},
        {"name": "마기라스", "id": 248, "desc": "압도적인 힘과 카리스마로 주변을 지배하는 모습이 ENTJ와 닮았어요."},
    ],
    "ENTP": [
        {"name": "저리더프", "id": 571, "desc": "재치있고 임기응변에 능한 모습이 아이디어 뱅크 ENTP와 잘 맞아요."},
        {"name": "팬텀", "id": 94, "desc": "장난기 넘치고 예측불가한 매력이 ENTP를 닮았어요."},
    ],
    "INFJ": [
        {"name": "라티아스", "id": 380, "desc": "신비롭고 통찰력 있는 에스퍼 타입으로 이상주의자 INFJ와 어울려요."},
        {"name": "무우마직", "id": 429, "desc": "깊은 내면과 신비로움을 지닌 포켓몬이에요."},
    ],
    "INFP": [
        {"name": "이브이", "id": 133, "desc": "무한한 가능성을 품은 순수한 존재로, 몽상가 INFP를 닮았어요."},
        {"name": "라프라스", "id": 131, "desc": "따뜻하고 온화한 성품이 INFP의 감수성과 잘 맞아요."},
    ],
    "ENFJ": [
        {"name": "루카리오", "id": 448, "desc": "타인을 이끌고 돕는 것을 좋아하는 리더형 포켓몬이에요."},
        {"name": "가디안", "id": 282, "desc": "우아하면서도 보호본능이 강한 모습이 ENFJ와 닮았어요."},
    ],
    "ENFP": [
        {"name": "피카츄", "id": 25, "desc": "밝고 에너지 넘치는 성격이 활발한 ENFP와 완벽하게 어울려요."},
        {"name": "부스터", "id": 136, "desc": "열정적이고 활기찬 에너지가 ENFP를 닮았어요."},
    ],
    "ISTJ": [
        {"name": "핫삼", "id": 212, "desc": "원칙을 중시하고 성실한 강철 타입 포켓몬이에요."},
        {"name": "딱구리", "id": 50, "desc": "묵묵히 자기 할 일을 해내는 성실함이 ISTJ와 잘 맞아요."},
    ],
    "ISFJ": [
        {"name": "밀로틱", "id": 350, "desc": "따뜻하고 헌신적인 성품이 수호자형 ISFJ를 닮았어요."},
        {"name": "럭키", "id": 113, "desc": "다정하고 보살핌이 많은 모습이 ISFJ와 어울려요."},
    ],
    "ESTJ": [
        {"name": "갸라도스", "id": 130, "desc": "강력한 힘과 통솔력을 지닌 포켓몬으로 관리자형 ESTJ와 어울려요."},
        {"name": "캥카", "id": 115, "desc": "책임감 있고 보호본능이 강한 모습이 ESTJ를 닮았어요."},
    ],
    "ESFJ": [
        {"name": "픽시", "id": 35, "desc": "다정하고 사교적인 매력이 사교형 ESFJ와 잘 맞아요."},
        {"name": "마임맨", "id": 122, "desc": "사람들과 어울리기 좋아하는 친근함이 ESFJ와 어울려요."},
    ],
    "ISTP": [
        {"name": "괴력몬", "id": 68, "desc": "실전적이고 손재주가 좋은 포켓몬으로 문제 해결형 ISTP와 잘 맞아요."},
        {"name": "잠만보", "id": 143, "desc": "느긋하지만 필요할 땐 강력한 힘을 내는 모습이 ISTP를 닮았어요."},
    ],
    "ISFP": [
        {"name": "글레이시아", "id": 471, "desc": "고요하고 아름다운 매력이 예술가형 ISFP와 어울려요."},
        {"name": "스이쿤", "id": 245, "desc": "자유롭고 우아하게 움직이는 모습이 ISFP를 닮았어요."},
    ],
    "ESTP": [
        {"name": "윈디", "id": 59, "desc": "활동적이고 대담한 성격이 모험가형 ESTP를 닮았어요."},
        {"name": "망나뇽", "id": 149, "desc": "역동적이고 자신감 넘치는 모습이 ESTP와 잘 맞아요."},
    ],
    "ESFP": [
        {"name": "또가스", "id": 110, "desc": "화려하고 주목받길 좋아하는 모습이 ESFP를 닮았어요."},
        {"name": "블래키", "id": 197, "desc": "밤에도 반짝이는 존재감이 매력적인 ESFP를 닮았어요."},
    ],
}

st.set_page_config(page_title="MBTI 포켓몬 추천기", page_icon="✨")

st.title("✨ MBTI 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 이미지와 함께 추천해드려요!")

mbti_list = list(mbti_pokemon.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

if st.button("포켓몬 추천받기 🎉"):
    pokemon = random.choice(mbti_pokemon[selected_mbti])
    st.subheader(f"{selected_mbti} 유형에게 추천하는 포켓몬은...")
    st.markdown(f"### 🔥 {pokemon['name']}")
    st.image(pokemon_image_url(pokemon["id"]), width=300)
    st.write(pokemon["desc"])
    st.balloons()
