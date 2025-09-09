import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

image = Image.open("./Images/Trophy.png")
image2 = Image.open("./Images/Trophy_Side.png")

def article():
    date = "Sunday 08/24/2025"
    author = "Patrick"

    st.subheader('''The Hardware We're Racing For''')
    st.image(image)
    st.markdown('''
                Season 4 brings a refresh to the championship trophy. Like last year, each track is displayed. However, in addition to the tracks, the track name and winner of each track will be displayed. For the Constructor's Championship, the winning team will be listed instead of the winning driver which will be on the Driver's trophy.

                All of these details will be centered around the winner's car which is captured moments before crossing the finish line and claiming their hardware.

                At the bottom of the trophy the driver or team's statistics for the season will be displayed next to their respective IRL trophy for the respective championship.
                
                Each trophy will be created with state of the art 3D printing technology and delivered to each of the winners, runners up, and third place finishers for each championship.
                ''')
    st.image(image2)
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()