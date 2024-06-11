import streamlit as st


def display_pdf(url: str):
    """Render a GDrive PDF file in an embedded frame. 
    Sharing options must be set to "anyone with the link can view".
    
    url: string. Replace /view... with /preview after pasting.
    """

    pdf_html =  f"""<embed 
        src="{url}" 
        style="overflow: auto; width: 100%; height: 80vh;" 
        allow="autoplay">
    """

    st.markdown(pdf_html, unsafe_allow_html=True)