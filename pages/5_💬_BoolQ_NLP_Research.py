import streamlit as st
import base64

st.set_page_config(page_title="Andrew Higgins - ML API Project", layout='wide', page_icon='☁️')

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
static_dir = "static/nlp/"

st.markdown(
    f"""
    # True/False Question Answering: Comparing simple transformers with state-of-the-art mega-models
    *Solo research project completed in 3 weeks for* Natural Language Processing *course at UC Berkeley, summer 2023*
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    ## Abstract

    Extractive closed-domain question answering tasks in natural language processing involve the
    reading comprehension of a passage of text so that a question may be answered about it. This
    paper explores a sub-category of such tasks: boolean, or yes/no, question answering. <span style='color:{primary_color}'>Models
    BERT and T5 and some of their pre-trained variants are compared with the state-of-the-art,
    ST-MoE from Google</span>. Results show that pretraining BERT is able to marginally improve its
    performance, but the biggest success comes from a variant of T5 trained specifically for boolean
    question answering.
    """,
    unsafe_allow_html=True
)

# def display_pdf(path):
#     # Opening pdf report from file path
#     with open(path, 'rb') as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')

#     # Embedding PDF in HTML
#     pdf_display =  f"""<embed
#         class="pdfobject"
#         type="application/pdf"
#         title="Embedded PDF"
#         src="data:application/pdf;base64,{base64_pdf}"
#         style="overflow: auto; width: 100%; height: 80vh;">
#     """

#     # Displaying File
#     st.markdown(pdf_display, unsafe_allow_html=True)

def display_pdf(url):
    # Opening pdf report from file path

    pdf_display =  f"""<embed 
        src="{url}" 
        style="overflow: auto; width: 100%; height: 80vh;" 
        allow="autoplay">
    """

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

st.markdown("## Slide Deck")
display_pdf("https://drive.google.com/file/d/1r7nxuHq7t5WfYe25mDH0h0zp14Li13CH/preview?usp=sharing")

st.markdown("## Complete Paper")
display_pdf(static_dir + 'NLP_report.pdf')

st.markdown('## Jupyter notebook')
with open(static_dir + 'NLP_code.html', 'rb') as f:
    jupyter_html = f.read()
st.components.v1.html(jupyter_html, height=800, scrolling=True)