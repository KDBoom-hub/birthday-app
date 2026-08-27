import datetime
import streamlit as st

# page header
st.title("Birthday Countdown !")

# asks for user input
name = st.text_input("Enter your name:", "Friend")
bday_date  = st.date_input(
    "Select your birthday: ",
    value=datetime.date(2000, 1, 1),
    min_value=datetime.date(2000, 1, 1),
    max_value=datetime.date.today()
)

# run calc when button is clicked
if st.button("Calculate Days Left"):
    today = datetime.date.today()

    next_bday = datetime.date(today.year, bday_date.month, bday_date.day)

    if next_bday < today:
        next_bday = datetime.date(today.year + 1, bday_date.month, bday_date.day)

    days_left = (next_bday - today).days

    if days_left == 0:
        st.balloons()
        st.success(f"Happy Birthday, {name}! Today is your special day! ❤️")
    else:
        st.info(f"Hiya, there are **{days_left} days** until your birthday!")

