import streamlit as st
import streamlit.components.v1 as components


PRIMARY_COLOR = st.get_option('theme.primaryColor')
TEXT_COLOR = st.get_option('theme.textColor')


def sidebar() -> None:
    """Render sidebar."""
    
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


def display_pdf(url: str) -> None:
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


def display_mermaid(code: str, height: int=500, primary_text_color: str=TEXT_COLOR) -> None:
    """Render a mermaid flow diagram in an html frame.
    
    code: string. Mermaid formatted text of the diagram."""
    
    components.html(
        f"""
        <pre class="mermaid">
            %%{{
            init: {{
                'theme': 'base',
                'themeVariables': {{
                    'primaryColor': '{PRIMARY_COLOR}',
                    'primaryTextColor': '{primary_text_color}',
                    'primaryBorderColor': '{TEXT_COLOR}',
                    'lineColor': '{TEXT_COLOR}',
                    'secondaryColor': '{PRIMARY_COLOR}',
                    'tertiaryColor': '#ffffff'
                }}
            }}
            }}%%
            {code}
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        height=height,
        scrolling=True
    )