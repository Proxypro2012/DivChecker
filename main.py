import streamlit as st
import math


col1, col2, col3 = st.columns([1, 2, 1]) 

with col2:
  dividend=int(st.text_input("Enter your dividend here: ", value=5))
  divisor=int(st.text_input("Enter your divisor here: ", value=5))

try:
  st.write(dividend/divisor)
except ZeroDivisionError:
  st.write("The divisor cannot be zero!")
