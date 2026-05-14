import streamlit as st


def footer_home():

    st.markdown("""
        <div style="
            text-align:center;
            margin-top:30px;
            width:100%;
        ">
            <p style="
                color:white;
                font-weight:bold;
                font-size:18px;
            ">
                Created with ❤️ by Kushagra
            </p>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():

    st.markdown("""
        <div style="
            width:100%;
            text-align:center;
            margin-top:40px;
            margin-bottom:20px;
        ">
            <p style="
                font-weight:bold;
                color:black;
                font-size:18px;
            ">
                Created with ❤️ by Kushagra
            </p>
        </div>
    """, unsafe_allow_html=True)