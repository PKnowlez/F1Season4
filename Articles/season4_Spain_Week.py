import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

circuit = Image.open("./Images/Spain_Circuit.png")
banner = Image.open("./Images/Spain_Banner.jpg")

def article():
    date = "Thursday 10/16/2025"
    author = "Patrick"

    st.subheader('''**BREAKING NEWS**''')
    st.markdown('''TWITCH TV TO RETAIN RIGHTS TO CURRENT LEAGUE STREAMS''')
    
    st.subheader('''Race Week: Spain''')
    st.image(banner)
    st.markdown('''
                IT'S RAWE CEEK!!! After an early season break the league returns to action in Spain. With the drama of Miami behind us, the league is primed and ready for a heater in Spain.
                
                While Miami posed a challenge for the drivers because of its tire wear and lack of maintained flow across a lap, Spain provides a new challenge with plenty of flow while still forcing drivers to combat tire wear and one another.

                Last season, the drivers took to Spain and had a jaw dropping race. Battles in the front, mid, and back field ensued throughout the entire race. After all the tire marbles settled, Alpine's Joshua took home the win but lost his incredible streak of Fastest Laps. McLaren's Nick and Ferrari's Erick finished on the podium respectively. 

                Then VCARB's Brently took home 4th place with retired Red Bull driver Yeti just behind him. Further back in 6th was VCARB's Patrick who took home the Fastest Lap after taking damage earlier in the race. Aston Martin's Del found himself finishing in 8th, with McLaren's Travis in 18th and Alpine's Eddie in 19th. The then Red Bull driver Boz, retired Ferrari driver Zane, and retired Aston Martin driver Gary all were unable to start the race.
                ''')
    st.image(circuit)
    st.markdown('''
                This year though, the competition seems a bit steeper up near the front, with multiple drivers and teams competing for wins and podiums. The drivers who make the most of their tires and avoid disaster early will likely bring home big point hauls in Spain.

                The circuit is not designed for catching up from too far back, so staying within the wake of the car in front will be critical for each driver. However, this could prove challenging as much of the track is comprised of high and medium speed turns that make it tough to follow with dirty air washing over a car's wings.

                Sector 1 is predominantly flat out, other than the medium-hard braking into Turn 1. From there the drivers will likely line up single file into the beginning of Sector 2 at the top of the initial hill climb.

                That braking zone may result in some side-by-side action going into Turn 5 where the driver's may have a decent non-DRS chance to make a few overtakes. Sector 2 then sweeps its way back uphill to the back straight where, after the first lap, we will likely see some DRS usage for overtakes or preparation for overtake on the front straight.

                The third sector of the track is filled with tricky corners for accelerating. Tires will be overheated in this sector as the race proceeds. The drivers near the end of the lap will find themselves going full throttle through the final few corners trying to avoid track limits into the long front straight. As they reapproach Turn 1, moments for overtaking are likely to occur as the combination of the slipstream, DRS, and ERS should allow for some ground to be gained into the braking zone.

                With all this said, this week's race should begin to show some trends for those who are contending for this season's crowns.
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
