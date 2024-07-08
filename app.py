import streamlit as st

# Create the input fields
name = st.text_input("Name")
father_name = st.text_input("Father's Name")
address = st.text_area("Address")
class_room = st.text_input("Class Room")
mobile_number = st.text_input("Mobile Number")
email = st.text_input("Email")

# Display the entered data
if st.button("Submit"):
    st.write("## Submitted Information")
    st.write(f"**Name:** {name}")
    st.write(f"**Father's Name:** {father_name}")
    st.write(f"**Address:** {address}")
    st.write(f"**Class Room:** {class_room}")
    st.write(f"**Mobile Number:** {mobile_number}")
    st.write(f"**Email:** {email}")

