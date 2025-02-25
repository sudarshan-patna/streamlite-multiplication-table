import streamlit as st

st.title('multiplication table application')

a= st.number_input('enter the number')
for i in range(1, 11):
    st.write(i*a)
