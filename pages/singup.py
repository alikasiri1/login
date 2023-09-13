from database import sign_up
import streamlit as st

no_sidebar_style = """
    <style>
        section[data-testid="stSidebar"] {display: none;}
    </style>
            """
st.markdown(no_sidebar_style, unsafe_allow_html=True)
sign_up()

# st.markdown("""<a href="http://localhost:8501/table"   target = "_self">login</a> """ , unsafe_allow_html=True)
st.markdown("""<a href="https://emailverify.streamlit.app/table"   target = "_self">login</a> """ , unsafe_allow_html=True)
# from database import sign_up, fetch_users ,update_user
# from table import u
# st.sidebar.subheader(f'Welcome {username}')
# # Authenticator.logout('Log Out', 'sidebar')
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