import streamlit as st
from PyPDF2 import PdfReader
from difflib import SequenceMatcher

st.set_page_config(
    page_title="Society Pet Rights",
    page_icon="🐾",
    layout="centered"
)

# Step-by-Step Guide Using YOUR Actual app.py

I checked your uploaded code.

Your entire logic is inside:

```python
app.py
```

So you only need to edit ONE file.

---

# STEP 1 — Open app.py

Open:

```text
society-pet-rights-main/app.py
```

You will see this at the top:

```python
import streamlit as st
from PyPDF2 import PdfReader
```

---

# STEP 2 — Replace The Import Section

## DELETE THIS

```python
import streamlit as st
from PyPDF2 import PdfReader
```

---

## PASTE THIS

```python
import streamlit as st
from PyPDF2 import PdfReader
from difflib import SequenceMatcher
```

---

# STEP 3 — Find The RULES Block

Scroll down.

You will find:

```python
RULES = {
```

This starts around line 27.

The full RULES section ends here:

```python
}
```

Right BEFORE:

```python
st.markdown("### Quick Questions")
```

---

# STEP 4 — DELETE THE FULL OLD RULES BLOCK

Delete EVERYTHING starting from:

```python
RULES = {
```

UNTIL the closing:

```python
}
```

---

# STEP 5 — PASTE THIS NEW RULES BLOCK

Paste THIS FULL BLOCK:

```python
RULES = {

    "lifts": {
        "questions": [
            "can dogs use lifts",
            "can pets use elevators",
            "can dogs travel in lift",
            "can security stop pets from using lift",
            "can society deny lift access to dogs",
            "can pets use society elevators",
            "can dogs go in elevator",
            "can pets travel in society lift"
        ],
        "response": """
Yes 😊 Residents with pets are allowed to use lifts and elevators used by other residents.

As per AWBI guidelines, housing societies cannot deny lift access to pets or impose separate lift charges for pets.

Pet owners should ensure pets are safely handled and maintain cleanliness while using common facilities.
"""
    },

    "ban_pets": {
        "questions": [
            "can society ban pets",
            "can apartment ban pets",
            "can rwa remove pets",
            "can society force us to remove dog",
            "are dogs not allowed in society",
            "can housing society ban dogs"
        ],
        "response": """
No 😊 Housing societies and RWAs cannot legally ban pets or force residents to remove pets from their homes.

Pet owners are expected to maintain hygiene, cleanliness, and safety while keeping pets in residential communities.
"""
    },

    "common_areas": {
        "questions": [
            "can dogs walk in garden",
            "can pets play in common area",
            "can i walk my dog in society",
            "can pets use common area",
            "can society stop dog walking",
            "can dogs enter common areas",
            "can pets walk in society"
        ],
        "response": """
Yes 😊 Pets are generally allowed in common areas such as pathways, gardens, and open spaces.

Residents should cooperate on cleanliness and safety, but complete bans on pet movement in common areas are generally discouraged.
"""
    },

    "feeding": {
        "questions": [
            "is feeding stray dogs legal",
            "can i feed street dogs",
            "can society stop dog feeding",
            "is feeding stray dogs allowed",
            "can residents feed stray dogs",
            "is stray feeding illegal"
        ],
        "response": """
Yes 😊 Feeding street dogs is legal in India.

Feeders should choose suitable spots and maintain cleanliness to avoid inconvenience to other residents.

AWBI guidelines encourage peaceful coexistence and humane treatment of community animals.
"""
    },

    "fines": {
        "questions": [
            "can society fine pet owners",
            "pet penalty",
            "dog fine",
            "lift charges for pets",
            "pet maintenance fine",
            "can society charge extra for pets"
        ],
        "response": """
Housing societies generally cannot impose arbitrary penalties or separate lift charges specifically for pets without proper legal authority.

However, genuine damages caused by negligence may still be recoverable under normal society rules.
"""
    },

    "barking": {
        "questions": [
            "dog barking complaint",
            "what if dog barks",
            "can society complain about barking",
            "pet noise complaint",
            "can society remove barking dog"
        ],
        "response": """
Pet owners should take reasonable steps to reduce excessive disturbance caused by barking.

However, pets cannot be forcibly removed simply because of complaints.

Peaceful communication and practical solutions between residents are always encouraged 😊
"""
    },

    "vaccination": {
        "questions": [
            "should dogs be vaccinated",
            "pet vaccination rules",
            "dog vaccine mandatory",
            "pet registration and vaccination",
            "is vaccination required for pets"
        ],
        "response": """
Yes 😊 Pet owners should ensure pets are properly vaccinated and maintained in a healthy condition.

Vaccination records are useful for both pet safety and community confidence.
"""
    }
}
```

---

# STEP 6 — Find The Old Matching Logic

Scroll lower.

You will find THIS:

```python
answer = None

for topic, data in RULES.items():

    for keyword in data["keywords"]:

        if keyword in q:
            answer = data["response"]
            break

    if answer:
        break
```

---

# STEP 7 — DELETE THAT FULL BLOCK

Delete the ENTIRE thing.

---

# STEP 8 — PASTE THIS NEW LOGIC

```python
answer = None
best_score = 0
best_answer = None

for topic, data in RULES.items():

    for sample_question in data["questions"]:

        score = SequenceMatcher(
            None,
            q.lower(),
            sample_question.lower()
        ).ratio()

        if score > best_score:
            best_score = score
            best_answer = data["response"]

if best_score > 0.45:
    answer = best_answer
```

---

# STEP 9 — Replace The Default Fallback Answer

Find THIS:

```python
if not answer:

    answer = """
According to AWBI guidelines, pet owners and residents should coexist peacefully while maintaining cleanliness and safety in common areas.

RWAs should avoid arbitrary restrictions, harassment, or intimidation of pet owners.
"""
```

---

# DELETE IT

---

# PASTE THIS

```python
if not answer:

    answer = """
I could not find an exact rule for this question 😊

However, according to AWBI guidelines, pet owners and other residents should coexist peacefully while maintaining cleanliness, safety, and mutual respect.

You can also try asking questions related to:

• lifts
• common areas
• pet bans
• feeding street dogs
• barking complaints
• fines
• vaccination
"""
```

---

# STEP 10 — Improve App Heading

Find:

```python
st.title("🐾 Society Pet Rights")
st.caption("Mangalam Anada • Pet Rights Assistant")
```

---

# REPLACE WITH

```python
st.title("🐶 Mangalam Ananda Pet Rights Assistant")

st.caption(
    "Helping residents understand pet-related guidelines peacefully and clearly 😊"
)
```

---

# STEP 11 — Save The File

Press:

```text
CTRL + S
```

---

# STEP 12 — Run The App Locally

Open terminal inside project folder.

Run:

```bash
streamlit run app.py
```

---

# STEP 13 — Deploy Updated Version

Push changes to GitHub.

Streamlit Cloud will auto-update.

---

# AFTER THIS YOUR APP WILL:

✅ answer more naturally
✅ understand similar questions
✅ feel more intelligent
✅ remain 100% free
✅ require no API
✅ require no OpenAI billing
✅ work on free Streamlit hosting

Most importantly:

Questions like:

* Can dogs use lifts?
* Can pets travel in elevator?
* Can security stop dogs from lift?

Will ALL return the correct answer.


pdf_path = "163282565895pet_dog_circular_26_2_2015.pdf"

@st.cache_data
def load_pdf_text():

    pdf_reader = PdfReader(pdf_path)

    text = ""

    for page in pdf_reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text.lower()

pdf_text = load_pdf_text()

# Step-by-Step Guide Using YOUR Actual app.py

I checked your uploaded code.

Your entire logic is inside:

```python
app.py
```

So you only need to edit ONE file.

---

# STEP 1 — Open app.py

Open:

```text
society-pet-rights-main/app.py
```

You will see this at the top:

```python
import streamlit as st
from PyPDF2 import PdfReader
```

---

# STEP 2 — Replace The Import Section

## DELETE THIS

```python
import streamlit as st
from PyPDF2 import PdfReader
```

---

## PASTE THIS

```python
import streamlit as st
from PyPDF2 import PdfReader
from difflib import SequenceMatcher
```

---

# STEP 3 — Find The RULES Block

Scroll down.

You will find:

```python
RULES = {
```

This starts around line 27.

The full RULES section ends here:

```python
}
```

Right BEFORE:

```python
st.markdown("### Quick Questions")
```

---

# STEP 4 — DELETE THE FULL OLD RULES BLOCK

Delete EVERYTHING starting from:

```python
RULES = {
```

UNTIL the closing:

```python
}
```

---

# STEP 5 — PASTE THIS NEW RULES BLOCK

Paste THIS FULL BLOCK:

```python
RULES = {

    "lifts": {
        "questions": [
            "can dogs use lifts",
            "can pets use elevators",
            "can dogs travel in lift",
            "can security stop pets from using lift",
            "can society deny lift access to dogs",
            "can pets use society elevators",
            "can dogs go in elevator",
            "can pets travel in society lift"
        ],
        "response": """
Yes 😊 Residents with pets are allowed to use lifts and elevators used by other residents.

As per AWBI guidelines, housing societies cannot deny lift access to pets or impose separate lift charges for pets.

Pet owners should ensure pets are safely handled and maintain cleanliness while using common facilities.
"""
    },

    "ban_pets": {
        "questions": [
            "can society ban pets",
            "can apartment ban pets",
            "can rwa remove pets",
            "can society force us to remove dog",
            "are dogs not allowed in society",
            "can housing society ban dogs"
        ],
        "response": """
No 😊 Housing societies and RWAs cannot legally ban pets or force residents to remove pets from their homes.

Pet owners are expected to maintain hygiene, cleanliness, and safety while keeping pets in residential communities.
"""
    },

    "common_areas": {
        "questions": [
            "can dogs walk in garden",
            "can pets play in common area",
            "can i walk my dog in society",
            "can pets use common area",
            "can society stop dog walking",
            "can dogs enter common areas",
            "can pets walk in society"
        ],
        "response": """
Yes 😊 Pets are generally allowed in common areas such as pathways, gardens, and open spaces.

Residents should cooperate on cleanliness and safety, but complete bans on pet movement in common areas are generally discouraged.
"""
    },

    "feeding": {
        "questions": [
            "is feeding stray dogs legal",
            "can i feed street dogs",
            "can society stop dog feeding",
            "is feeding stray dogs allowed",
            "can residents feed stray dogs",
            "is stray feeding illegal"
        ],
        "response": """
Yes 😊 Feeding street dogs is legal in India.

Feeders should choose suitable spots and maintain cleanliness to avoid inconvenience to other residents.

AWBI guidelines encourage peaceful coexistence and humane treatment of community animals.
"""
    },

    "fines": {
        "questions": [
            "can society fine pet owners",
            "pet penalty",
            "dog fine",
            "lift charges for pets",
            "pet maintenance fine",
            "can society charge extra for pets"
        ],
        "response": """
Housing societies generally cannot impose arbitrary penalties or separate lift charges specifically for pets without proper legal authority.

However, genuine damages caused by negligence may still be recoverable under normal society rules.
"""
    },

    "barking": {
        "questions": [
            "dog barking complaint",
            "what if dog barks",
            "can society complain about barking",
            "pet noise complaint",
            "can society remove barking dog"
        ],
        "response": """
Pet owners should take reasonable steps to reduce excessive disturbance caused by barking.

However, pets cannot be forcibly removed simply because of complaints.

Peaceful communication and practical solutions between residents are always encouraged 😊
"""
    },

    "vaccination": {
        "questions": [
            "should dogs be vaccinated",
            "pet vaccination rules",
            "dog vaccine mandatory",
            "pet registration and vaccination",
            "is vaccination required for pets"
        ],
        "response": """
Yes 😊 Pet owners should ensure pets are properly vaccinated and maintained in a healthy condition.

Vaccination records are useful for both pet safety and community confidence.
"""
    }
}
```

---

# STEP 6 — Find The Old Matching Logic

Scroll lower.

You will find THIS:

```python
answer = None

for topic, data in RULES.items():

    for keyword in data["keywords"]:

        if keyword in q:
            answer = data["response"]
            break

    if answer:
        break
```

---

# STEP 7 — DELETE THAT FULL BLOCK

Delete the ENTIRE thing.

---

# STEP 8 — PASTE THIS NEW LOGIC

```python
answer = None
best_score = 0
best_answer = None

for topic, data in RULES.items():

    for sample_question in data["questions"]:

        score = SequenceMatcher(
            None,
            q.lower(),
            sample_question.lower()
        ).ratio()

        if score > best_score:
            best_score = score
            best_answer = data["response"]

if best_score > 0.45:
    answer = best_answer
```

---

# STEP 9 — Replace The Default Fallback Answer

Find THIS:

```python
if not answer:

    answer = """
According to AWBI guidelines, pet owners and residents should coexist peacefully while maintaining cleanliness and safety in common areas.

RWAs should avoid arbitrary restrictions, harassment, or intimidation of pet owners.
"""
```

---

# DELETE IT

---

# PASTE THIS

```python
if not answer:

    answer = """
I could not find an exact rule for this question 😊

However, according to AWBI guidelines, pet owners and other residents should coexist peacefully while maintaining cleanliness, safety, and mutual respect.

You can also try asking questions related to:

• lifts
• common areas
• pet bans
• feeding street dogs
• barking complaints
• fines
• vaccination
"""
```

---

# STEP 10 — Improve App Heading

Find:

```python
st.title("🐾 Society Pet Rights")
st.caption("Mangalam Anada • Pet Rights Assistant")
```

---

# REPLACE WITH

```python
st.title("🐶 Mangalam Ananda Pet Rights Assistant")

st.caption(
    "Helping residents understand pet-related guidelines peacefully and clearly 😊"
)
```

---

# STEP 11 — Save The File

Press:

```text
CTRL + S
```

---

# STEP 12 — Run The App Locally

Open terminal inside project folder.

Run:

```bash
streamlit run app.py
```

---

# STEP 13 — Deploy Updated Version

Push changes to GitHub.

Streamlit Cloud will auto-update.

---

# AFTER THIS YOUR APP WILL:

✅ answer more naturally
✅ understand similar questions
✅ feel more intelligent
✅ remain 100% free
✅ require no API
✅ require no OpenAI billing
✅ work on free Streamlit hosting

Most importantly:

Questions like:

* Can dogs use lifts?
* Can pets travel in elevator?
* Can security stop dogs from lift?

Will ALL return the correct answer.


st.markdown("### Quick Questions")

quick_questions = [
    "Can RWAs ban pets?",
    "Can dogs use lifts?",
    "Can societies fine pet owners?",
    "Can I play with my dog in garden area?",
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

    q = question.lower()

    # Step-by-Step Guide Using YOUR Actual app.py

I checked your uploaded code.

Your entire logic is inside:

```python
app.py
```

So you only need to edit ONE file.

---

# STEP 1 — Open app.py

Open:

```text
society-pet-rights-main/app.py
```

You will see this at the top:

```python
import streamlit as st
from PyPDF2 import PdfReader
```

---

# STEP 2 — Replace The Import Section

## DELETE THIS

```python
import streamlit as st
from PyPDF2 import PdfReader
```

---

## PASTE THIS

```python
import streamlit as st
from PyPDF2 import PdfReader
from difflib import SequenceMatcher
```

---

# STEP 3 — Find The RULES Block

Scroll down.

You will find:

```python
RULES = {
```

This starts around line 27.

The full RULES section ends here:

```python
}
```

Right BEFORE:

```python
st.markdown("### Quick Questions")
```

---

# STEP 4 — DELETE THE FULL OLD RULES BLOCK

Delete EVERYTHING starting from:

```python
RULES = {
```

UNTIL the closing:

```python
}
```

---

# STEP 5 — PASTE THIS NEW RULES BLOCK

Paste THIS FULL BLOCK:

```python
RULES = {

    "lifts": {
        "questions": [
            "can dogs use lifts",
            "can pets use elevators",
            "can dogs travel in lift",
            "can security stop pets from using lift",
            "can society deny lift access to dogs",
            "can pets use society elevators",
            "can dogs go in elevator",
            "can pets travel in society lift"
        ],
        "response": """
Yes 😊 Residents with pets are allowed to use lifts and elevators used by other residents.

As per AWBI guidelines, housing societies cannot deny lift access to pets or impose separate lift charges for pets.

Pet owners should ensure pets are safely handled and maintain cleanliness while using common facilities.
"""
    },

    "ban_pets": {
        "questions": [
            "can society ban pets",
            "can apartment ban pets",
            "can rwa remove pets",
            "can society force us to remove dog",
            "are dogs not allowed in society",
            "can housing society ban dogs"
        ],
        "response": """
No 😊 Housing societies and RWAs cannot legally ban pets or force residents to remove pets from their homes.

Pet owners are expected to maintain hygiene, cleanliness, and safety while keeping pets in residential communities.
"""
    },

    "common_areas": {
        "questions": [
            "can dogs walk in garden",
            "can pets play in common area",
            "can i walk my dog in society",
            "can pets use common area",
            "can society stop dog walking",
            "can dogs enter common areas",
            "can pets walk in society"
        ],
        "response": """
Yes 😊 Pets are generally allowed in common areas such as pathways, gardens, and open spaces.

Residents should cooperate on cleanliness and safety, but complete bans on pet movement in common areas are generally discouraged.
"""
    },

    "feeding": {
        "questions": [
            "is feeding stray dogs legal",
            "can i feed street dogs",
            "can society stop dog feeding",
            "is feeding stray dogs allowed",
            "can residents feed stray dogs",
            "is stray feeding illegal"
        ],
        "response": """
Yes 😊 Feeding street dogs is legal in India.

Feeders should choose suitable spots and maintain cleanliness to avoid inconvenience to other residents.

AWBI guidelines encourage peaceful coexistence and humane treatment of community animals.
"""
    },

    "fines": {
        "questions": [
            "can society fine pet owners",
            "pet penalty",
            "dog fine",
            "lift charges for pets",
            "pet maintenance fine",
            "can society charge extra for pets"
        ],
        "response": """
Housing societies generally cannot impose arbitrary penalties or separate lift charges specifically for pets without proper legal authority.

However, genuine damages caused by negligence may still be recoverable under normal society rules.
"""
    },

    "barking": {
        "questions": [
            "dog barking complaint",
            "what if dog barks",
            "can society complain about barking",
            "pet noise complaint",
            "can society remove barking dog"
        ],
        "response": """
Pet owners should take reasonable steps to reduce excessive disturbance caused by barking.

However, pets cannot be forcibly removed simply because of complaints.

Peaceful communication and practical solutions between residents are always encouraged 😊
"""
    },

    "vaccination": {
        "questions": [
            "should dogs be vaccinated",
            "pet vaccination rules",
            "dog vaccine mandatory",
            "pet registration and vaccination",
            "is vaccination required for pets"
        ],
        "response": """
Yes 😊 Pet owners should ensure pets are properly vaccinated and maintained in a healthy condition.

Vaccination records are useful for both pet safety and community confidence.
"""
    }
}
```

---

# STEP 6 — Find The Old Matching Logic

Scroll lower.

You will find THIS:

```python
answer = None

for topic, data in RULES.items():

    for keyword in data["keywords"]:

        if keyword in q:
            answer = data["response"]
            break

    if answer:
        break
```

---

# STEP 7 — DELETE THAT FULL BLOCK

Delete the ENTIRE thing.

---

# STEP 8 — PASTE THIS NEW LOGIC

```python
answer = None
best_score = 0
best_answer = None

for topic, data in RULES.items():

    for sample_question in data["questions"]:

        score = SequenceMatcher(
            None,
            q.lower(),
            sample_question.lower()
        ).ratio()

        if score > best_score:
            best_score = score
            best_answer = data["response"]

if best_score > 0.45:
    answer = best_answer
```

---

# STEP 9 — Replace The Default Fallback Answer

Find THIS:

```python
if not answer:

    answer = """
According to AWBI guidelines, pet owners and residents should coexist peacefully while maintaining cleanliness and safety in common areas.

RWAs should avoid arbitrary restrictions, harassment, or intimidation of pet owners.
"""
```

---

# DELETE IT

---

# PASTE THIS

```python
if not answer:

    answer = """
I could not find an exact rule for this question 😊

However, according to AWBI guidelines, pet owners and other residents should coexist peacefully while maintaining cleanliness, safety, and mutual respect.

You can also try asking questions related to:

• lifts
• common areas
• pet bans
• feeding street dogs
• barking complaints
• fines
• vaccination
"""
```

---

# STEP 10 — Improve App Heading

Find:

```python
st.title("🐾 Society Pet Rights")
st.caption("Mangalam Anada • Pet Rights Assistant")
```

---

# REPLACE WITH

```python
st.title("🐶 Mangalam Ananda Pet Rights Assistant")

st.caption(
    "Helping residents understand pet-related guidelines peacefully and clearly 😊"
)
```

---

# STEP 11 — Save The File

Press:

```text
CTRL + S
```

---

# STEP 12 — Run The App Locally

Open terminal inside project folder.

Run:

```bash
streamlit run app.py
```

---

# STEP 13 — Deploy Updated Version

Push changes to GitHub.

Streamlit Cloud will auto-update.

---

# AFTER THIS YOUR APP WILL:

✅ answer more naturally
✅ understand similar questions
✅ feel more intelligent
✅ remain 100% free
✅ require no API
✅ require no OpenAI billing
✅ work on free Streamlit hosting

Most importantly:

Questions like:

* Can dogs use lifts?
* Can pets travel in elevator?
* Can security stop dogs from lift?

Will ALL return the correct answer.


 # Step-by-Step Guide Using YOUR Actual app.py

I checked your uploaded code.

Your entire logic is inside:

```python
app.py
```

So you only need to edit ONE file.

---

# STEP 1 — Open app.py

Open:

```text
society-pet-rights-main/app.py
```

You will see this at the top:

```python
import streamlit as st
from PyPDF2 import PdfReader
```

---

# STEP 2 — Replace The Import Section

## DELETE THIS

```python
import streamlit as st
from PyPDF2 import PdfReader
```

---

## PASTE THIS

```python
import streamlit as st
from PyPDF2 import PdfReader
from difflib import SequenceMatcher
```

---

# STEP 3 — Find The RULES Block

Scroll down.

You will find:

```python
RULES = {
```

This starts around line 27.

The full RULES section ends here:

```python
}
```

Right BEFORE:

```python
st.markdown("### Quick Questions")
```

---

# STEP 4 — DELETE THE FULL OLD RULES BLOCK

Delete EVERYTHING starting from:

```python
RULES = {
```

UNTIL the closing:

```python
}
```

---

# STEP 5 — PASTE THIS NEW RULES BLOCK

Paste THIS FULL BLOCK:

```python
RULES = {

    "lifts": {
        "questions": [
            "can dogs use lifts",
            "can pets use elevators",
            "can dogs travel in lift",
            "can security stop pets from using lift",
            "can society deny lift access to dogs",
            "can pets use society elevators",
            "can dogs go in elevator",
            "can pets travel in society lift"
        ],
        "response": """
Yes 😊 Residents with pets are allowed to use lifts and elevators used by other residents.

As per AWBI guidelines, housing societies cannot deny lift access to pets or impose separate lift charges for pets.

Pet owners should ensure pets are safely handled and maintain cleanliness while using common facilities.
"""
    },

    "ban_pets": {
        "questions": [
            "can society ban pets",
            "can apartment ban pets",
            "can rwa remove pets",
            "can society force us to remove dog",
            "are dogs not allowed in society",
            "can housing society ban dogs"
        ],
        "response": """
No 😊 Housing societies and RWAs cannot legally ban pets or force residents to remove pets from their homes.

Pet owners are expected to maintain hygiene, cleanliness, and safety while keeping pets in residential communities.
"""
    },

    "common_areas": {
        "questions": [
            "can dogs walk in garden",
            "can pets play in common area",
            "can i walk my dog in society",
            "can pets use common area",
            "can society stop dog walking",
            "can dogs enter common areas",
            "can pets walk in society"
        ],
        "response": """
Yes 😊 Pets are generally allowed in common areas such as pathways, gardens, and open spaces.

Residents should cooperate on cleanliness and safety, but complete bans on pet movement in common areas are generally discouraged.
"""
    },

    "feeding": {
        "questions": [
            "is feeding stray dogs legal",
            "can i feed street dogs",
            "can society stop dog feeding",
            "is feeding stray dogs allowed",
            "can residents feed stray dogs",
            "is stray feeding illegal"
        ],
        "response": """
Yes 😊 Feeding street dogs is legal in India.

Feeders should choose suitable spots and maintain cleanliness to avoid inconvenience to other residents.

AWBI guidelines encourage peaceful coexistence and humane treatment of community animals.
"""
    },

    "fines": {
        "questions": [
            "can society fine pet owners",
            "pet penalty",
            "dog fine",
            "lift charges for pets",
            "pet maintenance fine",
            "can society charge extra for pets"
        ],
        "response": """
Housing societies generally cannot impose arbitrary penalties or separate lift charges specifically for pets without proper legal authority.

However, genuine damages caused by negligence may still be recoverable under normal society rules.
"""
    },

    "barking": {
        "questions": [
            "dog barking complaint",
            "what if dog barks",
            "can society complain about barking",
            "pet noise complaint",
            "can society remove barking dog"
        ],
        "response": """
Pet owners should take reasonable steps to reduce excessive disturbance caused by barking.

However, pets cannot be forcibly removed simply because of complaints.

Peaceful communication and practical solutions between residents are always encouraged 😊
"""
    },

    "vaccination": {
        "questions": [
            "should dogs be vaccinated",
            "pet vaccination rules",
            "dog vaccine mandatory",
            "pet registration and vaccination",
            "is vaccination required for pets"
        ],
        "response": """
Yes 😊 Pet owners should ensure pets are properly vaccinated and maintained in a healthy condition.

Vaccination records are useful for both pet safety and community confidence.
"""
    }
}
```

---

# STEP 6 — Find The Old Matching Logic

Scroll lower.

You will find THIS:

```python
answer = None

for topic, data in RULES.items():

    for keyword in data["keywords"]:

        if keyword in q:
            answer = data["response"]
            break

    if answer:
        break
```

---

# STEP 7 — DELETE THAT FULL BLOCK

Delete the ENTIRE thing.

---

# STEP 8 — PASTE THIS NEW LOGIC

```python
answer = None
best_score = 0
best_answer = None

for topic, data in RULES.items():

    for sample_question in data["questions"]:

        score = SequenceMatcher(
            None,
            q.lower(),
            sample_question.lower()
        ).ratio()

        if score > best_score:
            best_score = score
            best_answer = data["response"]

if best_score > 0.45:
    answer = best_answer
```

---

# STEP 9 — Replace The Default Fallback Answer

Find THIS:

```python
if not answer:

    answer = """
According to AWBI guidelines, pet owners and residents should coexist peacefully while maintaining cleanliness and safety in common areas.

RWAs should avoid arbitrary restrictions, harassment, or intimidation of pet owners.
"""
```

---

# DELETE IT

---

# PASTE THIS

```python
if not answer:

    answer = """
I could not find an exact rule for this question 😊

However, according to AWBI guidelines, pet owners and other residents should coexist peacefully while maintaining cleanliness, safety, and mutual respect.

You can also try asking questions related to:

• lifts
• common areas
• pet bans
• feeding street dogs
• barking complaints
• fines
• vaccination
"""
```

---

# STEP 10 — Improve App Heading

Find:

```python
st.title("🐾 Society Pet Rights")
st.caption("Mangalam Anada • Pet Rights Assistant")
```

---

# REPLACE WITH

```python
st.title("🐶 Mangalam Ananda Pet Rights Assistant")

st.caption(
    "Helping residents understand pet-related guidelines peacefully and clearly 😊"
)
```

---

# STEP 11 — Save The File

Press:

```text
CTRL + S
```

---

# STEP 12 — Run The App Locally

Open terminal inside project folder.

Run:

```bash
streamlit run app.py
```

---

# STEP 13 — Deploy Updated Version

Push changes to GitHub.

Streamlit Cloud will auto-update.

---

# AFTER THIS YOUR APP WILL:

✅ answer more naturally
✅ understand similar questions
✅ feel more intelligent
✅ remain 100% free
✅ require no API
✅ require no OpenAI billing
✅ work on free Streamlit hosting

Most importantly:

Questions like:

* Can dogs use lifts?
* Can pets travel in elevator?
* Can security stop dogs from lift?

Will ALL return the correct answer.


    st.subheader("Answer")
    st.success(answer)

    with st.expander("AWBI Context"):
        st.info(
            "Animal Welfare Board of India Guidelines "
            "on Pet and Street Dogs (26 February 2015)."
        )

st.markdown("---")
st.caption("Built for pet parents of Mangalam Anada 🐶")
