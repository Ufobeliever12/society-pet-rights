import streamlit as st
from PyPDF2 import PdfReader
from openai import OpenAI

st.set_page_config(
    page_title="Society Pet Rights",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 Society Pet Rights")
st.caption("Mangalam Anada • AI Pet Rights Assistant")

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
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

    return text

pdf_text = load_pdf_text()

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

        prompt = f'''
You are a pet rights legal assistant for residents.

Use ONLY the following AWBI guidelines document content to answer.

AWBI DOCUMENT:
{pdf_text}

QUESTION:
{question}

RULES:
- Answer clearly and simply
- Keep answers legally accurate
- Do not make up laws
- Explain in simple language for society residents
'''

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content

        st.subheader("Answer")
        st.success(answer)

st.markdown("---")
st.caption("Built for pet parents of Mangalam Anada 🐶")
