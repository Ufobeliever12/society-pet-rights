import streamlit as st
from PyPDF2 import PdfReader
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document

st.set_page_config(
    page_title="Society Pet Rights",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 Society Pet Rights")
st.caption("Mangalam Anada • AI Pet Rights Assistant")

api_key = st.secrets["OPENAI_API_KEY"]

pdf_path = "163282565895pet_dog_circular_26_2_2015.pdf"

@st.cache_resource
def load_docs():
    pdf_reader = PdfReader(pdf_path)

    text = ""

    for page in pdf_reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    chunk_size = 1500

    chunks = [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]

    docs = [
        Document(page_content=chunk)
        for chunk in chunks
    ]

    return docs

docs = load_docs()

llm = ChatOpenAI(
    temperature=0,
    openai_api_key=api_key,
    model="gpt-4o-mini"
)

chain = load_qa_chain(
    llm,
    chain_type="stuff"
)

st.markdown("### Quick Questions")

quick_questions = [
    "Can RWAs ban pets?",
    "Can dogs use lifts?",
    "Can societies fine pet owners?",
    "Is feeding street dogs legal?",
    "Can pets enter parks?",
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

        relevant_docs = docs[:4]

        response = chain.run(
            input_documents=relevant_docs,
            question=(
                "Answer only using the AWBI pet rules document. "
                "Keep the answer simple, legally accurate, and easy to understand.\n\n"
                f"Question: {question}"
            )
        )

        st.subheader("Answer")
        st.success(response)

        with st.expander("Relevant Guidelines"):
            for i, doc in enumerate(relevant_docs):
                st.write(f"Section {i+1}")
                st.info(doc.page_content[:700])

st.markdown("---")
st.caption("Built for pet parents of Mangalam Anada 🐶")
