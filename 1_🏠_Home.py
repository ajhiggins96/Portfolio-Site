import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Andrew Higgins - Home", layout='centered', page_icon='👤')

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
    st.image('static/image/profile_pic.png', caption="Andrew at a mountain biking & hotdog eating competiton in Salida, CO")
    row0 = st.columns([0.1, 0.9])
    with row0[0]:
        st.image('https://mailmeteor.com/logos/assets/PNG/Gmail_Logo_512px.png', width=25)
    with row0[1]:
        st.html('<a href="mailto:ajhiggins96@gmail.com">ajhiggins96@gmail.com</a>')
    row1 = st.columns([0.1, 0.9])
    with row1[0]:
        st.image('https://camo.githubusercontent.com/dfe7e80288901f8d5e8de7562d6f94491e2a7f8042316fd544fe3b6364b63783/68747470733a2f2f69636f6e2d6c6962726172792e636f6d2f696d616765732f6769746875622d69636f6e2d77686974652f6769746875622d69636f6e2d77686974652d362e6a7067', width=25)
    with row1[1]:
        st.link_button(label='website source', url='https://github.com/ajhiggins96/Portfolio-Site/tree/main')

# ----- Body -----

primary_color = st.get_option('theme.primaryColor')
static_dir = 'static/home/'

# Intro
with st.container():
    st.markdown(
        f"""
            # 👋 Hi, I'm Andrew Higgins
            
            #### I'm a <span style='color:{primary_color}'>Data Scientist and Engineer</span> seeking a role at a company that values the names and faces behind the numbers.  
            
            Before completing my **Master of Information and Data Science** degree at UC Berkeley, I began my career as an **Additive Manufacturing Engineer** at Visser Precision LLC.
            I was quickly promoted to **Department Manager** of all metal 3D Printing operations. 
            For undergrad, I received a BS in Mechanical Engineering from the University of Denver, during which I also worked a couple of full-time internships.   

            ⬅️ Explore the pages in the sidebar to learn more about me, my past work, and my future goals.
        """,
        unsafe_allow_html=True
    )
    st.link_button('📄 Resume', '/About_me?tab=Resume', type='primary')

st.divider()

# Projects
with st.container(border=False):
    st.markdown("### 📊 Data Science Projects")
    cols = st.columns(4)
    with cols[0]:
        if st.button('End-to-end', use_container_width=True):
            st.switch_page('pages/2_☀️_SkinScreen.py')
        st.markdown("**SkinScreen**: deep learning image classification product")
        st.image(static_dir + 'skinscreen.png')
    with cols[1]:
        if st.button('Data Visualization', use_container_width=True):
            st.switch_page('pages/3_🥣_Cereal_Nutrition.py')
        st.markdown("Interactive Tableau visualizations with nutrition data")
        st.image(static_dir + 'datavis.png')
    with cols[2]:
        if st.button("Data Engineering", use_container_width=True):
            st.switch_page("pages/4_☁️_Machine_Learning_API.py")
        st.markdown("Robust & scalable ML endpoint deployment in Azure cloud")
        st.image(static_dir + 'mlapi.png')
    with cols[3]:
        if st.button("Large Lang. Models", use_container_width=True):
            st.switch_page("pages/5_💬_BoolQ_NLP_Research.py")
        st.markdown("NLP research comparing T5 and BERT to a SotA Google model")
        st.image(static_dir + 'nlp.png')
        
st.divider()

# Skills
with st.container(border=False):
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

    st.markdown('### 🧰 Skills')

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
