
import streamlit as st


def app():

    user_value = st.text_area('Enter new writing')
    if user_value:
        st.secrets['writings_for_future'].append(user_value)

    if st.button('Reset Writings'):
        st.secrets['writings_for_future'] = []

    for i, writing in enumerate(st.secrets['writings_for_future']):
        display_writing(writing, i)


# TODO: solve import error and use display writing from page utils
def display_writing(text: str, i: int = None):
    if i is not None:
        st.subheader(str(i))
    split_out = text.split('\n')
    for line in split_out:
        text = f'<p style="font-family:Arial; font-size: 16px;">{line}</p>'
        st.markdown(text, unsafe_allow_html=True)
