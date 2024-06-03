import streamlit as st
import streamlit_timeline as timeline
import base64

st.set_page_config(page_title='Andrew Higgins - About', layout='wide', page_icon='👤', initial_sidebar_state='auto')

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
        st.html('<a href="https://github.com/ajhiggins96/Portfolio-Site">website source</a>')

# ----- Body -----

primary_color = st.get_option('theme.primaryColor')

tab_names = ['Timeline Overview', 'Experience', 'Education', 'Hobbies', 'Resume']
overview, experience, education, hobbies, resume = st.tabs(tab_names)

with overview:
    st.markdown(
       f"""
        ### I am a Mechanical Engineer turned <span style='color:{primary_color}'>Data Scientist</span> based in Denver, Colorado.  
        Check out the timeline below for a brief history of my education and career journey.
        """,
        unsafe_allow_html=True
    )
    with open("static/timeline/timeline.json", 'r') as f:
        data = f.read()
    timeline.timeline(data, height=700)

with experience:
    datasci, engineering = st.tabs(['Data Science', 'Mechanical Engieering'])

    with datasci:
        st.markdown("## ⚠️🚧 Under Construction 🚧⚠️")

    with engineering:
        st.markdown("## ⚠️🚧 Under Construction 🚧⚠️")


with education:
    st.markdown("## ⚠️🚧 Under Construction 🚧⚠️")

with hobbies:
    st.markdown("## ⚠️🚧 Under Construction 🚧⚠️")

with resume:
    # Download button
    with open("static/resume.pdf", "rb") as file:
        st.download_button(
            label="⬇️ Download PDF",
            data=file,
            file_name="Andrew_J_Higgins_Resume.pdf",
            type='primary'
        )

    # Opening file from file path
    with open("static/resume.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display =  f"""<embed
    class="pdfobject"
    type="application/pdf"
    title="Embedded PDF"
    src="data:application/pdf;base64,{base64_pdf}"
    style="overflow: auto; width: 100%; height: 80vh;">"""

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

    

# Handling query params
query_params = st.query_params
if 'tab' in query_params.keys():
    tab_index = tab_names.index(query_params['tab'])
    st.components.v1.html(
        f"""
        <script>
            var tab = window.parent.document.getElementById('tabs-bui3-tab-{tab_index}');
            tab.click()
        </script>
        """
    )
st.query_params.clear()