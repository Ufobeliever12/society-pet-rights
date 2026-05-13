RULES = {

    "ban pets": {
        "keywords": ["ban", "remove pet", "not allowed", "illegal breed"],
        "response": """
RWAs and housing societies cannot legally ban pets, restrict dog breeds, or force residents to remove their pets from homes.

According to AWBI guidelines, pets are allowed in residential communities as long as owners maintain cleanliness and safety.
"""
    },

    "lifts": {
        "keywords": ["lift", "elevator"],
        "response": """
Pets cannot be denied access to lifts or elevators used by residents.

Housing societies also cannot impose special charges for using lifts with pets.
"""
    },

    "garden": {
        "keywords": ["garden", "park", "play", "walk", "common area", "basement"],
        "response": """
Pets should not be completely banned from common areas like gardens, parks, pathways, or basements.

Residents may mutually agree on suitable timings and cleanliness practices, but RWAs cannot create arbitrary pet bans.

If someone confronts or records you aggressively while walking your pet, remain calm and avoid escalation. Pet owners still have the right to use common areas responsibly.
"""
    },

    "fine": {
        "keywords": ["fine", "penalty", "charge"],
        "response": """
Housing societies cannot impose arbitrary fines or penalties on pet owners without proper legal authority.
"""
    },

    "street dogs": {
        "keywords": ["feed", "street dog", "stray dog", "feeder"],
        "response": """
Feeding street dogs is legal under Indian law.

Harassing or intimidating animal feeders is discouraged and may amount to an offense.
"""
    },

    "muzzle": {
        "keywords": ["muzzle"],
        "response": """
RWAs cannot force mandatory muzzles for all dogs.

However, pet owners should still ensure pets are safely handled in common areas.
"""
    },

    "barking": {
        "keywords": ["bark", "noise"],
        "response": """
Occasional barking is natural behavior for dogs.

Pet owners should still make reasonable efforts to minimize disturbance during late night hours.
"""
    },

    "poop": {
        "keywords": ["poop", "dirty", "clean", "waste"],
        "response": """
Pet owners should clean up pet waste and cooperate with society cleanliness practices.
"""
    }
}

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

    answer = None

    for topic, data in RULES.items():

    for keyword in data["keywords"]:

        if keyword in q:
            answer = data["response"]
            break

    if answer:
        break

if not answer:

    answer = """
According to AWBI guidelines, pet owners and residents should coexist peacefully while maintaining cleanliness and safety in common areas.

RWAs should avoid arbitrary restrictions, harassment, or intimidation of pet owners.
"""

    st.subheader("Answer")
    st.success(answer)

    with st.expander("AWBI Context"):
        st.info(
            "Animal Welfare Board of India Guidelines "
            "on Pet and Street Dogs (26 February 2015)."
        )

st.markdown("---")
st.caption("Built for pet parents of Mangalam Anada 🐶")
