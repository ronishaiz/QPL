import os
import glob
import streamlit as st


def app():
    st.header('Writings From Past QPs')

    st.header('QP #17')

    read_all_text(17)


def read_all_text(qp_num: int):

    data_folder = os.path.join('qpl_app', 'data')
    qp_folder = os.path.join(data_folder, 'past_qps', f'qp{qp_num}')
    files = glob.glob(os.path.join(qp_folder, '*.txt'))

    if len(files) == 0:
        raise Exception(f'did not find any text files in {qp_folder} folder')

    text_header_to_text = {}

    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            text_lines = f.readlines()
        text_header_to_text[os.path.basename(file).replace('.txt', '')] = text_lines

    for key in text_header_to_text:
        st.subheader(key)
        text_lines = text_header_to_text[key]
        for line in text_lines:
            text = f'<p style="font-family:Arial; font-size: 16px;">{line}</p>'
            st.markdown(text, unsafe_allow_html=True)
