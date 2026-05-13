import streamlit as st
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

st.set_page_config(
    page_title="Society Pet Rights",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 Society Pet Rights")
st.caption("Mangalam Anada • Pet Rights Assistant")

pdf_path = "163282565895pet_dog_circular_26_2_2015.pdf"

@st.cache_resource
def load_knowledge_base():

    pdf_reader = PdfReader(pdf_path)

    text = ""

    for page in pdf_reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    chunk_size = 800

    chunks = [
        text[i:i + chunk_size].strip()
        for i in range(0, len(text), chunk_size)
    ]

    chunks = [
        chunk
        for chunk in chunks
        if len(chunk) > 50
    ]

    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = np.array(
        model.encode(chunks)
    )

    return model, chunks, embeddings

model, chunks, embeddings = load_knowledge_base()

st.markdown("### Quick Questions")

quick_questions = [
    "Can RWAs ban pets?",
    "Can dogs use lifts?",
    "Can societies fine pet owners?",
    "Can pets play in garden areas?",
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

    with st.spinner("Checking AWBI guidelines..."):

        question_embedding = model.encode([question])

        similarities = cosine_similarity(
            question_embedding,
            embeddings
        )[0]

        top_indices = np.argsort(similarities)[-3:][::-1]

        relevant_sections = [
            chunks[i]
            for i in top_indices
        ]

        answer = "\n\n".join(relevant_sections)

        st.subheader("Relevant Guidelines")
        st.success(answer)

        st.info(
            "Based on AWBI Guidelines on Pet & Street Dogs "
            "(26 February 2015)."
        )

st.markdown("---")
st.caption("Built for pet parents of Mangalam Anada 🐶")
