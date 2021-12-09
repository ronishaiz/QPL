import streamlit as st

from qpl_app.multipage import MultiPage
from qpl_app.pages import past_qps, writing_together

app = MultiPage()

st.title('Welcome to the QP Library!')

app.add_page('Past QPs', past_qps.app)
app.add_page('Writing Together', writing_together.app)

app.run()
