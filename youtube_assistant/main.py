import streamlit as st
import langchain_helper as lch
import textwrap

st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_uri = st.sidebar.text_area(label="What is the Youtube video URL?",
                                           max_chars=50)
        query = st.sidebar.text_area(label="Ask me about the video?", 
                                     max_chars=50, 
                                     key="query")
        submit_button = st.form_submit_button(label="Submit")

if youtube_uri and query:
    db = lch.create_vector_db_from_youtube(youtube_uri)
    response =lch.get_response_from_query(db, query, 4)
    st.header("Answer: ")
    st.text(textwrap.fill(response, width=80))