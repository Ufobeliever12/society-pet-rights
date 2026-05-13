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

    "killing_dogs": {
        "questions": [
            "is killing a pet dog illegal",
            "can someone kill a dog legally",
            "is harming dogs illegal"
        ],
        "response": """
Yes. Killing or harming pet dogs is illegal in India.

Animal cruelty and unlawful killing of dogs may attract penalties under the Prevention of Cruelty to Animals Act and IPC Sections 428 and 429.

Courts have also clarified that indiscriminate killing of dogs is not permitted under law.
"""
    },

    "dog_bite": {
        "questions": [
            "if a pet dog bites someone who is responsible",
            "legal action against pet owners",
            "dog bite responsibility",
            "can police take action after dog bite"
        ],
        "response": """
Yes. If a pet dog bites or injures someone, authorities may take action depending on the severity of the incident and circumstances involved.

Pet owners are expected to maintain proper control, vaccination, and safe handling of their pets.
"""
    },

    "feeding": {
        "questions": [
            "is feeding stray dogs legal",
            "can society stop dog feeding",
            "feeding community dogs"
        ],
        "response": """
Yes 😊 Feeding community or stray dogs is legal in India.

However, feeders should maintain cleanliness and avoid inconvenience to other residents.
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

    return model.encode(document_paragraphs)

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
    "Is killing a pet dog illegal?",
    "Can dogs use lifts?",
    "Can society stop feeding stray dogs?",
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

    if not answer:

        answer = semantic_search(question)

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
