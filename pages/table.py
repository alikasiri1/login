import streamlit as st
from database import sign_up, fetch_users ,update_user
import streamlit_authenticator as stauth
st.set_page_config(page_title="login page", page_icon='🐍', menu_items=None)

def table():
    users = fetch_users()
    emails = []
    usernames = []
    passwords = []

    for user in users:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])

    credentials = {'usernames': {}}
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(credentials , cookie_name='Streamlit', key='abcdef')#, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4
    
    email, authentication_status, username = Authenticator.login(':green[Login]', 'main')
    print(email)
    print(username)
    stt = st.empty()
    stt.markdown("""<a href="http://localhost:8501/singup"   target = "_self">create acount</a> """ , unsafe_allow_html=True)
    st.markdown("""<a href="https://emailverify.streamlit.app/singup"   target = "_self">create acount</a> """ , unsafe_allow_html=True)

    info, info1 = st.columns(2)


    if authentication_status == False:
        no_sidebar_style = """
        <style>
            section[data-testid="stSidebar"] {display: none;}
        </style>
            """
        st.markdown(no_sidebar_style, unsafe_allow_html=True)
        st.error("Username/password is incorrect")

    elif authentication_status == None:
        no_sidebar_style = """
        <style>
            section[data-testid="stSidebar"] {display: none;}
        </style>
            """
        st.markdown(no_sidebar_style, unsafe_allow_html=True)
        st.warning("Please enter your username and password")

    if authentication_status:
        stt.empty()

        st.sidebar.subheader(f'Welcome {username}')
        Authenticator.logout('Log Out', 'sidebar')
        no_sidebar_style = """
            <style>
                div[data-testid="stSidebarNav"] {display: none;}
            </style>
        """
        st.markdown(no_sidebar_style, unsafe_allow_html=True)

        st.subheader('This is the home page')
        st.markdown(
            """
            ---
            Created with ❤️ by SnakeByte
            
            """
        )
        payment =st.button("hi")
        if payment:
            update_user(email , {"payment" : 10})


table()
