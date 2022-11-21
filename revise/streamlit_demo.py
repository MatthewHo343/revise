import streamlit as st
from streamlit_chat import message as st_message
import streamlit.components.v1 as components
import random
import string

from revise.bot import ReviseBot

source_url = ''
iframe = None
source_display = None

### CHAT UPDATED HERE
def getReply():
    user_message = st.session_state.input_text
    history = []
    for chat in st.session_state['history']:
        name = "user" if chat['is_user'] else "bot"
        history.append(f"{name}: {chat['message']}")
    bot.set_chat_history(history)
    reply = bot.answer(user_message)
    print(reply)

    st.session_state.input_text = ''
    st.session_state.history.append({"message": user_message, "is_user": True, "avatar_style": "gridy"})
    st.session_state.history.append({"message": reply, "is_user": False})

if __name__ == "__main__":
    text = ""
    bot = ReviseBot(st.secrets["cohere_api_token"], text)

    st.set_page_config(layout="wide")

    ### CHAT HISTORY SETUP
    if "history" not in st.session_state:
        st.session_state.history = []

    ### MAIN PAGE LAYOUT
    col1, col2 = st.columns(2)
    with st.sidebar:
        st.title("Writing Feedback Generation")
        st.markdown('This is a Cohere API powered contextualized  bot!')
        #used for any extra settings
        with st.expander("Advanced Settings"):
            st.selectbox('Model:', ('xlarge','large'), key="model")
    
    #text
    with col1:
        input = st.text_area(   
                                label='Input your text here',
                                height=500
                            )
        if input:
            bot.set_text(input)

    #chat
    with col2:
        for chat in st.session_state['history']:
            # call random.choices() string module to find the string in Uppercase + numeric data.
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            st_message(**chat, key=ran)  # laying out messages
        st.text_input("",
                      key="input_text",
                      on_change=getReply,
                      placeholder="Ask me a question...like 'what are your thoughts on my writing'")