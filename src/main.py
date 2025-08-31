import streamlit as st

st.set_page_config(layout="centered")

st.markdown(
    """
    <h1 style='text-align: center;'>Clip</h1>
    <h4 style='text-align: center; color: gray;'>Video Q&A with LLMs</h4>
""",
    unsafe_allow_html=True,
)

video_url = "https://youtu.be/1ntIL1jYTlc"

start_time = st.number_input("Start video at (seconds):", min_value=0, value=0, step=1)

st.video(video_url, start_time=start_time)

query = st.text_input("Ask a question about the video:")

if query:
    st.info("Backend logic to process the query will go here.")
    st.success(f"You asked: {query}")
