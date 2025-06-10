import streamlit as st
import requests
import webbrowser
import urllib.parse
import os

st.title("Job Hunt LinkedIn")

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

with st.form(key='chat_form'):
    query = st.text_input("Enter your job search keyword:")
    minutes = st.number_input(
    "Show jobs posted within the last(minutes)",
    min_value=0,
    step=1,
    help="Only display jobs posted within this time window."
)
    submit_button = st.form_submit_button(label='Get linkedIn Link')

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
    st.markdown(f"[Click here to view jobs on LinkedIn]({url})", unsafe_allow_html=True)

# Display chat history

# Persistent page visit counter at the bottom
counter_file = "visit_counter.txt"

def get_counter():
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f:
            f.write("0")
    with open(counter_file, "r") as f:
        return int(f.read())

def increment_counter():
    count = get_counter() + 1
    with open(counter_file, "w") as f:
        f.write(str(count))
    return count

page_visits = increment_counter()
st.markdown(f"<hr><b>Total page visits: {page_visits}</b>", unsafe_allow_html=True)

