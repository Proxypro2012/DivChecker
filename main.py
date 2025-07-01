import streamlit as st

col1, col2, col3 = st.columns([1, 2, 1]) 

with col2:
    dividend_input = st.text_input("Enter your dividend here:", value="5")
    divisor_input = st.text_input("Enter your divisor here:", value="5")

try:
    dividend = int(dividend_input)
    divisor = int(divisor_input)
    result = dividend / divisor
    st.write(f"Result: {result}")
except ZeroDivisionError:
    st.write("❌ The divisor cannot be zero!")
except ValueError:
    st.write("❌ Make sure to enter valid numbers for both dividend and divisor!")
