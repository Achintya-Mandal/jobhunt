import streamlit as st
import requests
import webbrowser

st.title("PMD Functional Chatbot")

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

with st.form(key='chat_form'):
    input_string = st.text_input("Enter your query :")
    submit_button = st.form_submit_button(label='Send')

if submit_button and input_string:
    url = "https://www.linkedin.com"
    webbrowser.open(url)
#     backend_api = "https://synonyms_service-sleepy-warthog-hg.cfapps.eu12.hana.ondemand.com/synonym_query?input_string=" + input_string
#     response = requests.get(
#         backend_api,
#         #params={"message": input_string},  # Use 'params' for GET requests
#         verify=False  # Disable SSL verification
#     )
#     if response.status_code == 200:
#         try:
#             # Handle plain text response
#             response_message = response.text.strip()  # Use response.text instead of response.json()
#             if response_message:
#                 # Append user input and response to chat history
#                 st.session_state.chat_history.append({"user": input_string, "bot": response_message})
#             else:
#                 st.write("Error: Empty response from the server.")
#         except Exception as e:
#             st.write("Error: Unable to process the response.")
#             st.write(f"Exception: {e}")
#     else:
#         st.write(f"Error: {response.status_code} - {response.reason}")
#         st.write("Response content:", response.text)

# Display chat history

if st.session_state.chat_history:
    for chat in st.session_state.chat_history:
        st.write(f"**You 😃:** {chat['user']}")
        st.write(f"**PMD Bot 🤖:** {chat['bot']}")

