import os
import glob
import streamlit as st


def app():
    st.header('Writings From Past QPs')

    st.header('QP #17')

    read_text_from_secrets('museum')


def read_text_from_secrets(secret_name: str):
    text: str = st.secrets[secret_name]
    split_out = text.split('\n')
    for line in split_out:
        text = f'<p style="font-family:Arial; font-size: 16px;">{line}</p>'
        st.markdown(text, unsafe_allow_html=True)
