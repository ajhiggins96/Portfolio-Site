import streamlit as st

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
static_dir = "static/skinscreen/"

st.html(f"<h1><span style='color:{primary_color}'>SkinScreen</span>: Your Go-to Skin Health Monitoring Website</h1><em>Built in 14 weeks for UC Berkelery MIDS Final Capstone course, spring 2024.</em>")

st.markdown(
    """
    ## Product Summary

    SkinScreen is a fully end-to-end Machine Learning product. The web app's function to classify user skin conditions with computer vision technology. 
    The website allows users to upload a photo of their skin lesion, and the app returns a preliminary diagnosis, a confidence interval, and additional information about the skin condition.
    """
)

st.markdown("## Product Demo")
st.video("https://youtu.be/RPZF8f-keVc")

st.markdown("## Project plan and execution")

with st.container(border=True):
    st.markdown("### Tech Stack")

    cols = st.columns(7)
    with cols[0]:
        st.image(static_dir + 'python.png', caption='Python', use_column_width='always')
    with cols[1]:
        st.image(static_dir + 'tensorflow.png', caption='TensorFlow', use_column_width='always')
    with cols[2]:
        st.image(static_dir + 'fastapi.png', caption='FastAPI', use_column_width='always')
    with cols[3]:
        st.image(static_dir + 'aws.png', caption='AWS', use_column_width='always')
    with cols[4]:
        st.image(static_dir + 'sagemaker.png', caption='Amazon SageMaker', use_column_width='always')
    with cols[5]:
        st.image(static_dir + 'lightsail.png', caption='Amazon Ligthsail', use_column_width='always')
    with cols[6]:
        st.image(static_dir + 'html.png', caption='HTML & CSS', use_column_width='always')
   
with st.container(border=True):
    st.markdown(
        """
        ### Training Data

        **58,000** training and **19,000** testing images originally curated by the [International Skin Imaging Collaboration (ISIC)](https://challenge.isic-archive.com/data/#2019).

        Union of 2019 and 2020 Challenge datasets. Images belong to 10 different classes, and the 6 classes with the highest cardinality were ultimately used.
        """
    )
    cols = st.columns([0.6, 0.4])
    with cols[0]:
        st.image(static_dir + 'class_dist.png', caption='Class distribution')
    with cols[1]:
        st.image(static_dir + 'class_counts.png')

with st.container(border=True):
    st.markdown("### Model Training and Evaluation")
    cols = st.columns([0.4, 0.6])
    with cols[0]:
        st.markdown("Multiple state-of-the-art image feature extraction models were tested against each other in Amazon SageMaker training instances for performance on the dataset and classification task.")
    with cols[1]:
        st.image(static_dir + 'model_comparison.png')

with st.container(border=True):
    st.markdown("### Final Model Architecture")
    cols = st.columns([0.5, 0.5])
    with cols[0]:
        st.markdown(
            """
            **DenseNet201** base model was selected as the base for the transfer learning architecture. 
            
            Dropout, fully connected, and softmax classification layers added to the head.

            Layers on the left side of the diagram are image pre-processing layers, to make image data compatible with DenseNet.
            """
        )
    with cols[1]:
        st.image(static_dir + 'model_architecture.png')

with st.container(border=True):
    st.markdown("### Web App Data Pipeline")
    st.image(static_dir + 'pipeline.png')
    st.markdown(
        """
        1. User navigates to the /classifier endpoint.
        2. GET call invoked. Site HTML and CSS is returned and rendered.
        3. User uploads skin lesion image to HTML form and clicks submit.
        4. POST call invoked on /predict endpoint. SageMaker API client sends image data to SageMaker model endpoint.
        5. Image is resized, preprocessed, and passed to classification model.
        6. Model inference results are returned to REST API.
        7. Results are parsed and passed to /classifier endpoint as URL querystring parameters.
        8. GET call invoked with query params. HTML template renders relevant user results and further information.
        """
    )

with st.container(border=True):
    st.markdown("## The Team")
    cols = st.columns(4)
    with cols[0]:
        st.image('https://media.licdn.com/dms/image/C4E03AQFzCRhgz0tcYA/profile-displayphoto-shrink_400_400/0/1567871997956?e=1722470400&v=beta&t=4QKUHffhw4OdClYagloN6NM8CDtNJRkYttiBOy1noTE')
        st.html(
            """
            <h5 style="text-align: center;"><a href="https://www.linkedin.com/in/phillipsrachael/">Rachael Phillips</a></h5>
            <ul style="text-align: center;  list-style-position: inside;">
                <li>Project Manager</li>
                <br>
            </ul>
            """
        )
    with cols[1]:
        st.image('https://media.licdn.com/dms/image/C5603AQErfWUMsVwzyw/profile-displayphoto-shrink_400_400/0/1517433496012?e=1722470400&v=beta&t=YmFiezlT53ubPz-r_q0FeATPrPSA0MySw9eCUM8lCvQ')
        st.html(
            """
            <h5 style="text-align: center;"><a href="https://www.linkedin.com/in/andrew-j-higgins/">Andrew Higgins</a></h5>
            <ul style="text-align: center;  list-style-position: inside;">
                <li>Systems Engineer</li>
                <li>Data Scientist</li>
            </ul>
            """
        )
    with cols[2]:
        st.image('https://media.licdn.com/dms/image/C4D03AQE9whu4bj_3TQ/profile-displayphoto-shrink_800_800/0/1516904716045?e=1722470400&v=beta&t=UKsqyqbON33ty2ZaiHjgORZD8YkIaQlsJZelEgg2K58')
        st.html(
            """
            <h5 style="text-align: center;"><a href="https://www.linkedin.com/in/peeti-sriwongsanguan/">Peeti Sriwongsanguan</a></h5>
            <ul style="text-align: center;  list-style-position: inside;">
                <li>Data Curator</li>
                <li>Data Scientist</li>
            """
        )
    with cols[3]:
        st.image('https://media.licdn.com/dms/image/D5603AQGcQPisMa2S4A/profile-displayphoto-shrink_400_400/0/1678848601924?e=1722470400&v=beta&t=q7TjSvO0_OuiDeofsw2vEPGaZK8P5Lur39cBCiZs-uE')
        st.html(
            """
            <h5 style="text-align: center;"><a href="https://www.linkedin.com/in/nithika-sivashankar/">Nithika Sivashankar</a></h5>
            <ul style="text-align: center;  list-style-position: inside;">
                <li>Front-End Developer</li>
                <br>
            </ul>
            """
        )