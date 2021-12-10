import streamlit as st

from qpl_app.pages.page_utils import get_all_text_from_qp


def app():

    st.header("QP #17")
    get_all_text_from_qp(17)
