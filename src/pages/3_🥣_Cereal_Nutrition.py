import streamlit as st

st.set_page_config(page_title='Cereal Nutrition', layout='wide', page_icon='🥣', initial_sidebar_state='auto')

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
static_dir = "static/cereal/"


st.markdown(
    f"""
    # Cereal Nutrition Data Visualization with <span style='color:{primary_color}'>Tableau</span>
    *Built in 14 weeks for UC Berkelery Data Visualization course, summer 2023.*
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
    st.components.v1.html(milk_html, height=800)

with st.container(border=True):
    st.markdown(
        """
        ## Team Project Website

        Entirety of the original project site embedded below. Navbar disabled becuase embedding breaks the links.
        """
    )
    with open('static/cereal/cereal.html', 'r') as f:
        cereal_html = f.read()
    st.components.v1.html(cereal_html, height=800, scrolling=True)