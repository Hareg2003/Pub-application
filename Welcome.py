#import requirements
import streamlit as st
import pandas as pd
import numpy as np

#reading dataset
df=pd.read_csv('pub.csv')

st.set_page_config(
     page_title="Streamlit App",
     page_icon=":shark:",
     layout="wide"
 )

#title alignment and color
# Object notation



st.title("Welcome to Open Pub Application")
title_alignment="""
<style>
#welcome-to-open-pub-application {
  text-align: center
  
}
</style>
"""
title_color="""
<style>
#welcome-to-open-pub-application {
  color:White
  
}
</style>
"""
title_font="""
<style>
#welcome-to-open-pub-application {
  font-family: "Times New Roman", Times, serif
  
}
</style>
"""
st.markdown(title_color, unsafe_allow_html=True)
st.markdown(title_alignment, unsafe_allow_html=True)
st.markdown(title_font, unsafe_allow_html=True)


st.header("TIME FOR SOME DRINKS...LET'S ENJOY!")


basic = st.selectbox('',('No. of pubs in UK','Head','Tail','unique local authority'))

if basic=='No. of pubs in UK':
    st.markdown(f'There  are  **{df.shape[0]}**  Pubs  in  **United Kingdom**')

elif basic=='Head':
    st.dataframe(df.head())

elif basic=='Tail':
    st.dataframe(df.tail())

elif basic=='unique local authority':
    st.text(f'Total no of pub local authority is {len(df.local_authority.unique())} in United Kingdom')

st.subheader('Find the Statistics information of the pub dataset')
stat = st.button('Describe')

if stat==True:
    st.dataframe(df.describe())
else:
    st.text('')
