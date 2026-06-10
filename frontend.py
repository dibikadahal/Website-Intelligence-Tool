import streamlit.st
import requests

#---------Page Config setup---------------
st.set_page_config(
    page_title="Website Intelligence Tool",
    page_icon="🕵️‍♂️",
    layout="centered"
)

#-----------Header--------------
st.title("🕵️‍♂️ Website Intelligence Tool")
st.markdown("Paste any URL to get a complete technical and AI-Powereed analysis")
st.divider()


#-----------Input----------------------
url = st.text_input(
    "Enter a URL",
    placeholder="https://github.com",
)

analyze = st.button("🔍 Analyze Website", use_container_width=True)

