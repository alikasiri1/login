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
from streamlit_javascript import st_javascript
import webbrowser

st.set_page_config(page_title="profesearch", page_icon='🐍', menu_items=None)#, initial_sidebar_state="collapsed"

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

url = str(st_javascript("window.location.search"))
print(url)
print(url.split("%")[-1][2:])
print("--------------------")
if url.split("%")[-1][2:] == "singup":
    st.write("singup : hehehheheheheheh")
    st.markdown("""<a href="http://localhost:8501"   target = "_self">go back</a>""",unsafe_allow_html=True)
    st.markdown("""<a href="https://emailverify.streamlit.app"   target = "_self">go back</a>""",unsafe_allow_html=True)

elif url.split("%")[-1][2:] == "login":
    st.markdown("""<a href="http://localhost:8501?singup"   target = "_self">singup</a>""",unsafe_allow_html=True)
    st.write("hehehehehehehheheh")
    st.markdown("""<a href="http://localhost:8501"   target = "_self">go back</a>""",unsafe_allow_html=True)
    st.markdown("""<a href="https://emailverify.streamlit.app"   target = "_self">go back</a>""",unsafe_allow_html=True)

else:
    st.markdown("""<a href="http://localhost:8501?login"   target = "_self">login</a>""",unsafe_allow_html=True)
    st.markdown("""<a href="https://emailverify.streamlit.app?login"   target = "_self">login</a>""",unsafe_allow_html=True)
    w = st.button("write")
    if w:
        st.warning("you must loging in")
        st.markdown("""<a href="http://localhost:8501/table"   target = "_self"><button class="css-7ym5gk ef3psqc11"> login</button></a> """ , unsafe_allow_html=True)
        st.markdown("""<a href="https://emailverify.streamlit.app/table"   target = "_self"><button class="css-7ym5gk ef3psqc11"> login</button></a> """ , unsafe_allow_html=True)
 
    # com.iframe()