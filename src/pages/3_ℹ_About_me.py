import streamlit as st
import streamlit_timeline as timeline
import base64

st.set_page_config(page_title='About Andrew', layout='wide', page_icon='👤', initial_sidebar_state='auto')

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
    st.markdown('## Contact me')
    st.html('<a href="mailto:ajhiggins96@gmail.com">ajhiggins96@gmail.com</a>')

# ----- Body -----

primary_color = st.get_option('theme.primaryColor')

tab_names = ['Timeline Overview', 'Experience', 'Education', 'Hobbies', 'Resume']
overview, experience, education, hobbies, resume = st.tabs(tab_names)

with overview:
    st.html(
       f"""
        <h3>I am a Mechanical Engineer turned <span style='color:{primary_color}'>Data Scientist</span> based in Denver, Colorado.</h3>  
        <p>Check out the timeline below for a brief history of my education and career journey.</p>
        """
    )
    with open("static/timeline/timeline.json", 'r') as f:
        data = f.read()
    timeline.timeline(data)

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