import streamlit as st
import plotly.express as px
from backend import get_data


# Add Title,text input,slider,selectbox, and slider
st.title("Weather Forecast for the Next Days")
city = st.text_input("Place:",placeholder="Enter the name of the city" ,value='London')
days = st.slider("Forecast Days:",min_value=1,max_value=5,value=1, help="How many days do you want to forecast")
options = st.selectbox('Select data to view', ('Temperature','Sky' ))

st.subheader(f'Temperature for the next {days} days in {city}')
# Get the Temperature/Sky data
filtered_data= get_data(city.title(),days )

if type(filtered_data) == str:
    st.error(filtered_data)
else :
        if options == 'Temperature':
            # create temperature plot
            temperatures = [dict['main']['temp'] / 10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]

            figure = px.line(x=dates,y=temperatures,labels={'x':'Data','y':'Temperature (C)'})
            st.plotly_chart(figure)
        if options == 'Sky':
            images ={'Clear':'images/clear.png', 'Clouds':'images/cloud.png', 'Rain':'images/rain.png', 'Snow':'images/snow.png'}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths,width=110)


