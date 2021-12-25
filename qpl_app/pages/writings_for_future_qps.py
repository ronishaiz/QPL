
import streamlit as st


def app():

    secret_name = 'future_writings'

    user_value = st.text_area('Enter new writing')
    if user_value:
        st.secrets[secret_name].append(user_value)

    st.subheader('Delete Writing')

    to_delete = st.selectbox('select index of writing to delete', [i for i in range(len(st.secrets[secret_name]))])

    if st.button('Remove Writing'):
        st.secrets[secret_name].remove(st.secrets[secret_name][to_delete])

    for i, writing in enumerate(st.secrets[secret_name]):
        display_writing(writing, i)


# TODO: solve import error and use display writing from page utils
def display_writing(text: str, i: int = None):
    if i is not None:
        st.subheader(str(i))
    split_out = text.split('\n')
    for line in split_out:
        text = f'<p style="font-family:Arial; font-size: 16px;">{line}</p>'
        st.markdown(text, unsafe_allow_html=True)
