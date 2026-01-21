# neet_forms.py
import streamlit as st
import pandas as pd
import json as js
st.title("Neet registration by NTA 2025-26")
st.title("Fill the form")
a = st.text_input("Name")
b = st.number_input("Age")
c = st.text_input("Father")
d = st.text_input("Mother")
e = st.number_input("Contact", min_value=1000000000, max_value=9999999999) # number should be 10 digit
g = st.number_input("Adhar Number", min_value=100000000000, max_value=999999999999) # Adhar Number should be 12 digit
h = st.text_input("DOB in DD.MM.YYYY")
i = st.text_input("Gender")

forms = {
    "Name": [a],
    "Age": [b],
    "Father": [c],
    "Mother": [d],
    "Contact": [e],
    "Adhar": [g],
    "DOB": [h],
    "Gender": [i]
}

df = pd.DataFrame(forms)
fill = (a and b and c and d and e and g and h and i) # all the fields
with open("neet_forms.json", "r") as f:
    data = js.load(f)
roll = len(data["Name"]) + 1 # roll number per user from 1 - final seat
if st.button("Submit"):
    if 17 <= b <=25 and fill:
        with open("neet_forms.json", "w") as f:
            data["Name"].append(a)
            data["Age"].append(int(b))
            data["Father"].append(c)
            data["Mother"].append(d)
            data["Contact"].append(e)
            data["Adhar"].append(g)
            data["DOB"].append(h)
            data["Gender"].append(i)
            data["Roll number"].append(roll)
            js.dump(data, f, indent=4)
            st.success("Registered successfully")
    elif not fill:
        st.warning("Please fill all the fields")
    else:
        st.error("Age must be 17 to 25")
