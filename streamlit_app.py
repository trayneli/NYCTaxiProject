import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("NYC Taxi Analytics Dashboard")

tableau_url="https://public.tableau.com/views/Taxi_Demand_and_Vendor_EDA_Final/FinalDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
tableau_url2 = "https://public.tableau.com/views/NYCTaxiEfficiency/Dashboard2?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

embed_url = f"{tableau_url}&:embed=yes&:showVizHome=no&:toolbar=top"
embed_url2 = f"{tableau_url2}&:embed=yes&:showVizHome=no&:toolbar=top"

## Pages for dashboards
tab1, tab2, tab3, tab4 = st.tabs(["EDA", "Efficiency Analysis", "Taxi Ride Predictions: LSTM", "Taxi Fare Predictions"])

with tab1:
    st.markdown("### EDA")
    st.caption("EDA Analysis for NYC Taxi Data")
    components.iframe(embed_url, width=1200, height=1500, scrolling=True)

with tab2:
    st.markdown("### Efficiency Analysis")
    st.caption("Revenue trends and sales performance")
    components.iframe(embed_url2, width=1200, height=1500, scrolling=True)

with tab3:
    st.markdown("### Taxi Ride Predictions: LSTM")
    st.caption("Taxi LSTTM Predictions")
    components.iframe(embed_url, width=1200, height=1500, scrolling=True)

with tab4:
    st.markdown("### Taxi Fare Predictions")
    st.caption("Taxi Fare Predictions")
    components.iframe(embed_url, width=1200, height=1500, scrolling=True)
