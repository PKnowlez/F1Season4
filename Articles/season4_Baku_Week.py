import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

image = Image.open("./Images/Baku_Circuit.png")

def article():
    date = "Monday 11/03/2025"
    author = "Patrick"

    st.subheader('''Race Week: Baku''')
    st.markdown('''
                It's ~~Race~~ Chaos Week. The league has faced street circuits before and come out clean. However, none have been as treacherous as the one that lies in front of them this week.

                Baku is not just the track with the longest continuous full throttle section of the season, but also a track that the league will likely take heavy casualties during. Tight and narrow straights, heavy braking, sharp turns, and little to no run off means the drivers will need to be on their toes during every moment.

                Not to mention how strong tire wear will be during the hard acceleration zones after each full stop braking zone. In an effort to gauge the league's vibes heading into this one, our intern has been polling the league on how many safety cars and incidents we will see. Thus far the results are estimating at least one virtual safety car, two safety cars, and one red flag. Additionally some drivers are expecting there to be as many as ten DNFs during this race.
                ''')
    st.image(image)
    st.markdown('''
                Last season the league took to the streets in Azerbaijan and chaos did truly ensue. Eddie was on for potentially his first ever win, but crashed out at the top of the castle section. Nick found a tire hack and cruised into a victory with an incredible tire saving strategy, and only two of the league's drivers even finished in the top 10, with Patrick finishing in second. Promoted VCARB driver Brently finished in 11th with Travis, Boz, and Eddie behind. While Del met an untimely end, part way through the race. Erick, Joshua, Zane, Yeti, and Gary did not even make it to the starting line.

                The street circuit showed no mercy and it likely will not this go around. But for the drivers who do survive the heavy braking in the first turn, they will likely be rewarded with a VSC or SC. If the league survives the first turn altogether, they will likely be two wide going into the second turn and then begin to string out into a line on the way down to Turn 3. 

                After coming out through Turn 4 the drivers will head directly into the most technical sector of the track. The castle section invites drivers to push the double apex left turn to its very limits and brake just early enough to coast through the sweeping chicane at the top of the castle turret. From there a high speed sweeping turn, similar to what the drivers will face later this season in Jeddah, will take the drivers to the most technical braking zone of the season.

                The downhill, left hand, semi-blind turn will challenge every driver and will potentially catch a few out and end their fight for the podium this race. For those who survive, Sector 3 starts just around the next corner.

                Sector 3 is flat out, full tilt, and later in the race, a place where a lapse in judgement will likely see someone smashing into an outside wall. Yet again, for those who survive, the track's only true overtaking zone will occur on the front straight and into the first turn. While some may see Turns 2 and 3 as opportunities to overtake, in many cases drivers will be better off waiting until the start of the lap so that they do not need to defend down the front straight.
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