import streamlit as st

a= st.number_input('enter tabe')
for i in range(1, 11):
    st.write(i*a)