import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

image = Image.open("./Images/Spa_Circuit.png")
cover = Image.open("./Images/Spa_Cover.jpg")

def article():
    date = "Sunday 11/16/2025"
    author = "Patrick"

    st.subheader('''Race Week: Spa''')
    st.image(cover)
    st.markdown('''
                The longest lap on the calendar is here and the league won't just race it once, but twice with a sprint and full race on the docket for Wednesday night.

                This will be a particularly grueling battle for many of the drivers with only one true DRS straight and a long defenseive and tight Sector 2. This all leads to a tantalizingly long flat out section up to the famed location of what once was the bus stop chicane.
                ''')
    st.image(image)
    st.markdown('''
                The track starts with a bare minimum run down to Turn 1. **I have been requested by FIA officials to put a helpful reminder here, BRAKE EARLY.** Turn 1, even on a standard mid-race lap is trecherous. At the beginning of the race it is truly a monster.

                Once the drivers have made it through Turn 1, it's pedal to the floor for the race to the Kemmel Straight. Those with enough gaul might even deploy their ERS up through the winding Eau Rogue twsists up Raidillon. The end of the Kemmel Straight is likely the best place for overtaking on the entire track. The wisest drivers will even allow their opponents to slip away a tiny bit up Eau Rogue, and then close with ERS and DRS on the straight. Overtaking and being side-to-side up the hill is simply put, unwise, for both the attacker and defender.
                
                After the famed uphill corners and straight, the technical downhill Sector 2 begins. Those running with enough downforce may catchup to the drivers with looser and slipperier setups. There are no traditional overtaking spots during Sector 2. But there are a few spots where an overtake is feasible, but potentially ill-advised.

                As Sector 2 ends, drivers are met with a flat out run all the way into the heaviest braking zone on the circuit. Here we may see a few attempt overtakes, but we may also see some drivers meet their demise as they go wide, hit the wall, or take a spin with a wheel dipped in the grass.

                With a sprint race on the schedule that means the drivers will participate in a special format. A single, short, qualifying session for the sprint and then a reverse grid race based on the results of the sprint race.

                Looking back into the league's history, it appears that Nick and McLaren have never lost here. Back-to-back-to-back-to-back wins are on the line for both Jairo and Nick. For Jairo, it would be four straight in season wins. For Nick, it would be four straight wins at Spa. Either way, at least one, if not both of these streaks will end this week.
                ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()