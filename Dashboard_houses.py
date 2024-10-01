import streamlit as st
import pandas as pd

data_path = "houses_to_rent_v2.csv"

data = pd.read_csv(data_path, sep=',', engine='python')
dataframe = pd.DataFrame(data)

#layout
st.set_page_config(layout='wide')
st.title("Universidade Federal Do Maranhão")
st.write("Especialização em Análise de dados e inteligencia artificial")
st.write("Disciplina: Visualização de dados")
st.write("Aluno: Luis Carlos Dutra Junior")
st.title("Dashboard de imoveis")

#defining 3 collums for standout values
collum1a, collum2a, collum3a = st.columns(3)

with collum1a:
    total_houses = len(dataframe['rooms'])
    st.metric(label="Quatidade de imoveis disponiveis", value=total_houses)

with collum2a:
    min_rent = dataframe['rent amount (R$)'].min()
    st.metric(label="aluguel minimo", value=min_rent)

with collum3a:
    max_rent = dataframe['rent amount (R$)'].max()
    st.metric(label="aluguel maximo", value= max_rent)


#price furnished and not furnished
avg_price_furniture = dataframe.groupby('furniture')['rent amount (R$)'].mean().sort_values(ascending=True)

#price funished by animal acceptance
avg_price_animal = dataframe.groupby('animal')['rent amount (R$)'].mean().sort_values(ascending=True)

#price by city
avg_price_city = dataframe.groupby('city')['rent amount (R$)'].mean().sort_values(ascending=True)

#defining main per city graph
st.bar_chart(avg_price_city, x_label="Media de Preços", y_label="Estados", horizontal=True, height=500, width=800)

st.title("Media de preços por aceitação de animais e mobilia")

#defining 2 collums
collum1b, collum2b = st.columns(2)

with collum1b:
    #plot a bar graph to streamlit
    st.bar_chart(avg_price_animal, height=500)

with collum2b:
    st.bar_chart(avg_price_furniture, height=500)
 
