import streamlit as st

from qpl_app.multipage import MultiPage
from qpl_app.pages import qp17

app = MultiPage()

st.title('Welcome to the QP Library!')
user_value = st.text_input('Please Enter Password')

if user_value == st.secrets['password']:

    app.add_page('QP #17', qp17.app)

    app.run()
