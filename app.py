import streamlit as st
from difflib import SequenceMatcher
from docx import Document
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

@st.cache_data
def load_all_docs():

    combined_text = ""

    for file in DOCX_FILES:

        try:

            doc = Document(file)

            for para in doc.paragraphs:

                text = para.text.strip()

                if text:
                    combined_text += text + "\n"

        except Exception:
            pass

    return combined_text.lower()

doc_text = load_all_docs()

RULES = {

    "lifts": {
        "questions": [
            "can dogs use lifts",
            "can pets use elevators",
            "can society deny lift access to dogs",
            "can pets use lift",
            "can security stop dogs from lift"
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
            "can society force us to remove dog",
            "are pets illegal in apartments"
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
            "can society stop dog feeding",
            "can feeders be fined",
            "is stray feeding allowed"
        ],
        "response": """
Yes 😊 Feeding street dogs is legal in India.

Feeders should maintain cleanliness and choose suitable feeding locations to avoid inconvenience to others.

Peaceful coexistence and humane treatment of community animals are encouraged under AWBI guidelines.
"""
    },

    "dog_bite": {
        "questions": [
            "if a pet dog bites someone who is responsible",
            "dog bite responsibility",
            "who is responsible if dog bites",
            "pet dog attacks resident",
            "who is liable for dog bite",
            "what if a pet dog bites someone",
            "if pet dog bites someone",
            "dog bites resident",
            "what happens if dog attacks someone"
        ],
        "response": """
Pet owners are generally expected to ensure their pets are safely handled, vaccinated, socialized, and do not pose danger to others 😊

AWBI guidelines promote responsible pet ownership, including proper behaviour management and dog bite prevention.

If any incident occurs, authorities may review:
• supervision and control of the pet
• vaccination status
• circumstances of the incident
• whether the dog was provoked or threatened

Peaceful resolution and proper safety measures are always encouraged.
"""
    },

    "clubhouse": {
        "questions": [
            "can pets enter clubhouse",
            "are dogs allowed in clubhouse",
            "can pets enter indoor facilities",
            "can dogs enter society clubhouse",
            "can pets go to clubhouse area"
        ],
        "response": """
Rules regarding clubhouse access for pets may depend on society usage policies and hygiene or safety considerations 😊

While AWBI guidelines discourage arbitrary discrimination against pets, societies may create reasonable rules for sensitive shared indoor spaces such as gyms, pools, or clubhouses if applied fairly and respectfully.
"""
    },

    "common_areas": {
        "questions": [
            "can dogs walk in garden",
            "can pets use common area",
            "can dogs enter common areas",
            "can pets walk in society",
            "can i walk my dog in society"
        ],
        "response": """
Yes 😊 Pets are generally allowed in common areas such as pathways, gardens, and open spaces.

Residents should cooperate on cleanliness and safety, while pet owners should ensure responsible handling of pets.
"""
    },

    "barking": {
        "questions": [
            "dog barking complaint",
            "can society complain about barking",
            "pet noise complaint",
            "can pets be removed because of barking",
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
            "are pets allowed without vaccination",
            "dog vaccine rules",
            "pet vaccination rules"
        ],
        "response": """
Yes 😊 Pet owners are expected to ensure their pets are properly vaccinated and maintained in a healthy condition.

Vaccination helps protect both pets and residents and supports responsible pet ownership.
"""
    }
}

def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    return text.strip()

def search_documents(question):

    paragraphs = doc_text.split("\n")

    keywords = [
        word.lower()
        for word in question.split()
        if len(word) > 3
    ]

    best_score = 0
    best_match = ""

    for para in paragraphs:

        para = clean_text(para)

        if len(para) < 80:
            continue

        para_lower = para.lower()

        keyword_hits = 0

        for word in keywords:

            if word in para_lower:
                keyword_hits += 1

        if keyword_hits == 0:
            continue

        similarity = SequenceMatcher(
            None,
            question.lower(),
            para_lower
        ).ratio()

        score = similarity + (keyword_hits * 0.08)

        if score > best_score:

            best_score = score
            best_match = para

    if best_score > 0.20:

        return f"""
📘 Based on AWBI / Government guidelines:

{best_match}
"""

    return None

st.markdown("### Quick Questions")

quick_questions = [
    "Can dogs use lifts?",
    "Can society ban pets?",
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

        answer = search_documents(question)

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
