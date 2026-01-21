# neetresult.py
import streamlit as st
import pandas as pd
with open("neet_forms.json", "r") as f:
    data = pd.read_json(f)
students = {
    "Name": data["Name"],
    "Roll number": data["Roll number"],
    "Marks": data["Marks"], # Should manually enter in he json file
    "Mother": data["Mother"],
    "Father": data["Father"],
    "DOB": data["DOB"],
    "Contact": data["Contact"],
    "Gender": data["Gender"]
}
df = pd.DataFrame(students)
st.title("Neet result 2025")
df["Rank"] = df["Marks"].rank(ascending = False, method= "min").astype(int)
st.write(df.sort_values("Rank", ascending=True))

name_in = st.text_input("Enter the name")
if st.button("Search with name"):
    if name_in in df["Name"].values:
        data = df[df["Name"] == name_in]
        st.success("Student Found")
        st.write(data)
    else:
        st.error("No such student found")

roll_in = st.number_input("Enter the roll number")
if st.button("Search with roll"):
    if roll_in in df["Roll number"].values:
        data_1 = df[df["Roll number"] == roll_in]
        st.success("Student Found")
        st.write(data_1)
    else:
        st.error("No such student found")