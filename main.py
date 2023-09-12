import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast for the Next Days")
place=st.text_input("Place:")
days=st.slider("forecast days",min_value=1,max_value=5,
               help="select the number of forecast days")
option=st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data=get_data(place,days)


    if option=="Temperature":
        temperatures=[dict['main']['temp'] for dict in filtered_data]
        dates=[dict["dt_txt"] for dict in filtered_data]
        figure=px.line(x=dates,y=temperatures,labels={"x":"DATE","y":"TEMPERATURE (C)"})
        st.plotly_chart(figure)
    if option=="Sky":
        sky_conditions=[dict["weather"][0]["main"] for dict in filtered_data]
        images={"Clear":"images/clear.png","Snow":"images/snow.png","Clouds":"images/cloud.png","Rain":"images/rain.png"}
        image_path=[images[conditions] for conditions in sky_conditions]
        print(sky_conditions)

        st.image(image_path,width=115)

