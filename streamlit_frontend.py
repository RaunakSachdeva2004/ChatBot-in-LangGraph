import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage


CONFIG = {'configurable': {'thread_id': 'thread-1'}}

#st.session_state -> dict ->

if'message_history' not in st.session_state:
    st.session_state['message_history'] = []


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
        
    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)

    ai_message = response['messages'][-1].content
    #first add the msg to msg history
    st.session_state['message_history'].append({'role':'ai','content': ai_message})
    with st.chat_message("ai"):
        st.text(ai_message)

