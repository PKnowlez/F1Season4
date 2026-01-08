import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

j1 = Image.open("./Images/Jeddah Vegas/Jeddah1.png")
j2 = Image.open("./Images/Jeddah Vegas/Jeddah2.png")
j3 = Image.open("./Images/Jeddah Vegas/Jeddah3.png")
j4 = Image.open("./Images/Jeddah Vegas/Jeddah4.png")
j5 = Image.open("./Images/Jeddah Vegas/Jeddah5.png")
j6 = Image.open("./Images/Jeddah Vegas/Jeddah6.png")
video = "./Images/Jeddah Vegas/Vegas.mp4"
v1 = Image.open("./Images/Jeddah Vegas/Vegas1.png")
v2 = Image.open("./Images/Jeddah Vegas/Vegas2.png")
v3 = Image.open("./Images/Jeddah Vegas/Vegas3.png")
v4 = Image.open("./Images/Jeddah Vegas/Vegas4.png")
v5 = Image.open("./Images/Jeddah Vegas/Vegas5.png")
v6 = Image.open("./Images/Jeddah Vegas/Vegas6.png")
jv1 = Image.open("./Images/Jeddah Vegas/JeddahVegas1.png")
jv2 = Image.open("./Images/Jeddah Vegas/JeddahVegas2.png")
jv3 = Image.open("./Images/Jeddah Vegas/JeddahVegas3.png")
jv4 = Image.open("./Images/Jeddah Vegas/JeddahVegas4.png")

def article():
    date = "Thursday 01/08/2026"
    author = "The Intern"

    st.subheader('''Race Recap: Jeddah & Las Vegas - Viva Las Double Header''')
    st.markdown('''
                **JEDDAH RECAP**
                
                First and foremost I must apologize for my lazy boss who didn't pen up a race week article...must have had you all lost out there not knowing where to overtake and stuff. Let's blame all your bad driving and mishaps on that, yeah? K cool.

                With that out of the way, let's talk about two of the most thrilling finishes we have seen this season. Jeddah, where we were just ~~one~~ ~~no two~~ three major mistakes away from a totally different podium. Let's start with the first big mistake. Reigning champ Nick calculated that the walls were made of pillows. His calculations were completely incorrect. First lap out there during qualifying, DNF.

                This guy might need to get his head checked after that one... Onto the second mistake. The master baker, Del, decided to snack on one too many little treats and also calculated that the walls were made of pillows mid-race. Taking himself from fighting for 3rd to sitting in the paddock.

                Now, the most egregious error of them all came from none other than the rookie phenom Jairo. With what some were calling the greatest strategy call of all time (insert eyeroll), Jairo put on a faster set of tires under safecty car and, well, wore them into the slipperiest set of rubber known to mankind. He found himself facing backwards multiple times during the final lap of the race spinning and spinning like a merry-go-round with a punctured rear tire.

                The race wasn't an entire bust though. Eddie from the backrow made it up into 7th. Nick, from even further back did manage to salvage his crappy qualifying and make it to 4th. The VCARB pair capitalized on everyone else's mistakes and took home a double podium. Erick made up a place or two as well, and finally, Joshua took home his second win in a row and this season. But let me immortalize a few of the glorious moments in memes below.
                ''')
    st.image(j1)
    st.image(j2)
    st.image(j3)
    st.image(j4)
    st.image(j5)
    st.image(j6)
    st.markdown('''
                **LAS VEGAS RECAP**
                
                Now, the league didn't just have one chance to mess things up, this was, of course, a double header. And boy howdy did they carpe the diem out of that opportunity. Eddie was simply too afraid to make another mistake so he bailed. Then he started chatting nonsense mid-qualifying about anime (the crowd truly booed), and his teammate cooked nearly every hot lap he tried. Alpine has really fallen from their throne after last year's win.

                In total these goons only mustered 7 finishers for this race. 9 started, 11 were present, and 3 gone with the wind. But this finish was like nothing we have ever seen before. No script, no skills, and a whole lot of luck lead to five drivers being right on top of each other coming out of the final braking zone on the track. This lead to a near three way tie for first. Now, you'd think the guy who was in first and started in second would be in that fight, but you would be wrong. Joshua was leading but this guy is allergic to staying within the white lines and so, because of how tight it was, he fell all the way to 5th after the smoke cleared.

                Jairo, Patrick, and Nick, all within 0.088s of each other, finshed in 1st through 3rd. Leo found himself just off the podium a few tenths back.

                A true masterpiece of a finish, that even I cannot truly meme on. Please enjoy a short clip of this excitement below as well as some glorious race memes.
                ''')
    st.video(video, format="video/mp4", loop=False, autoplay=False, muted=False, width="stretch")
    st.image(v1)
    st.image(v2)
    st.image(v3)
    st.image(v4)
    st.image(v5)
    st.image(v6)
    st.markdown('''Now, my friends, there were some moments and memes that superseded just one race. And so I present to you an assortment of memes that span the entirety of the double header evening.''')
    st.image(jv1)
    st.image(jv2)
    st.image(jv3)
    st.image(jv4)
    st.markdown('''
                **RUMOR MILL**
                
                There have been plenty of rumors this season, but we are nearing the end of our season. Which means, some of these rumors are about to go up in flames or come out as true through press releases. Sources are saying we will hear about the new look Red Bull team sometime next week as well as who is driving for Haas, Cadillac, and McLaren.

                But while those juicy rumors are soon to be made real, we've got something even bigger than that on the horizon. Reports are coming in that there has been massive flooding in Imola. The paddock is currently 8 feet deep in water. Parts of the track's surface are severely damaged due to debris overflowing and smashing into the surface at the onslaught of the flash flood.

                This is putting the season finale in jeapordy. But there is a rumor circulating that the Italian promoters of the event have identified a suitable substitute...

                **The Temple of Speed**

                So for those who have been simming in Imola, it might be time to begin practicing for the fastest lap of the year instead. Take this rumor as an official announcement, because there is no way y'all are running your cars in Atlantis, I mean, Imola in two weeks.
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