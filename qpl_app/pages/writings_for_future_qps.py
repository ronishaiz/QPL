
import streamlit as st


def app():

    user_value = st.text_area('Enter new writing')
    if user_value:
        st.secrets['future_writings'].append(user_value)

    reset_list = st.button('Reset Writings')
    if reset_list:
        st.secrets['future_writings'] = []

    for i, writing in enumerate(st.secrets['future_writings']):
        display_writing(writing, i)


# TODO: solve import error and use display writing from page utils
def display_writing(text: str, i: int = None):
    if i is not None:
        st.subheader(str(i))
    split_out = text.split('\n')
    for line in split_out:
        text = f'<p style="font-family:Arial; font-size: 16px;">{line}</p>'
        st.markdown(text, unsafe_allow_html=True)
