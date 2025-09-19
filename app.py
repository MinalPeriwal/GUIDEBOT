import streamlit as st
from database import init_database
from auth import show_login_page, logout
from chatbot import bot

# Configure Streamlit page
st.set_page_config(
    page_title="GUIDEBOT",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .user-message {
        background-color: #e3f2fd;
        margin-left: 20%;
        color: #333333;
    }
    .bot-message {
        background-color: #ffffff;
        border: 1px solid #ddd;
        margin-right: 20%;
        color: #333333;
    }
    .stButton > button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

def show_chat_interface():
    """Display the main chatbot interface"""
    # Header with logout button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("🚪 Logout"):
            logout()
    with col2:
        st.markdown("<h1 class='main-header'>🤖 GUIDEBOT</h1>", unsafe_allow_html=True)
    with col3:
        st.write(f"Welcome, {st.session_state.username}!")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "bot", "content": "Hello! I'm GUIDEBOT, your helpful assistant. How can I help you today?"}
        ]
    
    # Display chat messages
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>You:</strong> {message["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message bot-message">
                    <strong>🤖 GUIDEBOT:</strong> {message["content"]}
                </div>
                """, unsafe_allow_html=True)
    
    # Chat input
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([4, 1])
        with col1:
            user_input = st.text_input("Type your message here...", key="user_input")
        with col2:
            send_button = st.form_submit_button("Send 📤")
        
        if send_button and user_input:
            # Add user message
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Get bot response
            bot_response = bot.get_response(user_input)
            st.session_state.messages.append({"role": "bot", "content": bot_response})
            
            st.rerun()

def main():
    """Main application logic"""
    # Initialize database
    init_database()
    
    # Initialize session state
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    
    # Show appropriate interface
    if st.session_state.authenticated:
        show_chat_interface()
    else:
        show_login_page()

if __name__ == "__main__":
    main()