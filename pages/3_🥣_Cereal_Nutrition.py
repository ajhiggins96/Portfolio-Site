import streamlit as st
import streamlit.components.v1 as components

from utils import sidebar, PRIMARY_COLOR


st.set_page_config(page_title='Andrew Higgins - Cereal Nutrition', layout='wide', page_icon='🥣', initial_sidebar_state='auto')

sidebar()

# ----- Body -----

static_dir = "static/cereal/"

st.markdown(
    f"""
    # Cereal Nutrition Data Visualization with <span style='color:{PRIMARY_COLOR}'>Tableau</span>
    *Team project built in 6 weeks for* Data Visualization *course at UC Berkeley, summer 2023.*  

    <sup><sub>This page is not intended for viewing on mobile</sub></sup>
    """,
    unsafe_allow_html=True
)

with st.container(border=True):
    st.markdown(
        """
        ## Project Summary

        The final product is a website comprised of five **interacive** data visualizations that use data from the USDA [National Nutrient Database for Standard Reference](https://data.nal.usda.gov/dataset/composition-foods-raw-processed-prepared-usda-national-nutrient-database-standard-reference-release-28-0).
        The visualizations try to meet the following user questions:
        1. How do the **macronutrients** of different cereal products compare?
        2. What kind of trade-off exists between **calories and sugar** in cereals?
        3. Which brands are a good source of different **micronutrients**?
        4. *How does cow's milk compare to **non-dairy alternatives**?
        5. How to **gluten-free alternatives** compare?

        <sup><sub>*my contribution</sub></sup>
        """, 
        unsafe_allow_html=True
    )

with st.container(border=True):
    st.markdown(
        """
        ## My Contribution

        My team built some great tools to explore cereal nutrition, but I thought 
        
        *You can't have cereal without milk!*
        """
    )
    with open('static/cereal/milk.html', 'r') as f:
        milk_html = f.read()
    components.html(milk_html, height=800)

with st.container(border=True):
    st.markdown(
        """
        ## Team Project Website

        Entirety of the original project site embedded below. Navbar disabled because embedding breaks the links.
        """
    )
    with open('static/cereal/cereal.html', 'r') as f:
        cereal_html = f.read()
    components.html(cereal_html, height=800, scrolling=True)