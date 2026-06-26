import streamlit as st
from streamlit import title, subheader

st.title("Weather Forecast for the Next Days")
city = st.text_input("Place:",placeholder="Enter the name of the city")
days = st.slider("Forecast Days:",min_value=1,max_value=5,value=1, help="How many days do you want to forecast")
options = st.selectbox('Select data to view', ('temperature','sky' ))

subheader(f'Temperature for the next {days} days in {city}')