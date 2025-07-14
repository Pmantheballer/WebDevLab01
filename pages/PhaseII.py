import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt  #NEW

with open("data.json", "r") as f:
    gpa_data = json.load(f)

df = pd.DataFrame(gpa_data)

st.title("High School GPA Trend")  #NEW
st.subheader("Tracking my academic growth over 4 years")  #NEW

st.write("Here is the full GPA data:")  #NEW
st.dataframe(df, use_container_width=True)  #NEW

fig, ax = plt.subplots()  #NEW
ax.plot(df["Semester"], df["GPA"], marker="o", linewidth=2)  #NEW
ax.set_xlabel("Semester")  #NEW
ax.set_ylabel("Weighted GPA")  #NEW
ax.set_title("My Weighted GPA Over Time")  #NEW
plt.xticks(rotation=45)  #NEW
st.pyplot(fig)  #NEW

st.write("---")
user_gpa = st.number_input("Enter your current GPA", min_value=0.0, max_value=5.0, step=0.01)  #NEW
st.write(f"Your entered GPA: {user_gpa}")  #NEW
select_semester = st.selectbox("Select a semester to highlight", df["Semester"])  #NEW
highlighted = df[df["Semester"] == select_semester]  #NEW
st.write(f"You selected: {select_semester} — GPA: {highlighted['GPA'].values[0]}")  #NEW
if "gpa_list" not in st.session_state:  #NEW
    st.session_state.gpa_list = []  #NEW
if st.button("Add to GPA History"):  #NEW
    st.session_state.gpa_list.append(user_gpa)  #NEW
st.write("Your GPA History This Session:")  #NEW
st.line_chart(st.session_state.gpa_list)  #NEW
