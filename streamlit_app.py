import streamlit as st

from qpl_app.multipage import MultiPage
from qpl_app.pages import qp5, qp6, qp7, qp8, qp9, qp10, qp11, qp12, qp13, qp14, qp15, qp16, qp17, qp18, qp19, qp20, \
    qp21, qp22, qp23, all_writings, writings_for_future_qps

app = MultiPage()

st.title('Welcome to the QP Library!')
user_value = st.text_input('Please Enter Password')

if user_value == st.secrets['password']:

    all_qps = [(5, qp5), (6, qp6), (7, qp7), (8, qp8), (9, qp9), (10, qp10), (11, qp11), (12, qp12),
               (13, qp13), (14, qp14), (15, qp15), (16, qp16), (17, qp17), (18, qp18), (19, qp19), (20, qp20),
               (21, qp21), (22, qp22), (23, qp23)]

    for num, qp in all_qps:
        app.add_page(f'QP #{num}', qp.app)

    app.add_page('All Writings', all_writings.app)
    # app.add_page('Writings for Future QPs', writings_for_future_qps.app)

    app.run()
