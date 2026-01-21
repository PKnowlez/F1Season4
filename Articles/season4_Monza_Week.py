import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

image = Image.open("./Images/Monza_Circuit.png")

def article():
    date = "Tuesday 01/20/2026"
    author = "Patrick"

    st.subheader('''Race Week: Monza''')
    st.markdown('''
                One more race to finalize the results. A season tighter than ever, all comes down to this. What a thrilling, competitive, spicy, and all around enjoyable season it has been.

                The league has been carried to new heights thanks to the talent, dedication, and excitement brought week in and week out by every driver and team. With all of the joy this season has brought, it is now time to decide who are champions will be, Mercedes or VCARB, Joshua or Jairo.
                
                Shockingly, this has never happened before within the league. Typically, one of the two championships is clinched prior to the final race. This year though, at the track that gifted us The Intern last season, we are going to be gifted a thrilling and tense battle for both championships.

                So how can each driver or team win it? For Joshua, all he needs to do is win. In fact, it is a little easier than that even. Simply put, Jairo can win the race and all Joshua has to do is finish 8th or higher. But a Joshua DNF and a Jairo win flips the championship to the Mercedes rookie.

                On the constructor side of things, Mercedes simply needs to score 10 points, not including bonus points. If they do, VCARB is mathematically out of it. However, with bonus points in play, that bumps the threshold for a championship up to 14 points. So how can VCARB flip the script? To simplify the math, the following is all without bonus points.
                
                If VCARB finishes 1-2 and Mercedes only scores 9 points, then the trophy goes their way. If VCARB finishes 1-3 and Mercedes scores 6 points, then the trophy goes their way. If VCARB finishes 2-3 and Mercedes DNFs, then it will be a tie on points. League officials are already discussing how to break a tie like this and have determined a few metrics to base it off of if the need arises.
                ''')
    st.image(image)
    st.markdown('''
                Monza is an excellent track to host such a tight battle. With two incredible DRS zones and the pedal to the floor for nearly 80 percent of the lap, drivers are going to burn through tires and battle with track limits for all 27 laps.

                Turn 1's chicane will likely provide fireworks throughout the race, but a few of the other braking zones might prove to provide unique overtaking moments if drivers are feeling brave. It will be a test of mental fortitude throughout and if there are safety cars, penalties could decide the race.

                Last time out the league was in shambles around the Temple of Speed. So much so that I was incapable of writing an effective article, and so my trusty intern was hired. Who knows what this race will have in store for the league, but if nothing else, it will bring resolution to a tumultuous season.

                **RUMOR MILL**

                As this article goes out, our intrepid report, The Intern, brought in some intriguing news. The team from Maranello has reportedly signed a second driver to replace league legend Erick. With this being such incredibly breaking news, we will do our due diligence to confirm the rumors within the next week and announce the new lineup there.

                Of course, rookie Leo will continue his drive with the team after showing an increase in skill over the last half of the season. Additionally, rumors still swirl about Audi or Williams or both. The Intern is set to interrogate (their words) one or both of the drivers in these conversations some time soon.

                Be on the lookout for new information over the next few weeks.
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

# ----- How to add a Video: ----- #
# video = "./Images/VideoFile.mp4"
# st.video(video, format="video/mp4", loop=False, autoplay=False, muted=False, width="stretch")

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