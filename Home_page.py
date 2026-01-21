# home_page
import streamlit as st
st.sidebar.title("Qlevo.com")
op = st.sidebar.radio("Navigation", ["Home", "Products", "Support", "Account", "Terms and conditions"])
if op == "Home":
    st.image("Logo.png", width=300)
    st.title("Welcome to Qlevo.com")
    st.subheader("Your one-stop solution for all your needs.")
    st.markdown("[Follow us in Twitter to get the recent updates](https://twitter.com/QlevoCom)") # Comming soon
elif op == "Products":
    st.title("Explore anywhere, anytime with Qlevo")
    st.subheader("Discover our range of products designed to make your life easier.")
    st.write("Neet registration tool") 
    st.markdown("[Neet Registration 2025](http://192.168.31.214:8502)") # Tool_1.py
    st.write("Neet result analysis tool")
    st.markdown("[Neet Result Analysis 2025](http://192.168.31.214:8503)") # Tool_2.py
elif op == "Support":
    st.title("We are here to help you always")
    st.write("Customer care contact:  +91-9800919124")
    st.write("Service email: chauhannilay888@gmail.com")
    st.write("Place Order at +91-1200220120")
    st.write("For more support, visit our [Support Page](http://192.168.31.214:8504)") # support.py
elif op == "Account":
    st.title("Manage your Qlevo Account")
    st.subheader("Login to access your personalized dashboard and manage your orders.")
    st.markdown("[Login to your Account](http://192.168.31.214:8505)") # account.py
elif op == "Terms and conditions":
    st.title("Terms and Conditions")
    st.write("By using Qlevo.com, you agree to our terms and conditions. Please read them carefully before proceeding.")
    st.write("1. User Responsibilities: Users must provide accurate information during registration and are responsible for maintaining the confidentiality of their account credentials.")
    st.write("2. Product Usage: Products offered by Qlevo.com are for personal use only. Unauthorized commercial use is prohibited.")
    st.write("3. Privacy Policy: We are committed to protecting your privacy. Please review our Privacy Policy for details on how we collect, use, and safeguard your information.")
    st.write("4. Limitation of Liability: Qlevo.com is not liable for any damages arising from the use or inability to use our products or services.")
    st.write("5. Changes to Terms: We reserve the right to modify these terms at any time. Continued use of our services constitutes acceptance of the updated terms.")
    st.write("For any questions or concerns regarding our terms and conditions, please contact our support team.")
