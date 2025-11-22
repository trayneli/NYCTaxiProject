import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("NYC Taxi Analytics Dashboard")

tableau_url = "https://public.tableau.com/views/NYCTaxiEfficiency/Dashboard2?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"


embed_url = f"{tableau_url}&:embed=yes&:showVizHome=no&:toolbar=top"

## Pages for dashboards
tab1, tab2, tab3, tab4 = st.tabs(["EDA", "Efficiency Analysis", "Taxi Ride Analysis", "Taxi Predictions"])

with tab1:
    st.markdown("### EDA")
    st.caption("Key metrics and performance at a glance")
    components.iframe(embed_url, width=1200, height=1500, scrolling=True)

with tab2:
    st.markdown("### Efficiency Analysis")
    st.caption("Revenue trends and sales performance")
    components.iframe(embed_url, width=1200, height=1500, scrolling=True)

with tab3:
    st.markdown("### Taxi Ride Analysis")
    st.caption("Taxis")
    components.iframe(embed_url, width=1200, height=1500, scrolling=True)

with tab4:
    st.markdown("### Taxi Predictions")
    st.caption("Taxi Predictions")
    components.iframe(embed_url, width=1200, height=1500, scrolling=True)
