import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

def article():
    st.markdown('''
                <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div>
                ''', unsafe_allow_html=True)
    st.markdown('''
                **Press Release** \n
                **For Immediate Release**  
                _Date: October 9, 2025_

                **Miami Race Results & Driver Penalty Points Update:**

                Race officials have reviewed the incident in the final moments of the race between Mercedes' Jayden and Aston Martin's Del. It has been deemed that the maneuver was not on purpose but was on the fault of the Mercedes driver. Therefore, Jayden has been penalized five (5) places down to 8th place, and will have one (1) penalty point added to his license for the season.

                Additionally, upon reviewing the incident between VCARB's Patrick and Ferrari's Leo, the FIA has determined there will be no action taken that affects the final results. Leo will not receive a penalty point on his license.

                Finally, Alpine's Eddie was served a private written warning for his actions during the start of the Bahrain Grand Prix. This warning also adds one (1) penalty point to his license for the remainder of the season. 
                
                The FIA co-presidents are open to inquiries, clarifications, and formal correspondence. For further discussion, please contact Erick Tavera or Nick Beglin.
                    
                Jayden and Eddie's verdicts should not be considered the standard or norm for the league. These decisions were determined due to unprecedented circumstances and factors that will not continue to be considered valid throughout the remainder of the season. Going forward, the FIA will uphold its written regulations with full rigor. This release should serve as the final regulation reminder and warning to all drivers.

                League regulations can be found in the league's [main app](https://thealternativef1.streamlit.app/) under the Regulations & Settings sidebar dropdown.
                ''')
    st.markdown('''
                <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div>
                ''', unsafe_allow_html=True)
    st.markdown('''
                _The Alternative F1 League_
                <p style="color:lightgray;">Where racing meets integrity and fair competition.</p>
                ''',
                unsafe_allow_html=True,)
    st.markdown('''
                <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div>
                ''', unsafe_allow_html=True)
    st.divider()

# ----- How to add a GIF: ----- #
# gif = open('./Images/surfer.gif','rb')
# contents = gif.read()
# data_url = base64.b64encode(contents).decode('utf-8')
# st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Your GIF">', unsafe_allow_html=True)

# ----- How to add a Carousel ----- #
# carousel_images = [
#             {
#                 "title": "",
#                 "text": "",
#                 "img": "./Images/image.png"
#             },
#             {
#                 "title": "",
#                 "text": "",
#                 "img": "./Images/image.png"
#             },
#         ]

# carousel(items=carousel_images, interval=20000)