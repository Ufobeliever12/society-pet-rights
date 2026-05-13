import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="Society Pet Rights",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 Society Pet Rights")
st.caption("Mangalam Anada • Pet Rights Assistant")

pdf_path = "163282565895pet_dog_circular_26_2_2015.pdf"

@st.cache_data
def load_pdf_text():

    pdf_reader = PdfReader(pdf_path)

    text = ""

    for page in pdf_reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text.lower()

pdf_text = load_pdf_text()

RULES = {
    "ban pets": "RWAs and societies cannot legally ban pets or restrict breeds/sizes.",

    "lifts": "Pets cannot be denied access to lifts/elevators used by residents.",

    "fine": "Societies cannot impose arbitrary fines on pet owners without legal basis.",

    "garden": "Pets should not be completely banned from common areas like gardens and parks. Residents may mutually agree on suitable timings and cleanliness practices.",

    "park": "Pets should not be completely banned from parks and common areas.",

    "street dogs": "Feeding street dogs is legal. Harassing feeders may amount to an offense.",

    "muzzle": "RWAs cannot force mandatory muzzles for all dogs.",

    "barking": "Occasional barking is natural. Pet owners should still try to minimize disturbance.",

    "poop": "Pet owners should clean up pet waste and cooperate on cleanliness."
}

st.markdown("### Quick Questions")

quick_questions = [
    "Can RWAs ban pets?",
    "Can dogs use lifts?",
    "Can societies fine pet owners?",
    "Can I play with my dog in garden area?",
    "Is feeding street dogs legal?",
    "Can RWAs force muzzles?"
]

cols = st.columns(2)

selected_question = ""

for i, q in enumerate(quick_questions):

    if cols[i % 2].button(q):
        selected_question = q

question = st.text_input(
    "Ask your question",
    value=selected_question
)

if question:

    q = question.lower()

    answer = None

    for keyword, response in RULES.items():

        if keyword in q:
            answer = response
            break

    if not answer:

        if "dog" in q and "play" in q:
            answer = RULES["garden"]

        elif "garden" in q or "park" in q:
            answer = RULES["garden"]

        elif "lift" in q or "elevator" in q:
            answer = RULES["lifts"]

        elif "feed" in q:
            answer = RULES["street dogs"]

        else:
            answer = (
                "According to AWBI guidelines, pet owners and residents "
                "should coexist peacefully while maintaining cleanliness "
                "and safety in common areas."
            )

    st.subheader("Answer")
    st.success(answer)

    with st.expander("AWBI Context"):
        st.info(
            "Animal Welfare Board of India Guidelines "
            "on Pet and Street Dogs (26 February 2015)."
        )

st.markdown("---")
st.caption("Built for pet parents of Mangalam Anada 🐶")
