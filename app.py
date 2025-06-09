import streamlit as st
import requests
import webbrowser
import urllib.parse

st.title("Job Hunt LinkedIn")

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

with st.form(key='chat_form'):
    query = st.text_input("Enter your job search keyword:")
    minutes = st.number_input("Enter time in minutes:", min_value=0, step=1)
    submit_button = st.form_submit_button(label='Send')

if submit_button and query and minutes:
    seconds = int(minutes) * 60
    input_string = str(seconds)
    encoded_query = urllib.parse.quote(query)
    url = (
        f"https://www.linkedin.com/jobs/search-results/"
        f"?f_TPR=r{input_string}"
        f"&keywords={encoded_query}"
        f"&origin=JOBS_HOME_SEARCH_BUTTON"
    )
    webbrowser.open(url)

# Display chat history

# if st.session_state.chat_history:
#     for chat in st.session_state.chat_history:
#         st.write(f"**You 😃:** {chat['user']}")
#         st.write(f"**PMD Bot 🤖:** {chat['bot']}")

