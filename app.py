import datetime
import streamlit as st

# 2. Add Pastel Pink Background CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffdde1 0%, #ee9ca7 100%) !important;
        color: #4a4a4a;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# set browser tap config
st.set_page_config(
    page_title="Birthday Countdown !",
    page_icon="🎊", 
  layout="centered"
) 

# page header
st.title("Birthday Countdown !")
st.caption("Enter your birthdate below to see how many days until your birthday!~")
st.divider()

# asks for user input
with st.container(border=True):
    st.subheader("🎂 Enter your details in")

name = st.text_input("Enter your name:", "Friend")

bday_date  = st.date_input(
    "Select your birthday: ",
    value=datetime.date(2000, 1, 1),
    min_value=datetime.date(2000, 1, 1),
    max_value=datetime.date.today()
)

# run calc when button is clicked
if st.button("Calculate Days Left 🍾", use_container_width=True):
    today = datetime.date.today()

    next_bday = datetime.date(today.year, bday_date.month, bday_date.day)

    if next_bday < today:
        next_bday = datetime.date(today.year + 1, bday_date.month, bday_date.day)

    days_left = (next_bday - today).days

    if days_left == 0:
        st.balloons()
        st.snow()
        st.success(f"Happy Birthday, {name}! Today is your special day! ❤️")
    else:
        st.info(f"Hiya, **{name}** there are **{days_left} days** until your birthday!")

