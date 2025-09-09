import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

image = Image.open("./Images/Schedule_Reveal.png")

def article():
    date = "Thursday 08/21/2025"
    author = "Patrick"

    st.subheader('''The League's Longest Season to Date''')
    st.markdown('''
                As drivers around the league begin preparing with their teams, the FIA has been hard at work finalizing this season's schedule. Due to the length of this season the FIA has elected to include a few deliberate breaks in the action to allow drivers and their teams a moment of rest during the 14 race season plus both pre and post-season sessions.

                The league will hit the track for pre-season testing in Silverstone on Wednesday September 24, 2025. At 8:45PM Eastern, the engines will roar to life for the first qualifying round of the year. When discussing the intricacies of this season, the FIA made it clear that races will start promptly at 8:45PM Eastern, with a small bit of spare time for drivers who are just barely running behind.

                After pre-season testing, the drivers will take on the first two races of the year and then be met with an early Fall Break to allow for a bit of rest and extra practice for the rookies after their first stint in the league.

                From there, the drivers will take on the longest stint of regular season races on the calendar, which will end with a time of rest around Thanksgiving. Once the drivers are fat and happy, they will take to the streets again for a three race stint that gives way to the final pause of the season, Winter Break.

                Finally, with Winter Break completed, there will be four races that close out the season and then the post-season race at the end of January. Below, you will see the schedule in full with all of the races on Wednesday nights, except the New Year showdown in Jeddah.
                ''')
    st.image(image)
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()