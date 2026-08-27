import datetime
import time
import streamlit as st

# 
st.set_page_config(
    page_title="Birthday Countdown !",
    page_icon="🎊", 
  layout="centered"
) 

#
st.markdown(
    """
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #ffdde1 0%, #ee9ca7 100%) !important;
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

    /* Input Fields Styling - Matches Text and Date Inputs */
    div[data-testid="stTextInput"] > div > div, 
    div[data-testid="stDateInput"] > div > div {
        background-color: #262730 !important;
        border-radius: 8px !important;
        border: none !important;
    }

    .stTextInput input, .stDateInput input {
        color: #ffffff !important;
        background-color: transparent !important;
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


# 
st.title("Birthday Countdown !")
st.caption("Made by Animex~")
st.caption("Enter your birthdate below to see how many days until your birthday!~")
st.divider()

# 
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

    try:
        next_bday = datetime.date(today.year, bday_date.month, bday_date.day)
    except ValueError:
        next_bday = datetime.date(today.year, 3, 1)
    
    if next_bday < today:
        try:
            next_bday = datetime.date(today.year + 1, bday_date.month, bday_date.day)
        except ValueError:
            next_bday = datetime.date(today.year, 3, 1)

    if next_bday < today:
        try:
            next_bday = datetime.date(today.year + 1, bday_date.month, bday_date.day)
        except ValueError:
            next_bday = (datetime.date(today.year + 1, 3, 1))

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

