import streamlit as st
from PyPDF2 import PdfReader
from difflib import SequenceMatcher
import re

st.set_page_config(
    page_title="Society Pet Rights",
    page_icon="🐾",
    layout="centered"
)

st.title("🐶 Mangalam Ananda Pet Rights Assistant")

st.caption(
    "Helping residents understand pet-related guidelines peacefully and clearly 😊"
)

PDF_FILES = [
    "1.pdf",
    "2.pdf",
    "3.pdf",
    "4.pdf",
    "5.pdf",
    "6.pdf",
    "7.pdf",
    "8.pdf",
    "9.pdf",
    "10.pdf",
    "11.pdf",
    "12.pdf",
    "13.pdf"
]

@st.cache_data
def load_all_pdfs():

    combined_text = ""

    for pdf in PDF_FILES:

        try:

            reader = PdfReader(pdf)

            for page in reader.pages:

                text = page.extract_text()

                if text:
                    combined_text += text + "\n"

        except Exception:
            pass

    return combined_text

pdf_text = load_all_pdfs()

RULES = {

    "lifts": {
        "questions": [
            "can dogs use lifts",
            "can pets use elevators",
            "can dogs travel in lift",
            "can society deny lift access to dogs",
            "can pets use society elevators"
        ],
        "response": """
Yes 😊 Pets cannot be denied access to lifts or elevators used by residents.

Housing societies also cannot impose separate lift charges for pets.

Pet owners should ensure cleanliness and safe handling while using common facilities.
"""
    },

    "ban_pets": {
        "questions": [
            "can society ban pets",
            "can apartment ban pets",
            "can rwa remove pets",
            "can society force us to remove dog"
        ],
        "response": """
No 😊 Housing societies and RWAs cannot legally ban pets or force residents to remove them from their homes.

Pet owners are expected to maintain hygiene, safety, and responsible ownership.
"""
    },

    "feeding": {
        "questions": [
            "is feeding stray dogs legal",
            "can i feed street dogs",
            "can society stop dog feeding"
        ],
        "response": """
Yes 😊 Feeding street dogs is legal in India.

Feeders should maintain cleanliness and choose suitable feeding locations to avoid inconvenience to others.
"""
    }
}

def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    return text.strip()

def get_best_pdf_answer(question):

    question = question.lower()

    paragraphs = pdf_text.split("\n")

    best_score = 0
    best_paragraph = ""

    for para in paragraphs:

        para_clean = clean_text(para)

        if len(para_clean) < 80:
            continue

        score = SequenceMatcher(
            None,
            question,
            para_clean.lower()
        ).ratio()

        if question in para_clean.lower():
            score += 0.5

        if score > best_score:
            best_score = score
            best_paragraph = para_clean

    if best_score > 0.18:

        return f"""
📘 Based on AWBI / Government guidelines:

{best_paragraph}
"""

    return None

st.markdown("### Quick Questions")

quick_questions = [
    "Can RWAs ban pets?",
    "Can dogs use lifts?",
    "Is feeding street dogs legal?",
    "Can society fine pet owners?",
    "If a pet dog bites someone, who is responsible?"
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
                q,
                sample_question.lower()
            ).ratio()

            if score > best_score:

                best_score = score
                best_answer = data["response"]

    if best_score > 0.45:

        answer = best_answer

    else:

        pdf_answer = get_best_pdf_answer(question)

        if pdf_answer:

            answer = pdf_answer

    if not answer:

        answer = """
I could not find an exact answer for this question 😊

Please consult your local municipal authority, AWBI guidelines, or a legal expert for issue-specific clarification.
"""

    st.subheader("Answer")

    st.success(answer)

    with st.expander("AWBI / Government Context"):

        st.info(
            "This assistant uses AWBI circulars, government guidelines, and animal welfare documents for informational purposes."
        )

st.markdown("---")

st.caption("Built for pet parents of Mangalam Ananda 🐶")
