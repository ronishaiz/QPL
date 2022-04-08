import streamlit as st
from streamlit_player import st_player


def qp_page_app(qp_num: int, songs_played_daria: list = None, songs_played_roni: list = None, comment: str = None):
    st.header(f"QP #{qp_num}")

    if comment:
        st.subheader(comment)

    audio_secret_name = f'QP{qp_num}_audio'
    if audio_secret_name in st.secrets:
        st.audio(st.secrets[audio_secret_name])

    if songs_played_daria:
        st.subheader("Songs Played By Daria")
        for song in songs_played_daria:
            text = f'<p style="font-family:Arial; font-size: 16px;">{song}</p>'
            st.markdown(text, unsafe_allow_html=True)

    if songs_played_daria:
        st.subheader("Songs Played By Roni")
        for song in songs_played_roni:
            text = f'<p style="font-family:Arial; font-size: 16px;">{song}</p>'
            st.markdown(text, unsafe_allow_html=True)

    st.subheader("Writings Read")
    get_all_text_from_qp(qp_num)


def get_all_text_from_qp(qp_num: int):
    secret_name = f'QP{qp_num}'
    all_texts = st.secrets[secret_name]
    for i in range(len(all_texts)):
        text = all_texts[i]
        display_writing(text, i)


def display_writing(text: str, i: int = None):
    if i is not None:
        st.subheader(str(i))
    split_out = text.split('\n')
    for line in split_out:
        text = f'<p style="font-family:Arial; font-size: 16px;">{line}</p>'
        st.markdown(text, unsafe_allow_html=True)
