import streamlit as st
import requests
from utils.studio_style import apply_studio_style
from constants import OBQA_CONTEXT, OBQA_QUESTION

st.set_page_config(
    page_title="OpenBookQA",
)

endpoint = "https://api.ai21.com/studio/v1/experimental/open-book-qa"


def query(context, question):
    auth_header = "Bearer " + st.secrets['api-keys']['ai21-algo-team-prod']
    res = requests.post(endpoint,
                        headers={"Authorization": auth_header},
                        json={"context": context, "question": question})
    res = res.json()
    return res["answer"]


if __name__ == '__main__':

    apply_studio_style()
    st.title("Open Book Question Answering")

    st.write("Ask a question on a given context.")

    obqa_context = st.text_area(label="Context:", value=OBQA_CONTEXT, height=300)
    obqa_question = st.text_input(label="Question:", value=OBQA_QUESTION)

    if st.button(label="Answer"):
        with st.spinner("Loading..."):
            st.session_state["obqa_answer"] = query(obqa_context, obqa_question)

    if "obqa_answer" in st.session_state:
        st.write(f"Answer: {st.session_state['obqa_answer']}")
