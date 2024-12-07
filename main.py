import streamlit as st


home_page = st.Page(
    page='views/home.py',
    title='Home',
    default=True
)


pages=[home_page]

pg = st.navigation(pages=pages)

pg.run()
