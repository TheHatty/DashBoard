import streamlit as st
import pandas as pd

data_path = "houses_to_rent_v2.csv"

dataframe = pd.read_csv(data_path, sep=',')

st.set_page_config(layout='wide')
st.title("Dashboard para alugue de imoveis")

#defining 3 collums for standout values
collum1, collum2, collum3 = st.columns(3)

with collum1:
    total_houses = len(dataframe['rooms'])
    st.metric(label="Quatidade de imoveis disponiveis", value=total_houses)

with collum2:
    min_rent = dataframe['rent amount (R$)'].min()
    st.metric(label="aluguel minimo", value=min_rent)

with collum3:
    max_rent = dataframe['rent amount (R$)'].max()
    st.metric(label="aluguel maximo", value= max_rent)


#price furnished and not furnished
avg_price_furnished = dataframe[dataframe['furniture'] == 'furnished']['rent amount (R$)'].mean()
avg_price_n_furnished = dataframe[dataframe['furniture'] == 'not furnished']['rent amount (R$)'].mean()

#price by city
avg_price_city = dataframe.groupby('city')['rent amount (R$)'].mean().sort_values(ascending=True)

#plot a bar graph to streamlit
st.bar_chart(avg_price_city, x_label="Media de Preços", y_label="Estados", horizontal=True, height=500)
