import streamlit as st
from transformers import pipeline
from transformers import Conversation
import torch

st.write("""
I am a *chat bot*. I will respond based on your input to the best of my ability.
"""
)

st.subheader('What question do you have?!')

user_input = st.text_input("Please ask one query at a time.",)

user_input = Conversation(user_input)


@st.cache(allow_output_mutation=True)
def instantiate_generator():
    return pipeline('conversational')


generator = instantiate_generator()
response = generator(user_input)

st.markdown(response)

