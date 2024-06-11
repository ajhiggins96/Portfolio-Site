import streamlit as st
import streamlit_timeline as timeline
import streamlit.components.v1 as components

from utils import sidebar, display_pdf, PRIMARY_COLOR


st.set_page_config(page_title='Andrew Higgins - About', layout='wide', page_icon='👤', initial_sidebar_state='auto')

sidebar()

# ----- Body -----

tab_names = ['Career Timeline', 'Hobbies', 'Resume']
career_timeline, hobbies, resume = st.tabs(tab_names)

with career_timeline:
    st.markdown(
       f"""
        ### I am a Mechanical Engineer turned <span style='color:{PRIMARY_COLOR}'>Data Scientist</span> based in Denver, Colorado.  
        Check out the timeline below for a brief history of my education and career journey.
        """,
        unsafe_allow_html=True
    )
    with open("static/timeline/timeline.json", 'r') as f:
        data = f.read()
    timeline.timeline(data, height=700)

with hobbies:
    st.markdown("## Skiing is my passion")
    cols = st.columns(4)
    with cols[0]:
        st.image('static/hobbies/babyski.jpg', caption='Skiing before I was running')
    with cols[1]:
        st.image('static/hobbies/bross.JPG', caption="Hiking and skiing Mount Bross, CO (14,178')")
    with cols[2]:
        st.image('static/hobbies/alps.jpeg', caption='A trip to the alps for the best skiing of my life.')
    with cols[3]:
        st.video('static/hobbies/crash_reel.mp4', autoplay=True, muted=True)
        st.caption("Crash reel 2024. If you're not falling you're not trying")

    st.markdown("## Being outdoors rejuvinates me")
    cols = st.columns(4)
    with cols[0]:
        st.image('static/hobbies/bike.jpg', caption='Mountain biking: it almost fills the hole in my heart left by skiing each year')
    with cols[1]:
        st.image('static/hobbies/raft.jpg', caption="River rafting in CO and UT")
    with cols[2]:
        st.image('static/hobbies/backpacking.jpeg', caption="Backpacking: it's just camping with extra steps")
    with cols[3]:
        st.image('static/hobbies/triathlon.jpeg', caption='Testing my limits at events like the Yosemite Bass Lake Triathlon')

    st.markdown(
        """
        ## Travel and adventure teach me about the world
        In 2018, I walked 525 miles across Spain on the Camino de Santiago.
        """
    )
    cols = st.columns(4)
    with cols[0]:
        st.image('static/hobbies/camino_start.jpeg', caption='Starting off over 500 miles from my destination')
    with cols[1]:
        st.image('static/hobbies/locals.jpg', caption='Meeting and learning from locals')
    with cols[2]:
        st.image('static/hobbies/santiago.jpg', caption='Making friends from around the world')
    with cols[3]:
        st.image('static/hobbies/fisterra.jpg', caption='Reaching the Atlantic after 32 life-changing days')

with resume:
    # Download button
    with open("static/resume.pdf", "rb") as file:
        st.download_button(
            label="⬇️ Download PDF",
            data=file,
            file_name="Andrew_J_Higgins_Resume.pdf",
            type='primary'
        )

    display_pdf("https://drive.google.com/file/d/1WmSoi2qe4FSfGmJ22V27BUu4Jqk5C6tI/preview")

    

# Handling query params
query_params = st.query_params
if 'tab' in query_params.keys():
    tab_index = tab_names.index(query_params['tab'])
    components.html(
        f"""
        <script>
            var tab = window.parent.document.getElementById('tabs-bui3-tab-{tab_index}');
            tab.click()
        </script>
        """
    )
st.query_params.clear()