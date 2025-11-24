import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

def article():
    date = "Sunday 11/23/2025"

    st.markdown('''
                <div style="background-color: #97978F; padding: 10px; border-radius: 5px;">

                **Press Release** <br>
                **For Immediate Release** <br>
                Date: November 23, 2025 <br>
                Time: 20:30 local <br>
                From: The Stewards <br>
                To: All Competitors, All Teams <br>

                **SUBJECT:** Decision – Joshua & Leo Incidents <br>

                **JOSHUA VS. PATRICK** <br>
                **Summary** <br>
                Over roughly two minutes, Joshua made several late-braking attempts to pass Patrick into three consecutive corners, making light contact (“taps”) with Patrick’s car each time. This is considered avoidable and unnecessary contact that negatively affected Patrick’s race.

                **Decision** <br>
                - 10-second time penalty for causing a collision (avoidable contact).
                - 1 penalty point for:
                    - Endangering Patrick’s race, and
                    - Multiple infringements in a short span (three contacts in three corners).
                
                Joshua will be dropped 10 seconds, based on the final race results to 6th place. The penalty point is logged for future reference.

                **LEO – FINAL CORNER INCIDENT** <br>
                **Summary** <br>
                On the final corner, Leo attempted a very late move that resulted in contact and directly changed the result at the end of the race. Leo then DNF’d.

                **Decision** <br>
                - 1 penalty point for a reckless late move that altered the race result.
                - 5-place grid penalty for Leo at the next main race.
                    - With this being a Brazil sprint / reverse-grid weekend, applying it as a grid drop for the main race is the cleanest and fairest option.

                **RECAP** <br>
                - Joshua → 10s time penalty + 1 penalty point for repeated avoidable contact on Patrick over three corners.
                - Leo → 1 penalty point + 5-place grid penalty at the next main race for a final-corner move that changed the result.
                - Race results will be updated as described above, but otherwise stand; these penalties and points will be used when assessing any future incidents and repeat offences.

                **DECISION ISSUED BY** <br>
                FIA Stewards - The Alternative F1 League <br>
                Circuit de Spa-Francorchamps <br>
                November 23, 2025

                <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div> <br>

                <p style="color:lightgray;">The Alternative F1 League <br> Where racing meets integrity and fair competition.</p>
                ''', unsafe_allow_html=True)    
    
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()