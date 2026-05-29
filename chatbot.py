from dotenv import load_dotenv
import streamlit as st 
from langchain_groq import ChatGroq

#Loading environment variables from .env file 
load_dotenv()

# Setting up the Streamlit UI page 
st.set_page_config( 
    page_title="Generative AI Chatbot", 
    page_icon = "❗",
    layout="centered"
)

st.title("ChatX - Get Started! ")

#Best thing about Streamlit UI is that it allows a dyanamic interface for user input without specifying a lot of things 




#init a chat history in a session state of Streamlit UI 
if "chat_history" not in st.session_state: 
    st.session_state.chat_history = []


#showing chat history in the UI 
for chat in st.session_state.chat_history: 
    with st.chat_message(chat['role']): 
        st.markdown(chat['content']) # this is all for styling and formatting the blocks of chat messages

        
#defining the model 
llm = ChatGroq( 
    model = "llama-3.1-8b-instant",
    temperature = 0.0, 
    
)

user_prompt = st.chat_input("Ask Chatbot...")

#in this we are considering a valid input that is given by the user when they hit the enter button or press enter 
#We use the strucure of the chat where chat_message defines the role here and markdown the content of the message 
if user_prompt: 
    st.chat_message("user").markdown(user_prompt)

    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    #tracking the response
    response = llm.invoke (
        input = [{"role": "system", "content": "You are a helpful AI Assistant."}, *st.session_state.chat_history ]
    )

    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})


    #Adding it to the showing in chat hisory UI code block 
    with st.chat_message("assistant"): 
        st.markdown(assistant_response)


