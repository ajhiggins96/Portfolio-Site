import streamlit as st
import streamlit_timeline as timeline

st.set_page_config(page_title='About Andrew', layout="wide", page_icon='👤')

# ----- Sidebar -----

st.sidebar.markdown(
    """
    # Andrew Higgins
    - Data Scientist (MIDS)  
    - Mechanical Engineer (BSME)  
    - Outdoor enthusiast (HUCKYEAH)
    """
)
st.sidebar.image('static/image/profile_pic.jpg', caption="Andrew at a mountain biking & hotdog eating competiton in Salida, CO")
st.sidebar.divider()
st.sidebar.markdown("## Contact me")
st.sidebar.html("<a href='mailto:ajhiggins96@gmail.com'>ajhiggins96@gmail.com</a>")

# ----- Body -----

overview, experience, education, hobbies, resume = st.tabs(['Overview', 'Experience', 'Education', 'Hobbies', 'Resume'])

with overview:
    with open('static/json/timeline.json', 'r') as f:
        data = f.read()
    timeline.timeline(data)
