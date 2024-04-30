import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title='Andrew Higgins', layout="centered", page_icon='👤')

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

home, tacos, project = st.tabs(['home', 'tacos', 'project'])

with tacos:
    tacos = 'this is text about tacos'
    tacos

with home:
    'hello world'

with project:
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_data)

    