import streamlit as st

from utils import sidebar, display_mermaid, PRIMARY_COLOR


st.set_page_config(page_title="Andrew Higgins - ML API Project", layout='wide', page_icon='☁️')

sidebar()

# ----- Body -----

static_dir = "static/api/"

st.markdown(
    f"""
    # Robust API deployed with <span style='color:{PRIMARY_COLOR}'>Docker</span> and <span style='color:{PRIMARY_COLOR}'>Kubernetes</span>
    *Solo project built in 14 weeks for* Machine Learning Systems Engineering *course at UC Berkeley, fall 2023*
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    ## Project Summary

    The final product is a natural language sentiment classification API hosted on <span style='color:{PRIMARY_COLOR}'>Microsoft Azure</span> cloud platfom.
    
    The App was built with <span style='color:{PRIMARY_COLOR}'>Python's FastAPI</span> package and unit tested with <span style='color:{PRIMARY_COLOR}'>pytest</span>.
    The App and its components were containerized with <span style='color:{PRIMARY_COLOR}'>Docker</span>, and deployed with <span style='color:{PRIMARY_COLOR}'>Kubernetes</span>.
    System load performace was improved with <span style='color:{PRIMARY_COLOR}'>Redis</span> caching.
    Incoming and outgoing data validation was implemented with <span style='color:{PRIMARY_COLOR}'>Pydantic</span>.
    Performance metrics were recorded with <span style='color:{PRIMARY_COLOR}'>istio</span> and monitored using <span style='color:{PRIMARY_COLOR}'>Grafana</span>.

    The app was load tested with over 1600 requests per second, and it maintained a P99 of only ~800 ms!
    """,
    unsafe_allow_html=True
)

with st.container(border=True):
    st.markdown("### Tech Stack")
    st.html(
        """
        <p align="center">
            <!--Hugging Face-->
                <img src="https://user-images.githubusercontent.com/1393562/197941700-78283534-4e68-4429-bf94-dce7ab43a941.svg" width=13%, title="Hugging Face">
            <!--FAST API-->
                <img src="https://user-images.githubusercontent.com/1393562/190876570-16dff98d-ccea-4a57-86ef-a161539074d6.svg" width=13%, title="FastAPI">
            <!--REDIS LOGO-->
                <img src="https://user-images.githubusercontent.com/1393562/190876644-501591b7-809b-469f-b039-bb1a287ed36f.svg" width=13%, title="Redis">
            <!--KUBERNETES-->
                <img src="https://user-images.githubusercontent.com/1393562/190876683-9c9d4f44-b9b2-46f0-a631-308e5a079847.svg" width=13%, title="Kubernetes">
            <!--Azure-->
                <img src="https://user-images.githubusercontent.com/1393562/192114198-ac03d0ef-7fb7-4c12-aba6-2ee37fc2dcc8.svg" width=13%, title="Azure">
            <!--K6-->
                <img src="https://user-images.githubusercontent.com/1393562/197683208-7a531396-6cf2-4703-8037-26e29935fc1a.svg" width=13%, title="K6">
            <!--GRAFANA-->
                <img src="https://user-images.githubusercontent.com/1393562/197682977-ff2ffb72-cd96-4f92-94d9-2624e29098ee.svg" width=13%, title="Grafana">
        </p>
        """
    )
    with st.expander("Show list"):
        st.markdown(
            """
            1. Hugging Face
            2. FastAPI
            3. Redis
            4. Kubernetes
            5. Azure
            6. K6
            7. Grafana
            """
        )

with st.container(border=True):
    st.markdown("## Cloud Infrastructure")
    cols = st.columns([0.3,0.7])
    with cols[0]:
        st.markdown(
            """
            Key elements:
            - Python **FastAPI** container containing DistilBERT sentiment analysis model from **Huggingface**
            - **Redis** cache container.
            - Auto-scaling, load balancing, and network traffic coordination with **Kubernetes**.
            - Distinct production and deployment environments configured with **Kubernetes Kustomizations**.
            - App hosted in **Microsoft Azure Cloud**. *

            <sup><sub>*major Azure configuration was done by instructors: DNS, ingress gateways, resource groups</sub></sup>
            """, 
            unsafe_allow_html=True
        )
    with cols[1]:
        with open(static_dir + 'app_deployment_flow_diagram.mmd', 'r') as f:
            app_flow = f.read()
        display_mermaid(app_flow, height=550, primary_text_color='#000000')

with st.container(border=True):
    st.markdown("## API Sequence Logic")
    cols = st.columns(2)
    with cols[0]:
        st.markdown(
            """
            The sequence that occurs in each replicaset pod:
            1. Recieve POST payload from client and validate with **Pydantic**.
            2. Return HTML error if schema is violated.
            3. Check request payload against **Redis** cache.
            4. Return cached prediction to App if it exists.
            5. Invoke model with novel values.
            6. Store prediction value in App.
            7. Store new request-prediction key-value pair in cache.
            8. Return prediction payload to client.
            """
        )
    with cols[1]:
        with open(static_dir + 'api_seq_diagram.mmd', 'r') as f:
            app_seq = f.read()
        display_mermaid(app_seq)

with st.container(border=True):
    st.markdown(
        """
        ## Load Testing Results

        Load testing was performed with **K6**, and results are displayed with **Grafana**.  

        Load testing was performed with 10 simulated users over the course of 10 minutes, with a ramp-up period of 30 seconds and a ramp-down period of 3 minutes. Test data was generated to achieve a cache hit rate of 95%.

        The app passed load testing, with P(99) below the 2 second target threshold. In fact, even P(99.99) was below 2 seconds! (an opportunity for compute cost-savings)  
        During peak load, the replicaset scaled up to 6 pods.
        """
    )
    cols = st.columns([0.53,0.47])
    with cols[0]:
        st.image(static_dir + 'dashboard.png', caption='Grafana dashboard view')
    with cols[1]:
        st.image(static_dir + 'request_duration_graph.png')
    st.image(static_dir + 'K6.png', caption='K6 detailed test results')