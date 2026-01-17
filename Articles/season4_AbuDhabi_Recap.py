import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

ad1 = Image.open("./Images/Abu Dhabi/ad1.png")
ad2 = Image.open("./Images/Abu Dhabi/ad2.png")
ad3 = Image.open("./Images/Abu Dhabi/ad3.png")
ad4 = "./Images/Abu Dhabi/ad4.mp4"
ad5 = Image.open("./Images/Abu Dhabi/ad5.png")
ad6 = Image.open("./Images/Abu Dhabi/ad6.png")
ad7 = Image.open("./Images/Abu Dhabi/ad7.png")
ad8 = Image.open("./Images/Abu Dhabi/ad8.png")
ad9 = Image.open("./Images/Abu Dhabi/ad9.png")
ad10 = Image.open("./Images/Abu Dhabi/ad10.png")
ad11 = Image.open("./Images/Abu Dhabi/ad11.png")
ad12 = Image.open("./Images/Abu Dhabi/ad12.png")
ad13 = Image.open("./Images/Abu Dhabi/ad13.png")
ad14 = "./Images/Abu Dhabi/ad14.mp4"
McLaren = Image.open("./Images/Silly Season/McLarenS5.png")
Cadillac = Image.open("./Images/Silly Season/CadillacS5.png")

def article():
    date = "Friday 01/16/2026"
    author = "The Intern"

    st.subheader('''Race Recap: A Turbulent Penultimate Race''')
    st.markdown('''
                Nothing gives me more pleasure than to tell you all that my boss is out of the running for the Driver's Championship. Well...there is one thing that gives me more pleasure, both championships are coming down to the last dang race.

                INCREDIBLE!

                The script writers have done some immaculate work here. Jairo vs. Joshua, VCARB vs. Mercedes. All the pressure on Jairo to not DNF. All the pressure on Jaden to pull it back together. All the pressure on Joshua in a position he has never been in before. All the pressure on the sophomore and rookie lineup at VCARB.

                Spectacular. But enough about what is coming up. Patrick will do a crappy job explaining that in a future article I'm sure. Let's get into ripping memes. Well, first a little play-by-play.

                Qualifying was mostly uneventful. Patrick sucked more than usual during it, Leo started showing out a bit, and Josh showed why the whole #1 driver thing is on his mind. With the race underway the first stint saw a handful of good overtakes and battles. Tight stuff up front, strong back and forths from the mid-field, and the AI were riding in the back.

                However, this led to a  rookie mistake by VCARB rookie Josh. From there, his teammate made sure that he was more embarrassing than the rookie. Patrick, for the second time in Abu Dhabi, ran right into the wall of the third corner. Bro sucks here.

                This led to a safety car that cooked Nick and Josh's strategies. Everyone was tight and battles commenced, but not until after Del and Eddie decided to have a dumb off and blockade the hotel section. Much of the second stint was good racing, and some strategic defending that brought the group close together. And then, Brently smashed into the pit wall. 

                Safety car number two deployed. Which led to one of the most CHAOTIC restarts of all time. Some one slammed on their brakes or someone wasn't paying attention (i.e. Lance Stroll into DR in Canada 2024). But whatever the truth is, Nick's car went flipping flying. It was beautiful. Truly gorgeous. Masterpiece. Art. Don't worry, I've got a clip below. Simply gorgeous.

                The race finished without much other chaos, and Jairo won yet another one. Now, enjoy some memes.
                ''')
    st.image(ad1)
    st.image(ad2)
    st.image(ad3)
    st.video(ad4, format="video/mp4", loop=True, autoplay=True, muted=False, width="stretch")
    st.image(ad5)
    st.image(ad6)
    st.image(ad7)
    st.image(ad8)
    st.image(ad9)
    st.image(ad10)
    st.image(ad11)
    st.image(ad12)
    st.image(ad13)
    st.markdown('''**ART**''')
    st.video(ad14, format="video/mp4", loop=False, autoplay=False, muted=False, width="stretch")
    st.markdown('''
                **RUMOR MILL**
                
                So don't worry there are still rumors galore. From continued talks with both Williams and Audi for Del and Boz, to a new spicy rumor out there about one of our contenders.

                Mercedes seems to have lost their dynamic pairing. No word yet on where they will both go, and who they will join. But speaking of loss...it looks like Leo might be losing his teammate officially.

                Some official bombshell news has dropped. Both Erick's fate and the super team rumor are coming to a close. Enjoy the Silly Season posts.

                **SILLY SEASON**

                McLaren Announcement
                ''')
    st.image(McLaren)
    st.markdown('''Cadillac Announcement''')
    st.image(Cadillac)
    st.markdown('''
                So two league legends are joining forces, and the Red Bull/VCARB super team seems to be going All American together next season. More rumors will continue to unfold, but for now, the Silly Season announcements have all dried up, at least the official ones. Stay tuned.
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