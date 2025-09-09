import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

image = Image.open("./Images/Rookie Button.png")
image2 = Image.open("./Images/New Foe.png")

def article():
    date = "Monday 09/08/2025"
    author = "Patrick"

    st.subheader('''The rookies are coming! The rookies are coming!''')
    st.image(image2)
    st.markdown('''
                Shouts around the paddock this week have been all about the rookies. As some begin to post times in time trial and others participate in full race weekend simulations with their teammates, the league's rookies are starting to heat up their tires.

                Wheels are spinning, tires are screeching, and gravel and grass are most certainly being touched. Their practice efforts are clearly all aimed at one goal, performing. None of the five rookies are here just to turn some laps. Each of them is here to see what they are made of. They want to win and they want to help elevate their teams to the next level.

                But with five fresh drivers zipping around the league, this is the first year it has made sense for a new award to be fought for.

                That's right, this season, there will be an award for the rookie who brings home the most points across the course of the season. In addition to the award, a new filter has been added to the driver comparison tab within the Season 4 app, allowing users to narrow down the results of the app to just the five rookie drivers.
                ''')
    st.image(image)
    st.markdown('''
                All this means that when the lights go out for the first time this season, there will be so much more at play than just the two main championships. Yes, a four-peat is on the line for the Driver's Championship, and yes the Constructor's Championship is certainly way up in the air. But maybe more importantly, the league's rookies are going to be elevated well above where they might normally be and put straight into the spotlight from day one.
                
                Each of these rookies will be racing for their own copy of the league's trophy that lists them as the one and only rookie of the year for The Alternative F1 Season 4.
                ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()