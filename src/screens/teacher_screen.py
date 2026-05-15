import streamlit as st
import time
from src.ui.style_base_layout import style_background_dashboard, style_base_layout
from src.screens.components.header import header_dashboard
from src.screens.components.footer import footer_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login

def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    
    # Check if a teacher is already logged in
    if "teacher_data" in st.session_state and st.session_state.teacher_data:
        teacher_dashboard()
    
    # Otherwise, handle Login/Register routing
    else:
        if 'teacher_login_type' not in st.session_state:
            st.session_state.teacher_login_type = "login"

        if st.session_state.teacher_login_type == "login":
            teacher_screen_login()
        elif st.session_state.teacher_login_type == "register":
            teacher_screen_register()

def teacher_dashboard():
    """This displays after a successful login."""
    teacher_data = st.session_state.teacher_data
    
    c1, c2 = st.columns([3, 1])
    with c1:
        st.header(f"Welcome, {teacher_data['name']}!") 
    with c2:
        if st.button("Logout", type="secondary"):
            del st.session_state.teacher_data
            st.session_state.is_logged_in = False
            st.rerun()

    st.write("---")
    st.info("Teacher Dashboard Content Goes Here (Classes, Attendance, etc.)")
    footer_dashboard()

def login_teacher_logic(username, password):
    """Helper to verify and set session state."""
    if not username or not password:
        return False
    
    teacher = teacher_login(username, password)

    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return teacher 
    return None

def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Login to your teacher profile")
    
    teacher_username = st.text_input("Enter Username", placeholder='e.g. kush_sharma', key="login_user").strip()
    teacher_pass = st.text_input("Enter Password", type='password', placeholder="••••••••", key="login_pass").strip()

    st.divider()
    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button("Login", icon=':material/passkey:', use_container_width=True):
            if not teacher_username or not teacher_pass:
                st.warning("Please enter both username and password")
            else:
                # Use the helper logic
                logged_in_user = login_teacher_logic(teacher_username, teacher_pass)
                if logged_in_user:
                    st.toast(f"Welcome back, {logged_in_user['name']}!", icon="👋")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Invalid username or password")

    with btnc2:
        if st.button("Register Instead", type="primary", icon=':material/person_add:', use_container_width=True):
            st.session_state.teacher_login_type = 'register'
            st.rerun()
    footer_dashboard()

def register_teacher(username, name, pwd, pwd_confirm):
    if not name or not pwd or not username:
        return False, "All fields are required!"
    if pwd != pwd_confirm:
        return False, 'Passwords do not match'
    if check_teacher_exists(username):
        return False, 'Username is already taken'

    success = create_teacher(username, pwd, name)
    
    if success:
        return True, 'Successfully Created! Login Now'
    return False, 'Database error during registration'

def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='registerbackbtn', use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Register your teacher profile")
    
    teacher_username = st.text_input("Create Username", placeholder='e.g. kush_sharma', key="reg_user").strip()
    teacher_name = st.text_input("Enter Full Name", placeholder='Kushagra Sharma', key="reg_name").strip()
    teacher_pass = st.text_input("Create Password", type='password', key="reg_pass").strip()
    teacher_pass_confirm = st.text_input("Confirm Password", type='password', key="reg_confirm").strip()

    st.divider()
    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button("Register now", type='primary', icon=':material/how_to_reg:', use_container_width=True):
            success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
            if success:
                st.success(message)
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)

    with btnc2:
        if st.button("Login Instead", icon=':material/login:', use_container_width=True):
            st.session_state.teacher_login_type = 'login'
            st.rerun()
    footer_dashboard()