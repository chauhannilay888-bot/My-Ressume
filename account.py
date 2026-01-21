# account.py
import streamlit as st
import json as js
st.title("Manage your Qlevo account")
st.subheader("Existing User? Login here")
a = st.text_input("Email ID")
b = st.text_input("Password", type="password")
fill = (a and b)
with open("account.json", "r") as f:
    data = js.load(f)
    if st.button("Login"):
        if not fill:
            st.warning("Please fill all the fields")
        elif a in data["E-mail"] and b in data["Password"]:
            st.success("Logged in Successfully")
        else:
            st.error("No such account found")
st.subheader("New User? Create an account")
c = st.text_input("Username")
d = st.text_input("Create Email ID")
e = st.text_input("Create Password", type='password')
e1 = st.text_input("Confirm Password", type='password')
filled = (c and d and e and e1)
if st.button("Create Account"):
    if not filled:
        st.warning("Please fill all the datails")
    elif e != e1:
        st.error("Password do not match")
    elif d in data["E-mail"] or e in data["Password"]:
        st.info("E-mail ID or Password already in use!")
    else:
        data["E-mail"].append(d)
        data["Password"].append(e)
        with open("account.json", "w") as f:
            js.dump(data, f, indent=4) 
            with open("forms.csv", "a") as f:
                f.write(f"{c}, {d}, {e}\n")
                st.success("Account Created Successfully")