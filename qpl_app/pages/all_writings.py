import streamlit as st
from qpl_app.pages.page_utils import display_writing


def app():

    all_writings = []

    for key in st.secrets:
        if isinstance(st.secrets[key], list):
            for writing in st.secrets[key]:
                if writing not in all_writings:
                    all_writings.append(writing)

    for i, writing in enumerate(all_writings):
        display_writing(writing, i)
