import streamlit as st
from PyPDF2 import PdfReader
from difflib import SequenceMatcher

st.set_page_config(
    page_title="Society Pet Rights",
    page_icon="🐾",
    layout="centered"
)

st.title("🐶 Mangalam Ananda Pet Rights Assistant")

st.caption(
    "Helping residents understand pet-related guidelines peacefully and clearly 😊"
)

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

    "lifts": {
        "questions": [
            "can dogs use lifts",
            "can pets use elevators",
            "can dogs travel in lift",
            "can security stop pets from using lift",
            "can society deny lift access to dogs",
            "can pets use society elevators",
            "can dogs go in elevator",
            "can pets travel in society lift"
        ],
        "response": """
Yes 😊 Residents with pets are allowed to use lifts and elevators used by other residents.

As per AWBI guidelines, housing societies cannot deny lift access to pets or impose separate lift charges for pets.

Pet owners should ensure pets are safely handled and maintain cleanliness while using common facilities.
"""
    },

    "ban_pets": {
        "questions": [
            "can society ban pets",
            "can apartment ban pets",
            "can rwa remove pets",
            "can society force us to remove dog",
            "are dogs not allowed in society",
            "can housing society ban dogs"
        ],
        "response": """
No 😊 Housing societies and RWAs cannot legally ban pets or force residents to remove pets from their homes.

Pet owners are expected to maintain hygiene, cleanliness, and safety while keeping pets in residential communities.
"""
    },

    "common_areas": {
        "questions": [
            "can dogs walk in garden",
            "can pets play in common area",
            "can i walk my dog in society",
            "can pets use common area",
            "can society stop dog walking",
            "can dogs enter common areas",
            "can pets walk in society"
        ],
        "response": """
Yes 😊 Pets are generally allowed in common areas such as pathways, gardens, and open spaces.

Residents should cooperate on cleanliness and safety, but complete bans on pet movement in common areas are generally discouraged.
"""
    },

    "feeding": {
        "questions": [
            "is feeding stray dogs legal",
            "can i feed street dogs",
            "can society stop dog feeding",
            "is feeding stray dogs allowed",
            "can residents feed stray dogs",
            "is stray feeding illegal"
        ],
        "response": """
Yes 😊 Feeding street dogs is legal in India.

Feeders should choose suitable spots and maintain cleanliness to avoid inconvenience to other residents.

AWBI guidelines encourage peaceful coexistence and humane treatment of community animals.
"""
    }
}

st.markdown("### Quick Questions")

quick_questions = [
    "Can RWAs ban pets?",
    "Can dogs use lifts?",
    "Can societies fine pet owners?",
    "Can I play with my dog in garden area?",
    "Is feeding street dogs legal?"
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
    best_score = 0
    best_answer = None

    for topic, data in RULES.items():

        for sample_question in data["questions"]:

            score = SequenceMatcher(
                None,
                q.lower(),
                sample_question.lower()
            ).ratio()

            if score > best_score:
                best_score = score
                best_answer = data["response"]

    if best_score > 0.45:
        answer = best_answer

    if not answer:

        answer = """
I could not find an exact rule for this question 😊

However, according to AWBI guidelines, pet owners and other residents should coexist peacefully while maintaining cleanliness, safety, and mutual respect.
"""

    st.subheader("Answer")
    st.success(answer)

    with st.expander("AWBI Context"):
        st.info(
            "Animal Welfare Board of India Guidelines "
            "on Pet and Street Dogs (26 February 2015)."
        )

st.markdown("---")
st.caption("Built for pet parents of Mangalam Ananda 🐶")
