import streamlit as st


def app():

    all_writings = []

    for key in st.secrets:
        if isinstance(st.secrets[key], list):
            for writing in st.secrets[key]:
                if writing not in all_writings:
                    all_writings.append(writing)

    for i, writing in enumerate(all_writings):
        display_writing(writing, i)


# TODO: solve import error and use display writing from page utils
def display_writing(text: str, i: int = None):
    if i:
        st.subheader(str(i))
    split_out = text.split('\n')
    for line in split_out:
        text = f'<p style="font-family:Arial; font-size: 16px;">{line}</p>'
        st.markdown(text, unsafe_allow_html=True)