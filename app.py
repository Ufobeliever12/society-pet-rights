
import streamlit as st

st.set_page_config(
    page_title="Society Pet Rights",
    page_icon="🐾",
    layout="centered"
)

RULES = {
    "ban pets": "RWAs and apartment associations cannot legally ban pets, restrict dog sizes, or force residents to abandon pets.",
    "lifts": "Pets cannot be denied access to lifts/elevators. Associations also cannot impose charges for lift usage.",
    "fine pet owners": "Associations cannot impose arbitrary fines or special charges on pet owners without legal authority.",
    "parks": "Pets should not be completely banned from parks. Communities may mutually agree on suitable timings.",
    "street dogs": "Feeding street dogs is legal. Harassing or intimidating feeders may amount to an offense.",
    "muzzle": "RWAs cannot insist on mandatory muzzles for all dogs.",
    "barking": "Occasional barking is natural. Pet owners should however try to minimize disturbance during night hours.",
    "poop": "Pet owners are encouraged to clean pet waste and cooperate on cleanliness solutions."
}

def get_answer(question):
    q = question.lower()

    for key, value in RULES.items():
        if key in q:
            return value

    return (
        "According to the AWBI guidelines, pet owners and residents should "
        "coexist peacefully. Please ask a more specific question about bans, "
        "lifts, parks, fines, barking, feeding street dogs, or pet rights."
    )

st.title("🐾 Society Pet Rights")
st.caption("Mangalam Anada • Pet Rights Assistant")

st.markdown("---")

st.subheader("Quick Questions")

cols = st.columns(2)

quick_questions = [
    "Can RWAs ban pets?",
    "Can dogs use lifts?",
    "Can societies fine pet owners?",
    "Can pets enter parks?",
    "Is feeding street dogs legal?",
    "Can RWAs force muzzles?"
]

selected_question = None

for i, q in enumerate(quick_questions):
    if cols[i % 2].button(q):
        selected_question = q

st.markdown("---")

question = st.text_input(
    "Ask your question",
    value=selected_question if selected_question else ""
)

if question:
    answer = get_answer(question)

    st.subheader("Answer")
    st.success(answer)

    st.markdown("### Source")
    st.info(
        "Animal Welfare Board of India (AWBI) Guidelines on Pet & Street Dogs "
        "(26 February 2015)."
    )

st.markdown("---")
st.caption("Built for pet parents of Mangalam Anada 🐶")
