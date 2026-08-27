import datetime
import time
import streamlit as st

# 2. Add Pastel Pink Background CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffdde1 0%, #ee9ca7 100%) !important;
        color: #4a4a4a;
    }
   
   /* Headings & Subtitles */
    h1, h2, h3, p, label {
        color: #2c3e50 !important;
        font-weight: 600 !important;
    }

    /* Container with Solid White Background and Black Border */
    div[data-testid="stVerticalBlock"] > div[style*="border"] {
        background-color: #ffffff !important;
        border-radius: 20px !important;
        border: 3px solid #111111 !important;
        padding: 24px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15) !important;
    }

    /* Input Fields */
    .stTextInput input, .stDateInput input {
        background-color: #ffffff !important;
        color: #2c3e50 !important;
        border-radius: 10px !important;
        border: 1px solid #e0e0e0 !important;
    }

    /* Action Button */
    .stButton > button {
        background: linear-gradient(135deg, #d63384 0%, #e83e8c 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 12px !important;
        transition: transform 0.2s ease !important;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
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
        for _ in range(3):
            st.balloons()
            time.sleep(0.3)

        st.markdown(
            f"""
            <div style="
                background-color: #d4edda;
                color: #155724;
                border: 2px solid #c3e6cb;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                font-size: 26px;
                font-weight: bold;
                box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            ">
                Happy Birthday, {name}! Today is your special day! 💕🎉
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="
                background-color: #e2f0d9;
                color: #2e6b27;
                border: 2px solid #b7e1cd;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                font-size: 22px;
                font-weight: bold;
            ">
                Hiya {name}, there are <span style="font-size: 30px; color: #1e4620;">{days_left}</span> days until your next birthday! 🎈
            </div>
            """,
            unsafe_allow_html=True
        )

