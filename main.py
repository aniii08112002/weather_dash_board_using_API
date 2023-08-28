import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast for the Next Days")
place=st.text_input("Place:")
days=st.slider("forecast days",min_value=1,max_value=5,
               help="select the number of forecast days")
option=st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
data=get_data(place,days,option)

    temperature=[days*i for i in temperature]
    return date,temperature
d,t=get_data(days)

figure=px.line(x=d,y=t,labels={"x":"DATE","y":"TEMPERATURE (C)"})
st.plotly_chart(figure)