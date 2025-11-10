import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

cover = Image.open("./Images/austria_reverse.jpg")
track = Image.open("./Images/Austria_Circuit.png")

def article():
    date = "Monday 11/10/2025"
    author = "Patrick"

    st.subheader('''Race Week: Austria (Reverse)''')
    st.image(cover)
    st.markdown('''
                The league has never faced a challenge like this one; a track no official F1 race has ever run on, turns no one has ever really tested to the limit, and a guessing game on what setups and strategies will play out best.

                But that's what makes this something to look forward to. The Red Bull Ring is sure to provide some thrilling racing with it's three DRS zones, uphill sweepers, and tight track limits. While examining the track, it is clear that there are only a few true overtaking locations. The most obvious two spots are at the end of the final DRS zone and Turn 1. The turn at the end of the second DRS zone might entice some drivers, but it is likely not worth the late braking and overtake due to the immediate DRS gift the overtaking driver will give to the driver who was overtaken.

                In addition to the unique DRS enabled overtaking zones, there might be moments at the top of the uphill portion of Sector 2 where a driver could feasibly squeeze their opponents and make a side-by-side maneuver. This opportunity would allow the overtaker to take advantage of the upcoming DRS zone to secure the move.
                ''')
    st.image(track)
    st.markdown('''
                Since the league has never raced in this configuration, there are no previous results and it is all to play for. However, the league has begun to hear rumors of retirements, team swaps, and even a shakeup in the FIA leadership structure. Below, we will recap some of the rumors from around the leaue.

                **RUMOR MILL**  
                The strongest rumor running around is that one of the drivers in Papaya will be moving on from their position as a driver to a new rank within the FIA at the end of the season. There are no names associated with this rumor just yet, and it is unclear what role within the FIA is opening up or if a new one is being created. More on this as it develops.

                In addition to the rumors surrounding McLaren, there are rumors around the upcoming 11th team on the grid. Word on the street is that four drivers are looking to combine forces on what they are calling Team USA. This was discovered from leaked carrier bald eagle messages that the group of four has been sending to covertly communicate their plans. Handwriting analyses are underway and we will likely find answers in the near future on who these potential drivers are.

                With Kick Sauber finding the end of their run as a team this season, there have also been rumors of who might race with rings next year. Some solid rumors are coming in that a good lineup is coming to Audi next season. Whoever these drivers are they "gotta go fast, like Sonic, like Sonic" with all those rings.
                ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()