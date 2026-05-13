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
            "can security stop dogs from lift",
            "can pets use service lift"
        ],
        "response": """
No 😊 Pets cannot be denied access to lifts or elevators used by residents.

Housing societies also cannot impose separate lift charges or force pet owners to use separate lifts only.
"""
    },

    "dog_bite": {
        "questions": [
            "if a pet dog bites someone who is responsible",
            "dog bite responsibility",
            "pet dog attacks resident",
            "legal action against pet owners",
            "dog bite legal action",
            "is there legal action if dog bites someone",
            "can police take action after dog bite",
            "can pet owners be fined after dog bite"
        ],
        "response": """
Yes. If a pet dog bites or injures someone, authorities may take action depending on the severity of the incident and the circumstances involved.

Pet owners are expected to maintain proper control, vaccination, and safe handling of their pets.

Complaints or incidents may be reviewed by local authorities or police if negligence, unsafe handling, or repeated aggression is involved.
"""
    },

    "feeding": {
        "questions": [
            "is feeding stray dogs legal",
            "can society stop dog feeding",
            "can feeders be fined",
            "is feeding community dogs legal"
        ],
        "response": """
Yes 😊 Feeding street or community dogs is legal in India.

However, feeders should maintain cleanliness and avoid causing inconvenience to other residents.
"""
    },

    "clubhouse": {
        "questions": [
            "can pets enter clubhouse",
            "are dogs allowed in clubhouse",
            "can pets enter indoor facilities",
            "can dogs go inside clubhouse"
        ],
        "response": """
Societies may create reasonable rules for sensitive indoor spaces such as clubhouses, gyms, or swimming pool areas 😊

However, arbitrary or discriminatory restrictions against pets are generally discouraged.
"""
    },

    "play_area": {
        "questions": [
            "can pets be banned from children's play areas",
            "can dogs enter play area",
            "are pets allowed in kids play area",
            "can pets go near children play area"
        ],
        "response": """
Societies may create reasonable safety guidelines for dedicated children's play areas 😊

However, blanket discrimination against pets across all common areas is generally discouraged.

Pet owners should ensure proper supervision and responsible handling near children.
"""
    },

    "common_areas": {
        "questions": [
            "can pets use common area",
            "can dogs walk in garden",
            "can pets walk in society",
            "can dogs enter common spaces"
        ],
        "response": """
Yes 😊 Pets are generally allowed in common areas such as pathways, gardens, and open spaces.

Pet owners should ensure cleanliness, supervision, and responsible handling.
"""
    },

    "barking": {
        "questions": [
            "dog barking complaint",
            "can society complain about barking",
            "pet noise complaint",
            "what if dog barks at night"
        ],
        "response": """
Pet owners should take reasonable steps to reduce excessive disturbance caused by barking 😊

However, pets generally cannot be forcibly removed merely because complaints are raised.

Peaceful communication and practical solutions between residents are encouraged.
"""
    },

    "vaccination": {
        "questions": [
            "is pet vaccination mandatory",
            "should dogs be vaccinated",
            "dog vaccine rules",
            "pet vaccination rules"
        ],
        "response": """
Yes 😊 Pet owners are expected to ensure their pets are properly vaccinated and maintained in a healthy condition.

Vaccination helps protect both pets and residents and supports responsible pet ownership.
"""
    }
}

LEGAL_KEYWORDS = [
    "legal",
    "police",
    "liable",
    "liability",
    "court",
    "fine",
    "action",
    "complaint",
    "case",
    "crime",
    "punishment",
    "illegal"
]

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

        legal_question = False

        for word in LEGAL_KEYWORDS:

            if word in question.lower():
                legal_question = True
                break

        if legal_question:

            return f"""
⚖️ Based on AWBI / Government guidelines:

{document_paragraphs[best_index]}
"""

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
