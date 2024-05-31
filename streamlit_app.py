import streamlit as st
import random

# Set the title of the app
st.title("Home Price Estimator")

# Create input fields for user to enter home details
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2, step=1)
latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=37.7749)
longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=-122.4194)
zipcode = st.text_input("Zipcode", value="94103")

# Button to trigger price estimation
if st.button("Estimate Price"):
    # Generate random numbers for min and max price (replace this with your model's prediction)
    min_price = random.randint(300000, 500000)
    max_price = random.randint(500001, 800000)
    
    # Display the min and max price
    st.write(f"Estimated Minimum Price: ${min_price}")
    st.write(f"Estimated Maximum Price: ${max_price}")

# To run this Streamlit app, save this script as `app.py` and run `streamlit run app.py` in your terminal.
