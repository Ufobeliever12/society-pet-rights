import streamlit as st
from docx import Document
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

st.set_page_config(
    page_title="Society Pet Rights",
    page_icon="🐾",
    layout="centered"
)

st.title("🐶 Mangalam Ananda Pet Rights Assistant")

st.caption(
    "Helping residents understand pet-related guidelines peacefully and clearly 😊"
)

DOCX_FILES = [
    "1.docx",
    "2.docx",
    "3.docx",
    "4.docx",
    "5.docx",
    "6.docx",
    "7.docx",
    "8.docx",
    "9.docx",
    "10.docx",
    "11.docx",
    "12.docx",
    "13.docx"
]

RULES = {

    "lifts": {
        "questions": [
            "can dogs use lifts",
            "can pets use elevators",
            "can security stop dogs from lift"
        ],
        "response": """
Yes 😊 Pets cannot be denied access to lifts or elevators used by residents.

Housing societies also cannot impose separate lift charges for pets.
"""
    },

    "dog_bite": {
        "questions": [
            "if a pet dog bites someone who is responsible",
            "dog bite responsibility",
            "pet dog attacks resident"
        ],
        "response": """
Pet owners are generally expected to ensure their pets are safely handled, vaccinated, socialized, and do not pose danger to others 😊

AWBI guidelines promote responsible pet ownership, behaviour management, and dog bite prevention.
"""
    }
}

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

@st.cache_data
def load_documents():

    paragraphs = []

    for file in DOCX_FILES:

        try:

            doc = Document(file)

            for para in doc.paragraphs:

                text = para.text.strip()

                if len(text) > 80:
                    paragraphs.append(text)

        except:
            pass

    return paragraphs

document_paragraphs = load_documents()

@st.cache_resource
def create_embeddings():

    embeddings = model.encode(document_paragraphs)

    return embeddings

document_embeddings = create_embeddings()

def semantic_search(question):

    question_embedding = model.encode([question])

    similarities = cosine_similarity(
        question_embedding,
        document_embeddings
    )[0]

    best_index = np.argmax(similarities)

    best_score = similarities[best_index]

    if best_score > 0.35:

        return f"""
📘 Based on AWBI / Government guidelines:

{document_paragraphs[best_index]}
"""

    return None

st.markdown("### Quick Questions")

quick_questions = [
    "Can dogs use lifts?",
    "If a pet dog bites someone, who is responsible?",
    "Can pets enter clubhouse area?",
    "Can society stop feeding stray dogs?"
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

    # FAQ MATCH FIRST
    for topic, data in RULES.items():

        for sample in data["questions"]:

            similarity = cosine_similarity(
                model.encode([question]),
                model.encode([sample])
            )[0][0]

            if similarity > 0.75:

                answer = data["response"]
                break

        if answer:
            break

    # DOCUMENT SEARCH
    if not answer:

        answer = semantic_search(question)

    # FALLBACK
    if not answer:

        answer = """
I could not find an exact answer for this question 😊

Please consult AWBI or local authorities for issue-specific clarification.
"""

    st.subheader("Answer")

    st.success(answer)

    with st.expander("AWBI / Government Context"):

        st.info(
            "This assistant uses government and AWBI animal welfare documents."
        )

st.markdown("---")

st.caption("Built for pet parents of Mangalam Ananda 🐶")
