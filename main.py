import streamlit as st
import math


col1, col2, col3 = st.columns([1, 2, 1]) 

with col2:
  dividend=int(st.text_input("Enter your dividend here: "))
  divisor=int(st.text_input("Enter your dividend here: "))

try:
  st.write(dividend/divisor)
except ZeroDivisionError:
  st.write("The divisor cannot be zero!")
