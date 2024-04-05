import os
import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

st.caption("This is a simple website created by Shashi. Based on the cuisine selected, it generates name of restaurants and respective menus. This is implemented in Langchain and uses OpenAI Large Language Models (LLMs)",
           unsafe_allow_html=False, help=None)


## cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian","Italian","American","Chinese","Japanese", "Korean","Thai","Mexican"))

cuisine = st.text_input("Pick a Cuisine", value="", max_chars=None, key=None, type="default")

image_name = cuisine.lower()+".png"


if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(str(response['restaurant_name']))
    if os.path.exists(image_name):
        st.image(str(image_name), caption='Bob Apetit', width=300)
    else:
        st.image(str("bon-appetit.png"), width=300)
    menu_items = response['menu_items'].strip().split(',')
    st.write("**Menu Items**")
    for item in menu_items:
        st.write(item)