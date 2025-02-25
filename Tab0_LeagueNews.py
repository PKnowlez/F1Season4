import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
import base64
from streamlit_carousel import carousel
from PIL import Image

# Images
australia_circuit = Image.open("./Images/Australia_Circuit.png")
spa_circuit = Image.open("./Images/Spa_Circuit.png")
spain_circuit = Image.open("./Images/Spain_Circuit.png")
china_circuit = Image.open("./Images/China_Circuit.png")
baku_circuit = Image.open("./Images/Baku_Circuit.png")
canada_circuit = Image.open("./Images/Canada_Circuit.png")
abu_dhabi_circuit = Image.open("./Images/Abu_Dhabi_Circuit.png")
austria_circuit = Image.open("./Images/Austria_Circuit.png")
cota_circuit = Image.open("./Images/COTA_Circuit.png")

def Tab0():
    if 'show_all_content' not in st.session_state:
        st.session_state.show_all_content = False

    #region --
    st.markdown('''
                <p style="color:lightgray;">DAY XX/YY/ZZZ - AUTHOR</p>
                ''',
                unsafe_allow_html=True,)
    st.divider()
    #endregion
    
    # ----------------------------------------------------------------------------------------------------------
    # "Show More/Less" button 
    if not st.session_state.show_all_content:
        if st.button('Show More'):
            st.session_state.show_all_content = True
            st.rerun()  # Rerun the app to show everything
    else: 
        if st.button('Show Less'):
            st.session_state.show_all_content = False
            st.rerun()

    if st.session_state.show_all_content:
        #region --
        st.markdown('''
                <p style="color:lightgray;">DAY XX/YY/ZZZ - AUTHOR</p>
                ''',
                unsafe_allow_html=True,)
        st.divider()
        #endregion