import streamlit as st
import random

st.set_page_config(
    page_title="놀거리 추천 앱",
    page_icon="🎉",
)

st.title("🎉 오늘 뭐하지?")
st.write("기분에 맞는 놀거리를 추천해드려요!")

mood = st.selectbox(
    "오늘 기분은 어떤가요?",
    ["신남", "심심함", "우울함", "스트레스", "설렘"]
)

place = st.selectbox(
    "어디에서 놀고 싶나요?",
    ["집", "밖", "상관없음"]
)

recommendations = {
    "신남": [
        "친구랑 노래방 가기 🎤",
        "야식 먹으면서 영화 보기 🍿",
        "즉흥 드라이브 가기 🚗",
    ],
    "심심함": [
        "카페 가서 디저트 먹기 ☕",
        "새로운 게임 해보기 🎮",
        "산책하면서 음악 듣기 🎧",
    ],
    "우울함": [
        "따뜻한 음식 먹기 🍜",
        "힐링 영화 보기 🎬",
        "조용한 공원 산책 🌳",
    ],
    "스트레스": [
        "운동하기 💪",
        "매운 음식 먹기 🌶️",
        "혼자 드라이브 🚘",
    ],
    "설렘": [
        "예쁜 카페 가기 ✨",
        "사진 찍으러 가기 📸",
        "데이트 코스 찾아보기 💕",
    ]
}

if st.button("추천 받기"):

    result = random.choice(recommendations[mood])

    if place == "집":
        result += "\n\n🏠 집에서도 충분히 즐길 수 있어요!"
    elif place == "밖":
        result += "\n\n🌈 밖에 나가서 기분 전환해보세요!"

    st.subheader("오늘의 추천")
    st.success(result)
