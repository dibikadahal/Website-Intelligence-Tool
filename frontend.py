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


#------------Button click---------------------
if analyze:
    if not url:
        st.warning("Please enter a URL first")
    else:
        #add https:// if the user forgot about it
        if not url.startswith("http"):
            url = "https://" + url

        with st.spinner("Analyzing website..."):
            try:
                response=requests.get(
                    "http://127.0.0.1:8000/inspect",
                    params={"url": url},
                    timeout=10
                )
                data=response.json()

                #-------networking results----------------
                st.subheader("🌐 Network Information")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Status Code", data.get("status_code", "N/A"))

                with col2:
                    st.metric("Response Time", f"{data.get('response_time_ms', 'N/A')} ms")

                with col3:
                    https = data.get("https", False)
                    st.metric("HTTPS", "✅ Secure" if https else "❌ Not Secure")

                st.divider()

                col4, col5 = st.columns(2)

                with col4:
                    st.markdown("**🌍 Domain**")
                    st.code(data.get("domain", "N/A"))

                    st.markdown("**🖥 Server**")
                    st.code(data.get("server", "N/A"))

                with col5:
                    st.markdown("**📍 IP Address**")
                    st.code(data.get("ip_address", "N/A"))

                    st.markdown("**📄 Content Type**")
                    st.code(data.get("content_type", "N/A"))

                st.divider()


                #-------AI Summary----------------
                st.subheader("🤖 AI Summary")
                summary = data.get("ai_summary", "No summary available")
                st.info(summary)

                st.divider()

                #-------Raw JSON (Expandable)------------
                with st.expandable("📦 View Raw JSON Response"):
                    st.json(data)

            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to backend. Make sure your FASTAPI is running on port 8000")
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")


#-----------Footer----------------
st.divider()
st.caption("Built with Fast API + Gemini 2.5 + Streamlit")


