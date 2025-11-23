import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-panel"] {
        overflow: visible;
    }
    iframe {
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("NYC Taxi Analytics Dashboard")

tableau_url="https://public.tableau.com/views/Taxi_Demand_and_Vendor_EDA_Final/FinalDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
#tableau_url2 = "https://public.tableau.com/views/NYCTaxiEfficiency/Dashboard2?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
tableau_url2 = "https://public.tableau.com/views/NYCTaxiEfficiency/Dashboard2?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

tableau_url3="https://public.tableau.com/views/Demand_forecasting_17639297095930/Dashboard2?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
embed_url = f"{tableau_url}&:embed=yes&:showVizHome=no&:toolbar=top"
embed_url2 = f"{tableau_url2}&:embed=yes&:showVizHome=no&:toolbar=top"
embed_url3=f"{tableau_url3}&:embed=yes&:showVizHome=no&:toolbar=top"

if "page" not in st.session_state:
    st.session_state.page = "EDA"

# Sidebar navigation
#st.sidebar.title("")

if st.sidebar.button("EDA", use_container_width=True):
    st.session_state.page = "EDA"

if st.sidebar.button("Efficiency Analysis", use_container_width=True):
    st.session_state.page = "Efficiency"

if st.sidebar.button("Demand Forecasting", use_container_width=True):
    st.session_state.page = "LSTM"

if st.sidebar.button("Fare Predictions", use_container_width=True):
    st.session_state.page = "Fare"

#st.sidebar.caption("")

#st.title("")

if st.session_state.page == "EDA":
    st.markdown("### Exploratory Data Analysis")
    st.caption("EDA Analysis for NYC Taxi Data")
    components.iframe(embed_url, width=1200, height=3500, scrolling=True)

elif st.session_state.page == "Efficiency":
    st.markdown("### Taxi Efficiency Analysis")
    st.caption("Efficiency Score and Ride Quality Score (RQS) calculations compared across different Taxi Ride characteristics, including trip time, trip purpose, trip route, trip speed and factors contributing to overall ride quality and efficiency")
    components.iframe(embed_url2, width=1200, height=1500, scrolling=True)

elif st.session_state.page == "LSTM":
    st.markdown("### Taxi Demand Forecasting")
    st.caption("Hourly taxi demand forecast across NYC boroughs. Blue shows actual July 2025 demand, orange displays August 2025 predictions. The NeuralProphet model captures daily patterns with morning/evening peaks, weekly cycles, and overnight lows.")
    components.iframe(embed_url3, width=1200, height=800, scrolling=True)

elif st.session_state.page == "Fare":
    st.markdown("### Taxi Fare Predictions")
    st.caption("ML-based fare predictions")
    components.iframe(embed_url, width=1200, height=800, scrolling=True)


# ## Pages for dashboards
# tab1, tab2, tab3, tab4 = st.tabs(["EDA", "Efficiency Analysis", "Taxi Ride Predictions: LSTM", "Taxi Fare Predictions"])

# with tab1:
#     st.markdown("### EDA")
#     st.caption("EDA Analysis for NYC Taxi Data")
#     components.iframe(embed_url, width=1200, height=1500, scrolling=False)

# with tab2:
#     st.markdown("### Efficiency Analysis")
#     st.caption("Revenue trends and sales performance")
#     components.iframe(embed_url2, width=1100, height=800, scrolling=False)

# with tab3:
#     st.markdown("### Taxi Ride Predictions: LSTM")
#     st.caption("Taxi LSTTM Predictions")
#     components.iframe(embed_url, width=1200, height=1500, scrolling=False)

# with tab4:
#     st.markdown("### Taxi Fare Predictions")
#     st.caption("Taxi Fare Predictions")
#     components.iframe(embed_url, width=1200, height=1500, scrolling=False)
