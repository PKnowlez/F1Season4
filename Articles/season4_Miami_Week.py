import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

header = Image.open("./Images/Miami_Header.jpg")
circuit = Image.open("./Images/Miami_Circuit.png")

def article():
    date = "Saturday 10/04/2025"
    author = "Patrick"

    st.subheader('''Race Week: Miami''')
    st.image(header)
    st.markdown('''
                With the drama of Bahrain solidly in the rearview mirror, the drivers have their eyes set on Miami's Hard Rock Stadium. A temporary street circuit with high speed turns, low speed thrills, and plenty of passing opportunities; Miami should provide some excellent racing.

                On top of the circuit itself, the league will be facing its first sprint of the year. That means drivers and teams need to come prepared with multiple tire strategies and the right setup to be fast during a short stint but safe on tires in a longer stint.

                Drivers will qualify in an abbreviated qualifying format and head into the sprint race. Finishing position means everything for the points and for starting position during the main race. The race's grid will be set in reverse order from the final standings of the sprint race, likely lining up early championship front runners in the backfield and enabling huge opportunities to level the playing field across the standings.

                When the lights go out, the drivers will accelerate up to Turn 1 where heavy braking could induce some incidents. In the best case scenario, the drivers all make it out unscathed and rapidly rip through Turns 2 & 3 on their way into the complicated esses of Turns 4, 5, & 6. At this point the drivers are likely to be lined up like ducks in a row following the leader into Sector 2.

                While there are a few bends between Turns 8 and 11, the drivers will be slipstreaming down this nearly straight high speed section. In later laps, this will serve as a primary overtaking location with the aid of DRS and a good exit from Turn 8. However, during Lap 1 the drivers are likely to keep it steady through here and prepare to attack in Sector 3 under heavy braking going into Turn 17 or early on the front straight and into Turn 1.
                ''')
    st.image(circuit)
    st.markdown('''
                The league hasn't had an official race in Miami since Season 1 where Miami's biggest hater (McLaren's Nick) took home the win with a double podium for the then Mercedes drivers Erick and Marcus.

                Nick and Erick both qualified where they finished, but Marcus battled up from 5th to finish on the podium. McLaren's Travis fell from qualifying 3rd into finishing in 9th. Then Red Bull driver Boz qualified in 6th and battled up to 4th with then Aston Martin driver Zane doing nearly the exact opposite, going from 4th to 7th.

                The league recorded a pre-season session in Miami at the onset of Season 3 where Alpine's Joshua took home the win with Nick and VCARB's Patrick rounding out the podium. Ferrari's Erick missed the podium by mere seconds landing himself in 4th with Red Bull's Yeti and Boz in 16th and 17th respectively, and Aston Martin's Del and Gary in 18th and 19th respectively.

                With a sprint and reverse grid race in play, this week's race has the ability to really shift the standings early on and create an even playing field for many of our drivers going into the first break of the season.
                ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
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