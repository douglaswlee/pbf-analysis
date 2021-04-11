import streamlit as st
import pandas as pd

import home
import aggregate
import magistrate
import price
import neighborhood
import race_gender

def main():
    PAGES = {
        "Home": home,
        "Summary" : aggregate,
        "By Actor" : magistrate,
        "By Price" : price,
        "By Neighborhood" : neighborhood,
        "By Demographics": race_gender
    }
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Please select a page", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

if __name__ == '__main__':
    main()