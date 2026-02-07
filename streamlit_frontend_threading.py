import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid


# **************************************** utility functions *************************

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

# **************************************** Session Setup *************************

if'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
    




# **************************************** sidebar UI *************************

st.sidebar.title("Langgraph Chatbot")

st.sidebar.button("New Chat")

st.sidebar.header("My Conversations")

st.sidebar.text(st.session_state['thread_id'])


# ******************************************* MAIN UI ***************************

#loading the conversation history from memory
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


# {'role':'user','content':'hi'}
# {'role':'ai','content':'hi'}

user_input = st.chat_input("Type here: ")

if user_input:
    #first add the msg to msg history
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message("user"):
        st.text(user_input)
        
        
    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}
    #first add the msg to msg history
    
    with st.chat_message("ai"):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
            {'messages': [HumanMessage(content=user_input)]},
            config = CONFIG,
            stream_mode='messages'
            )
        )
        
    st.session_state['message_history'].append({'role':'ai','content': ai_message})

