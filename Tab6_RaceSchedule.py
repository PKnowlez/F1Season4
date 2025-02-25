import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

def Tab6():
    schedule = pd.read_excel('The_Alternative_F1.xlsx', sheet_name='S2Schedule')
    
    # CSS to inject contained in a string
    hide_table_row_index = """
    <style>
    thead tr th:first-child {display:none}
    tbody th {display:none}
    </style>
    """
    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    # Print Table
    st.table(schedule)