import streamlit as st


dividend=int(st.text_input("Enter your dividend here: "))
divisor=int(st.text_input("Enter your dividend here: "))

try:
  print(dividend/divisor)
except ZeroDivisionError:
  print("The divisor cannot be zero!")
