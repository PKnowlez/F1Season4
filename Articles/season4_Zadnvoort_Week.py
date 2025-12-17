import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

image = Image.open("./Images/Netherlands_Circuit.png")
cover = Image.open("./Images/Zandvoort.jpg")

def article():
    date = "Tuesday 12/16/2025"
    author = "Patrick"

    st.subheader('''Race Week: Zandvoort''')
    st.image(cover)
    st.markdown('''
                What an incredible season thus far. Competitive, thrilling, and passionate all around. With five races to go, there has never been a tighter battle for the Driver's Championship. And while the Constructor's Championship is not as tight, there are still plenty of points still on the table.

                After the league survived Austria for a second time, a new driver took the lead of the Driver's Championship. Last season's runner up, and primary Alpine driver, Joshua has taken the lead by just three points.

                McLaren's Nick and VCARB's Patrick swapped places as well, while Mercedes' Jaden closed the gap to the top four just to make things a bit more exciting.

                On the Constructor's side, both Alpine and VCARB closed a small amount on Mercedes. But enough with the season recap, it is time for some analysis of what the drivers should expect in Zandvoort this week.
                ''')
    st.image(image)
    st.markdown('''
                When the lights go out, drivers will accelerate down a moderately short starting straight. As they enter the first corner, every driver will need to keep their whits about them as the right hand curb butts directly up against a race ending wall. As drivers proceed through the first corner, the exit could potentially spin out a driver or two on the steep raised curbs.

                This is a theme in Zandvoort. Many of the exit corners have steep, brightly colored, and extremely dangerous curbs that can send a driver straight into a DNF if they are not careful. After surviving the first couple of turns, drivers will be met with the tightly banked fourth corner.

                Here we may see some late braking high-to-low overtaking for the drivers who have soft or medium tires strapped on. Those with hard compound tires will be hoping they can keep it on the circuit as they proceed into the high speed winding esses that conclude Sector 1.

                The next Sector is the most braking intensive of the track and is dangerously narrow in some areas. With killer curbs on many turns, Sector 2 will likely be a parade for most of the race.

                But as the drivers leave Sector 2 and enter the next, there will be a chance to close the gap with a small dose of DRS into the modified chicane at the end of the back straight. As drivers exit that section, they will be met with the most dangerous curb on track just before the insanely high speed banked corner leading to the front straight. This portion of the track could provide a thrilling drag race to the finish line on the final lap.

                The league has faced the famous circuit twice before. In both times Erick and Nick have found the podium. Erick won the first outing and Nick won the second. Surprisingly during the first race, no one from the league finished third. However, this year's chmpionship leader Joshua finished third on the podium last time out.

                **RUMOR MILL UPDATE**

                In a surprising twist, McLaren has squashed the rumor that they are losing both of their drivers and have officially resigned Nick to a year-to-year deal. Travis has not officially confirmed that he is leaving the team, but all signs point towards a new role for him in the FIA in the coming season.

                The newest rumor points towards McLaren looking to sign a veteran driver who is in search of a turn-around season next year. With these signings and rumors, silly season has somehow begun with five races left in the championship. When approached about this, Erick was very coy with his answers. Our beat reporter (Intern) believes this is a sign that he may be the mystery signing. Only time will tell.
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