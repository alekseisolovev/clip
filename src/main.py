import streamlit as st

st.set_page_config(layout="wide")

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

st.sidebar.title("Video Playlist")
st.sidebar.markdown("Click on a title below to select the video.")

for title, video_info in playlist.items():
    if st.sidebar.button(title, key=f"btn_{title}", use_container_width=True):
        st.session_state.selected_video_url = video_info["url"]

st.markdown(
    """
    <h1 style='text-align: center;'>Clip</h1>
    <h4 style='text-align: center; color: gray;'>Video Q&A with LLMs</h4>
    """,
    unsafe_allow_html=True,
)

if st.session_state.selected_video_url:
    st.video(st.session_state.selected_video_url)

    st.subheader("Ask a question")
    start_time = st.number_input(
        "Start video at (seconds):", min_value=0, value=0, step=1
    )
    query = st.text_input("Ask a question about the video:", key="query_input")

    if query:
        st.info("Backend logic to process the query and timestamp will go here.")
        st.success(f"You asked: '{query}' starting from {start_time}s.")
else:
    st.info("Please select a video from the playlist on the left to begin.")
