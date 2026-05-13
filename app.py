import streamlit as st
from difflib import SequenceMatcher
from pdf2image import convert_from_path
import pytesseract
import os
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

    for pdf_file in PDF_FILES:

        try:

            pages = convert_from_path(pdf_file)

            for page in pages:

                text = pytesseract.image_to_string(page)

                combined_text += text + "\n"

        except Exception:
            pass

    return combined_text.lower()

pdf_text = load_all_pdfs()

RULES = {

    "lifts": {
        "questions": [
            "can dogs use lifts",
            "can pets use elevators"
        ],
        "response": """
Yes 😊 Pets cannot be denied access to lifts or elevators used by residents.

Housing societies cannot impose separate lift charges for pets.
"""
    },

    "ban_pets": {
        "questions": [
            "can society ban pets",
            "can rwa remove pets"
        ],
        "response": """
No 😊 RWAs and housing societies cannot legally ban pets or force residents to remove them from their homes.
"""
    }
}

def clean_text(text):

    text = re.sub(r"\\s+", " ", text)

    return text.strip()

def search_pdf_answer(question):

    paragraphs = pdf_text.split("\n")

    best_score = 0
    best_match = ""

    for para in paragraphs:

        para = clean_text(para)

        if len(para) < 80:
            continue

        score = SequenceMatcher(
            None,
            question.lower(),
            para.lower()
        ).ratio()

        keywords = question.lower().split()

        keyword_hits = 0

        for word in keywords:

            if word in para.lower():
                keyword_hits += 1

        score += keyword_hits * 0.05

        if score > best_score:

            best_score = score
            best_match = para

    if best_score > 0.15:

        return f"""
📘 Based on AWBI / Government guidelines:

{best_match}
"""

    return None

st.markdown("### Quick Questions")

quick_questions = [
    "Can dogs use lifts?",
    "Can society ban pets?",
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

    answer = None

    best_score = 0
    best_answer = None

    for topic, data in RULES.items():

        for sample in data["questions"]:

            score = SequenceMatcher(
                None,
                question.lower(),
                sample.lower()
            ).ratio()

            if score > best_score:

                best_score = score
                best_answer = data["response"]

    if best_score > 0.45:

        answer = best_answer

    else:

        answer = search_pdf_answer(question)

    if not answer:

        answer = """
I could not find an exact answer for this question 😊
"""

    st.subheader("Answer")

    st.success(answer)

    with st.expander("AWBI / Government Context"):

        st.info(
            "This assistant uses government and AWBI guidelines."
        )

st.markdown("---")

st.caption("Built for pet parents of Mangalam Ananda 🐶")
