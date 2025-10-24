import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

def article():
    date = "Thursday 10/23/2025"
    author = "Patrick"

    st.subheader('''BREAKING NEWS''')
    st.markdown('''
                The FIA has released a ruling on the incident that caused immense drama during last night's race. In a surprising twist, the ruling body did not award either driver any form of race altering penalty. The findings were thorough and involved the review of expert racers from outside of the league.
                
                No official statements have been shared thus far from teams. However, murmors around the league are beginning.
                ''')

    st.markdown('''
                <div style="background-color: #97978F; padding: 10px; border-radius: 5px;">

                **Press Release** <br>
                **For Immediate Release** <br>
                Date: October 23, 2025 <br>
                Time: 20:45 local <br>
                From: The Stewards <br>
                To: All Competitors, All Teams <br>

                **SUBJECT:** Decision – Incident Between Nick (McLaren) and Eddie (Alpine), Turn 10, Lap 21 <br>

                **DESCRIPTION OF INCIDENT** <br>
                The Stewards were requested to review an incident involving Nick (McLaren) and Eddie (Alpine) at Turn 10 on Lap 21 of the Spanish Grand Prix. During the approach to Turn 10, Eddie missed the initial braking point and ran long into the corner. While doing so, he transmitted a radio message indicating that Nick could pass. At the same time, Nick, following closely behind, also missed his braking point and, affected by turbulent (“dirty”) air, made contact with the rear of the Alpine. Nick subsequently alleged that the incident constituted a breach of Article 33.4 of the FIA Formula One Sporting Regulations, which prohibits “erratic driving, such as any sudden braking or other manoeuvre liable to endanger another driver.”

                **FINDINGS OF THE STEWARDS** <br>
                After reviewing all available telemetry, on-board video, and team radio communications, and following consultation with three independent arbiters, the Stewards determined that:

                1. Both drivers missed their braking points independently of each other.
                2. The “brake test” provision under Article 33.4 does not apply in this scenario because both drivers were within a braking zone where they are already decelerating for a corner. In such cases, the article is interpreted to cover erratic movement under braking (for example, a sudden change of line or unnecessary variation in braking pressure), none of which was observed prior to the collision.
                3. Eddie’s radio message was a reaction to having overshot the corner entry and not an intentional signal of erratic braking.
                4. The contact occurred as a result of Nick’s misjudgment of the braking distance and aerodynamic disturbance from following closely.

                **DECISION** <br>
                The Stewards classify the incident as a racing incident. No further action will be taken regarding the race result. However, as Nick (McLaren) was deemed to have initiated contact, one (1) penalty point is added to his Super License for causing a collision.

                **REASON** <br>
                The evidence confirms that both drivers misjudged their braking independently, and no erratic movement under braking was detected. The application of Article 33.4 does not extend to genuine braking errors where both competitors are already in the braking phase for a corner.
                
                **FURTHER NOTES** <br>
                The FIA Stewards remind all competitors that situational awareness and car control remain the driver’s responsibility at all times, and that radio communication does not exempt a driver from maintaining safe operation of their vehicle.

                **DECISION ISSUED BY** <br>
                FIA Stewards - The Alternative F1 League <br>
                Circuit de Barcelona-Catalunya <br>
                October 23, 2025

                <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div> <br>

                <p style="color:lightgray;">The Alternative F1 League <br> Where racing meets integrity and fair competition.</p>
                ''', unsafe_allow_html=True)    
    
    st.markdown('''             
                With this ruling in place, three drivers now have Super License points for the remainder of the season. Should these drivers or others continue to gain penalty points, they will incur larger penalties when they are involved in a more severe incident that ends or ruins another driver's race.
                ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()