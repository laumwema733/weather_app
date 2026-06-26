import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
city = st.text_input("Place:",placeholder="Enter the name of the city")
days = st.slider("Forecast Days:",min_value=1,max_value=5,value=1, help="How many days do you want to forecast")
options = st.selectbox('Select data to view', ('temperature','sky' ))

st.subheader(f'Temperature for the next {days} days in {city}')

def get_data(days):
    dates =["2026-25-10","2026-26-10","2026-27-10"]
    temperatures =[10,11,15]
    temperatures =[days * i for i in temperatures]
    return dates,temperatures


d,t = get_data(days)

figure = px.line(x=d,y=t,labels={'x':'Data','y':'Temperature (C)'})
st.plotly_chart(figure)