import streamlit as st
import random

st.set_page_config(
    page_title="AI 고민상담소",
    page_icon="💭",
)

st.title("💭 AI 고민상담소")
st.write("편하게 고민을 입력해보세요.")

user_input = st.text_area(
    "고민 입력",
    placeholder="예: 요즘 인간관계 때문에 너무 힘들어요..."
)

responses = [
    "지금 많이 지쳐있는 것 같아요. 너무 혼자 버티려고 하지 마세요.",
    "당장 모든 걸 해결하지 않아도 괜찮아요. 천천히 하나씩 정리해보세요.",
    "스스로를 너무 몰아붙이지 않았으면 좋겠어요.",
    "지금의 감정도 충분히 의미가 있어요.",
    "가끔은 쉬어가는 것도 정말 중요합니다.",
    "당신의 마음을 먼저 돌보는 시간이 필요할 수 있어요.",
]

def get_advice(text):
    text = text.lower()

    if "공부" in text:
        return "결과보다 꾸준함이 더 중요할 때가 많아요."

    elif "연애" in text:
        return "상대의 마음보다 자신의 감정을 먼저 살펴보세요."

    elif "친구" in text:
        return "모든 인간관계를 완벽하게 유지할 필요는 없어요."

    elif "가족" in text:
        return "가까운 관계일수록 대화와 이해가 중요합니다."

    elif "회사" in text or "직장" in text:
        return "일도 중요하지만 건강과 감정도 꼭 챙겨야 해요."

    else:
        return random.choice(responses)

if st.button("상담 받기"):
    if user_input.strip() == "":
        st.warning("고민을 입력해주세요.")
    else:
        answer = get_advice(user_input)

        st.subheader("🫶 상담 결과")
        st.success(answer)
