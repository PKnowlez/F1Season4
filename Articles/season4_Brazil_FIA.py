import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

def article():
    date = "Sunday 12/07/2025"

    st.markdown('''
                <div style="background-color: #97978F; padding: 10px; border-radius: 5px;">

                **Press Release** <br>
                **For Immediate Release** <br>
                Date: December 07, 2025 <br>

                **SUBJECT:** Official League Regulations Update <br>

                The FIA has finalized three new regulations. Below are the details on each. During the race in Brazil, these regulations were partially implemented and monitored. During the race, a restart was necessary due to a glitch. There were no race start incidents worth noting. However, during the race a collision was caused by Alpine driver Joshua with VCARB driver Josh. In the furture this incident would have been reviewed under the criteria specified in 'Causing a Collision.'

                **RACE START INCIDENT** <br>
                During the start of a race or Red Flag restart, any driver found to be the cause of an incident will be penalized in the league's next race.* An incident in this scenario is any collision, squeeze, or brake check, involving one or more cars getting damage or losing more than 3 places due to the incident. The driver at fault will be penalized by being unable to compete in Q2 of the next race. In other words, the driver will qualify last, unless there are late drivers, in which those drivers that are late will start behind the offending driver from the previous race. A penalty point will also be added to the driver's super license for the remainder of the season.

                *This regulation will be modified for the final race of the season to penalize the driver on their finishing position in the final race, rather than carrying over to the next season.

                **CAUSING A COLLISION** <br>
                In some scenarios, drivers may cause a collision that is not severe enough to meet the requirements of Regulation 8 - Endangering or Ruining Another Driver's Race. In these scenarios, drivers who cause a collision will be penalized with a 5 second or 10 second penalty to their finishing position. The size of the penalty will be based on league review and severity of the incident. A penalty point will also be added to the driver's super license for remainder of the season.

                **RACE RESTARTS** <br>
                Races will not be restarted for racing incidents. If there is a bug or glitch during or before the race start, the race may be restarted depending on the scenario.

                **DECISION ISSUED BY** <br>
                FIA Stewards - The Alternative F1 League <br>
                December 07, 2025

                <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div> <br>

                <p style="color:lightgray;">The Alternative F1 League <br> Where racing meets integrity and fair competition.</p>
                ''', unsafe_allow_html=True)    
    
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()