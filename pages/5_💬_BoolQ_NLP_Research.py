import streamlit as st
import streamlit.components.v1 as components

from utils import sidebar, display_pdf, PRIMARY_COLOR


st.set_page_config(page_title="Andrew Higgins - ML API Project", layout='wide', page_icon='☁️')

sidebar()

# ----- Body -----

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
    paper explores a sub-category of such tasks: boolean, or yes/no, question answering. <span style='color:{PRIMARY_COLOR}'>Models
    BERT and T5 and some of their pre-trained variants are compared with the state-of-the-art,
    ST-MoE from Google</span>. Results show that pretraining BERT is able to marginally improve its
    performance, but the biggest success comes from a variant of T5 trained specifically for boolean
    question answering.
    """,
    unsafe_allow_html=True
)

st.markdown("## Slide Deck")
display_pdf("https://drive.google.com/file/d/1r7nxuHq7t5WfYe25mDH0h0zp14Li13CH/preview")

st.markdown("## Complete Paper")
display_pdf("https://drive.google.com/file/d/14CgmFl9LA_ghNJsAubfBLByQd-4ZPmga/preview")

st.markdown('## Jupyter notebook')
with open(static_dir + 'NLP_code.html', 'rb') as f:
    jupyter_html = f.read()
components.html(jupyter_html, height=800, scrolling=True)