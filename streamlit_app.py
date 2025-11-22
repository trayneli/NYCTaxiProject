import streamlit as st

st.title("NYC Taxi Analytics Dashboard")
st.write(
    "NYC Efficiency Analysis"
)

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

tableau_url = "https://public.tableau.com/views/NYCTaxiEfficiency/Dashboard3"

embed_url = f"{tableau_url}?:language=en-US&:display_count=n&:origin=viz_share_link&:embed=yes&:showVizHome=no&:toolbar=top"

components.iframe(embed_url, height=1500, scrolling=True)
