import streamlit as st

st.set_page_config(
    page_title="연애 코칭 앱",
    page_icon="💕",
)

st.title("💕 AI 연애 코칭")
st.write("연애 고민을 입력하면 조언을 해드립니다.")

user_input = st.text_area(
    "고민을 입력하세요",
    placeholder="예: 썸남이 답장이 너무 느려요..."
)

def love_coach_response(text):
    text = text.lower()

    if "답장" in text:
        return "상대의 답장 속도만으로 마음을 단정하지 마세요. 중요한 건 대화의 진정성과 꾸준함입니다."

    elif "헤어" in text:
        return "헤어짐은 힘들지만, 자신을 먼저 돌보는 시간이 꼭 필요합니다."

    elif "고백" in text:
        return "고백은 완벽한 타이밍보다 솔직한 마음이 더 중요할 수 있어요."

    elif "썸" in text:
        return "썸 단계에서는 너무 조급해하지 말고 자연스럽게 관계를 이어가 보세요."

    else:
        return "상대보다 자신의 감정과 행복을 먼저 챙기는 것이 건강한 연애의 시작입니다."

if st.button("조언 받기"):
    if user_input.strip() == "":
        st.warning("고민을 입력해주세요.")
    else:
        result = love_coach_response(user_input)
        st.success(result)
