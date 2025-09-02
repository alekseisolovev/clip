import streamlit as st
from langchain.schema import AIMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(layout="wide")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

playlist = {
    "Siemens ET200SP hardware assembly, connection to PLC and TIA configuration": {
        "url": "https://www.youtube.com/watch?v=4kI16VLmBJw"
    },
    "Installation guide video of automatic industrial insulated overhead sectional doors": {
        "url": "https://youtu.be/1ntIL1jYTlc"
    },
}

if "selected_video_url" not in st.session_state:
    st.session_state.selected_video_url = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.sidebar.title("Video Playlist")
st.sidebar.markdown("Click on a title below to select the video.")

for title, video_info in playlist.items():
    if st.sidebar.button(title, key=f"btn_{title}", use_container_width=True):
        st.session_state.selected_video_url = video_info["url"]
        st.session_state.chat_history = []

st.markdown(
    """
    <h1 style='text-align: center;'>Clip</h1>
    <h4 style='text-align: center; color: gray;'>Video Q&A with LLMs</h4>
    """,
    unsafe_allow_html=True,
)

if st.session_state.selected_video_url:

    st.video(st.session_state.selected_video_url)

    for message in st.session_state.chat_history:
        role = "Human" if isinstance(message, HumanMessage) else "AI"
        with st.chat_message(role):
            st.markdown(message.content)

    user_prompt = st.chat_input("Ask Gemini anything about the video...")
    if user_prompt:
        st.session_state.chat_history.append(HumanMessage(content=user_prompt))
        with st.chat_message("Human"):
            st.markdown(user_prompt)

        with st.chat_message("AI"):
            with st.spinner("Thinking..."):
                response = model.invoke(st.session_state.chat_history)
                st.session_state.chat_history.append(
                    AIMessage(content=response.content)
                )
                st.markdown(response.content)
