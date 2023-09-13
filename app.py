###################################################

# import streamlit as st
# from mycomponent import mycomponent
# value = mycomponent(my_input_value="hello there")
# st.write("Received", value)
################################################

import streamlit as st
import streamlit_authenticator as stauth
from database import sign_up, fetch_users 
import streamlit.components.v1 as com
import webbrowser

# st.set_page_config(page_title='Streamlit',  initial_sidebar_state='collapsed')
st.set_page_config(page_title="profesearch", page_icon='🐍', menu_items=None)#, initial_sidebar_state="collapsed"
# st. markdown(""" <style> .css-vk3wp9.eczjsme11 { display: none; } </style> """, unsafe_allow_html=True)
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
    """
st.markdown(no_sidebar_style, unsafe_allow_html=True)
no_sidebar_style = """
    <style>
        section[data-testid="stSidebar"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

# try:
 
# def open_support_ticket():
#     email_link = "https://appgit-8oduf5nlupbrtnl43xcrul.streamlit.app/table"
#     webbrowser.open(email_link,new=0)
#     # st.markdown("http://localhost:8501/", unsafe_allow_html=True)
# st.button("Contact us!", on_click=open_support_ticket)

# st.markdown("""<a href="https://appgit-8oduf5nlupbrtnl43xcrul.streamlit.app/table"   target = "_self"><button class="css-7ym5gk ef3psqc11"> go to table</button></a> """ , unsafe_allow_html=True)
# login()

# st.subheader('This is the home page')
# st.markdown(
#                 """
#                 ---
#                 Created with ❤️ by SnakeByte
                   
#                 """
#             )
w = st.button("write")
if w:
    st.warning("you must loging in")
    st.markdown("""<a href="http://localhost:8501/table"   target = "_self"><button class="css-7ym5gk ef3psqc11"> login</button></a> """ , unsafe_allow_html=True)
    # st.markdown("""<a href="https://emailverify.streamlit.app/table"   target = "_self"><button class="css-7ym5gk ef3psqc11"> login</button></a> """ , unsafe_allow_html=True)
    # users = fetch_users()
    # emails = []
    # usernames = []
    # passwords = []

    # for user in users:
    #     emails.append(user['key'])
    #     usernames.append(user['username'])
    #     passwords.append(user['password'])

    # credentials = {'usernames': {}}
    # for index in range(len(emails)):
    #     credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    # Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4)
        
    # email, authentication_status, username = Authenticator.login(':green[Login]', 'main')

    # app_state = st.experimental_get_query_params() 

    # info, info1 = st.columns(2)

    # if "my_saved_result" not in app_state:
    #     stt = st.empty()
    #     bb = stt.button("sing_up")

    #     if bb:
    #         st.experimental_set_query_params(my_saved_result=True)
    #         stt.empty()

    # if not authentication_status:
    #     if "my_saved_result" in app_state:
    #         if app_state["my_saved_result"][0]:
    #             don = sign_up()
    #             if don:
    #                 app_state.clear()
    #                 stt = st.empty()
    #                 bb = stt.button("sing_up")
    #                 st.success('Account created successfully!!')

    # if username:
    #     if username in usernames:
    #         if authentication_status:
    #             # let User see app
    #             app_state.clear()
    #             st.sidebar.subheader(f'Welcome {username}')
    #             Authenticator.logout('Log Out', 'sidebar')

    #             st.subheader('This is the home page')
    #             st.markdown(
    #                 """
    #                 ---
    #                 Created with ❤️ by SnakeByte
                    
    #                 """
    #             )


    #         elif not authentication_status:
    #             with info:
    #                 st.error('Incorrect Password or username')
    #         else:
    #             with info:
    #                 st.warning('Please feed in your credentials')
    #     else:
    #         with info:
    #             st.warning('Username does not exist, Please Sign up')


# except:
#     st.success('Refresh Page')

# from streamlit import caching

# import streamlit.components.v1 as com
# stt = st.empty()
# stts = st.empty()
# t = False
# if not t:
#     b = stts.empty().button("send" , key="dfkgfd")
#     # c = stt.button("sends" , key="dfkgdfd")
    
#     c = """
    # <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    # <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
    # <script>// validation example for Login form
    #     $("#btnLogin").click(function(event) {

    #         var form = $("#loginForm");

    #         if (form[0].checkValidity() === false) {
    #             event.preventDefault();
    #             event.stopPropagation();
    #         }

    #         // if validation passed form
    #         // would post to the server here

    #         form.addClass('was-validated');
    #     });
    # </script>
    # <div class="col-md-6 offset-md-3">
    #                 <span class="anchor" id="formLogin"></span>

    #                 <!-- form card login with validation feedback -->
    #                 <div class="card card-outline-secondary">
    #                     <div class="card-header">
    #                         <h3 class="mb-0">Login</h3>
    #                     </div>
    #                     <div class="card-body">
    #                         <form class="form" role="form" autocomplete="off" id="loginForm" novalidate="" method="POST">
    #                             <div class="form-group">
    #                                 <label for="uname1">Username</label>
    #                                 <input type="text" class="form-control" name="uname1" id="uname1" required="">
    #                                 <div class="invalid-feedback">Please enter your username or email</div>
    #                             </div>
    #                             <div class="form-group">
    #                                 <label>Password</label>
    #                                 <input type="password" class="form-control" id="pwd1" required="" autocomplete="new-password">
    #                                 <div class="invalid-feedback">Please enter a password</div>
    #                             </div>
    #                             <div class="form-check small">
    #                                 <label class="form-check-label">
    #                                     <input type="checkbox" class="form-check-input"> <span>Remember me on this computer</span>
    #                                 </label>
    #                             </div>
    #                             <button type="submit" class="btn btn-success btn-lg float-right" id="btnLogin">Login</button>
    #                         </form>
    #                     </div>
    #                     <!--/card-body-->
    #                 </div>
    #                 <!-- /form card login -->

    #             </div>
#                 """
#     # stt.markdown(c ,unsafe_allow_html=True )
#     d =com.html(c , height=300)
#     if b :
#         d.empty()
#         stt.empty()
#         stts.empty()