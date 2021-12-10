import streamlit as st


def get_all_text_from_qp(qp_num: int):
    secret_name = f'QP{qp_num}'
    all_texts = st.secrets[secret_name]
    for i in range(len(all_texts)):
        st.subheader(str(i))
        text = all_texts[i]
        split_out = text.split('\n')
        for line in split_out:
            text = f'<p style="font-family:Arial; font-size: 16px;">{line}</p>'
            st.markdown(text, unsafe_allow_html=True)