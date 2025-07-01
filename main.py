import streamlit as st


dividend=int(input("Enter your dividend here: "))
divisor=int(input("Enter your dividend here: "))

try:
  print(dividend/divisor)
except ZeroDivisionError:
  print("The divisor cannot be zero!")
