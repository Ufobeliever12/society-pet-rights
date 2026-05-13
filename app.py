import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
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
def load_vector_store():
    pdf_reader = PdfReader(pdf_path)

    text = ""
    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    docs = [Document(page_content=chunk) for chunk in chunks]

    embeddings = OpenAIEmbeddings(
        openai_api_key=api_key
    )

    vectorstore = FAISS.from_documents(docs, embeddings)

    return vectorstore

vectorstore = load_vector_store()

llm = ChatOpenAI(
    temperature=0,
    openai_api_key=api_key,
    model="gpt-4o-mini"
)

chain = load_qa_chain(llm, chain_type="stuff")

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

        docs = vectorstore.similarity_search(question, k=4)

        response = chain.run(
            input_documents=docs,
            question=(
                "Answer only using the AWBI pet rules document. "
                "Keep the answer simple, clear, and legally accurate.\n\n"
                f"Question: {question}"
            )
        )

        st.subheader("Answer")
        st.success(response)

        with st.expander("Relevant Guidelines"):
            for i, doc in enumerate(docs):
                st.write(f"Section {i+1}")
                st.info(doc.page_content[:700])

st.markdown("---")
st.caption("Built for pet parents of Mangalam Anada 🐶")
