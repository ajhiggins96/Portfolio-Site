import streamlit as st
from streamlit_lottie import st_lottie
import requests
from utils.GPT_utils import ask_bot

st.set_page_config(page_title='Andrew Higgins', layout='centered', page_icon='👤')

# ----- Sidebar -----

with st.sidebar:
    st.markdown(
        """
        # Andrew Higgins
        - Data Scientist (MIDS)  
        - Mechanical Engineer (BSME)  
        - Outdoor enthusiast (YEWW)
        """
    )
    st.image('static/image/profile_pic.jpg', caption="Andrew at a mountain biking & hotdog eating competiton in Salida, CO")
    st.divider()
    st.subheader('Contact me')
    st.html('<a href="mailto:ajhiggins96@gmail.com">ajhiggins96@gmail.com</a>')

# ----- Body -----

# Intro
with st.container():
    st.subheader("Hi, I'm Andrew Higgins 👋")

    st.markdown(
        """
            I'm searching for full-time employment as a **data scientist**, data engineer, or analyst 
            at a company that values **teamwork**, life long **education**, and improving the human condition.  

            Explore the pages in the sidebar to learn more about me, my past work, and my future goals.
        """
    )

# Chat bot
with st.container():
    st.subheader("🤖 Ask my chat bot assistant about me")
    with st.expander("Enter your OpenAI API Key first"):
        st.markdown("Use an existing key or generate one [here](https://platform.openai.com/settings/profile?tab=api-keys).  \nIt will never be saved here, I promise.")
        openai_api_key = st.text_input("Key (starts with 'sk-')", type="password")
        
    user_input = st.text_input("Enter your question:", key="input", placeholder="e.g. What does Andrew like to do for fun?")
    if user_input:
        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key above.', icon='⚠')
        if openai_api_key.startswith('sk-'):
            #st.info(ask_bot(user_input, openai_api_key))
            st.markdown("### ⚠️🚧 Bot Under Construction 🚧⚠️ \nTry again another day.")

# Skills
with st.container():

    # Load a Lottie animation from a URL
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    python_lottie = load_lottieurl("https://lottie.host/244b97c6-ddae-47d6-a092-c2baad1f923d/SdhxUU9dmI.json")
    tensorflow_lottie = load_lottieurl("https://lottie.host/0791394e-d115-4ad6-a06a-e0ff13f66e38/j8ajmaMxSq.json")
    cli_lottie = load_lottieurl("https://lottie.host/f2d1dc72-f28d-4168-afbd-91119f21198b/jrPDqtRibA.json")
    tableau_lottie = load_lottieurl("https://lottie.host/a3f92d0d-c762-4b28-9f70-9dd792e7d059/1hNT9ksFMz.json")
    github_lottie = load_lottieurl("https://lottie.host/de6cf4ef-1233-4d30-a5a3-495804271c21/WraLTdtQ4U.json")
    aws_lottie = load_lottieurl("https://lottie.host/23c8d36f-b577-4985-add8-c0256baa2b24/nNGsS10UQG.json")
    docker_lottie = load_lottieurl("https://lottie.host/6c028fe7-387f-4b45-b05f-f6cd10528c6b/zrKBaeepIf.json")
    ms_lottie = load_lottieurl("https://lottie.host/35c41eff-f14c-4ebb-af82-a92435dbb2e9/NzmQhwdrZ0.json")

    st.subheader('🧰 Skills')

    row0 = st.columns(4)
    with row0[0]:
        st_lottie(python_lottie, height=100)
        st.html('<center style="font-family:monospace">Python</center>')
    with row0[1]:
        st_lottie(tensorflow_lottie, height=100)
        st.html('<center style="font-family:monospace">TensorFlow & Keras</center>')
    with row0[2]:
        st_lottie(tableau_lottie, height=100)
        st.html('<center style="font-family:monospace">Tableau</center>')
    with row0[3]:
        st_lottie(ms_lottie, height=100)
        st.html('<center style="font-family:monospace">Microsoft Office</center>')

    row1 = st.columns(4)
    with row1[0]:
        st_lottie(cli_lottie, height=100)
        st.html('<center style="font-family:monospace">Linux CLI</center>')
    with row1[1]:
        st_lottie(github_lottie, height=100)
        st.html('<center style="font-family:monospace">Github</center>')
    with row1[2]:
        st_lottie(aws_lottie, height=100)
        st.html('<center style="font-family:monospace">AWS</center>')
    with row1[3]:
        st_lottie(docker_lottie, height=100)
        st.html('<center style="font-family:monospace">Docker & Kubernetes</center>')
