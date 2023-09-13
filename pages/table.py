import streamlit as st
from database import sign_up, fetch_users ,update_user
import streamlit_authenticator as stauth
st.set_page_config(page_title="table", page_icon='🐍', initial_sidebar_state="collapsed", menu_items=None)
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
    st.markdown("""<a href="http://localhost:8501/singup"   target = "_self">create acount</a> """ , unsafe_allow_html=True)
    st.markdown("""<a href="https://emailverify.streamlit.app/singup"   target = "_self">create acount</a> """ , unsafe_allow_html=True)
    # sldf = Authenticator.register_user("sign_up","main",preauthorization=False)
    # app_state = st.experimental_get_query_params() 
    # if 'login' not in st.session_state:
    #     st.session_state['login'] = False
    info, info1 = st.columns(2)

    # print(st.session_state["login"])

    
    # if authentication_status == False or authentication_status == None:
    #     no_sidebar_style = """
    #     <style>
    #         section[data-testid="stSidebar"] {display: none;}
    #     </style>
    #         """
        # st.markdown(no_sidebar_style, unsafe_allow_html=True)
        # if "login" not in st.session_state:
        # # if "my_saved_result" not in app_state:
        #     stt = st.empty()
        #     bb = stt.button("sing_up")

        #     if bb:
        #         st.experimental_set_query_params(my_saved_result=True)
        #         st.session_state["login"] = True
        #         # print(st.session_state["login"])
        #         stt.empty()
        # if "login" in st.session_state:
        # # if "my_saved_result" in app_state:
        #     if st.session_state["login"]:
        #     # if app_state["my_saved_result"][0]:
        #         don = sign_up()
        #         if don:
        #             st.session_state.clear()
        #             # app_state.clear()
        #             stt = st.empty()
        #             bb = stt.button("sing_up")
        #             st.success('Account created successfully!!')
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
        # dic = {}
        # dic["username"] = username
        # dic["email"] = email
        # dic["Authenticator"] = Authenticator
        # return  dic
        # st.session_state.clear()
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
        # if "username" not in dic:
        #     if username:
        #         if username in usernames:
        #             if authentication_status:
                        
                        # dic["username"] = username
                        # dic["email"] = email
                        # dic["Authenticator"] = Authenticator
                        # return  dic
                        # let User see app
                        # app_state.clear()
                        # st.session_state.clear()
                        # st.sidebar.subheader(f'Welcome {username}')
                        # Authenticator.logout('Log Out', 'sidebar')
                        # no_sidebar_style = """
                        #     <style>
                        #         div[data-testid="stSidebarNav"] {display: none;}
                        #     </style>
                        # """
                        # st.markdown(no_sidebar_style, unsafe_allow_html=True)

                        # st.subheader('This is the home page')
                        # st.markdown(
                        #     """
                        #     ---
                        #     Created with ❤️ by SnakeByte
                            
                        #     """
                        # )
                        # payment =st.button("hi")
                        # if payment:
                        #     update_user(email , 2)

                #     elif not authentication_status:
                #         with info:
                #             st.error('Incorrect Password or username')
                #     else:
                #         with info:
                #             st.warning('Please feed in your credentials')
                # else:
                #     with info:
                #         st.warning('Username does not exist, Please Sign up')


table()
# def page(username , email , Authenticator):
#     st.session_state.clear()
#     st.sidebar.subheader(f'Welcome {username}')
#     Authenticator.logout('Log Out', 'sidebar')
#     no_sidebar_style = """
#         <style>
#             div[data-testid="stSidebarNav"] {display: none;}
#         </style>
#     """
#     st.markdown(no_sidebar_style, unsafe_allow_html=True)

#     st.subheader('This is the home page')
#     st.markdown(
#         """
#         ---
#         Created with ❤️ by SnakeByte
        
#         """
#     )
#     payment =st.button("hi")
#     if payment:
#         update_user(email , 2)
# # dic = {}
# if "login_page" not in st.session_state:
#     st.session_state["login_page"] = {}

# if "personal" not in st.session_state:
#     st.session_state["personal"] = False

# if not st.session_state["personal"]: 
#     st.session_state["login_page"]  = table()

# if st.session_state["login_page"]:
#     if "username" in st.session_state["login_page"]:
#         st.session_state["personal"] = True
#         page(st.session_state["login_page"]["username"] ,st.session_state["login_page"]["email"] , st.session_state["login_page"]["Authenticator"])
    
