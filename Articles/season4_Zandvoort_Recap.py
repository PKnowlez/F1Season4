import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

z1 = Image.open("./Images/Zandvoort/Zandvoort1.jpeg")
z2 = Image.open("./Images/Zandvoort/Zandvoort2.jpeg")
z3 = Image.open("./Images/Zandvoort/Zandvoort3.jpeg")
z4 = Image.open("./Images/Zandvoort/Zandvoort4.jpeg")
z5 = Image.open("./Images/Zandvoort/Zandvoort5.jpeg")
z6 = Image.open("./Images/Zandvoort/Zandvoort6.jpeg")
z7 = Image.open("./Images/Zandvoort/Zandvoort7.jpeg")
z8 = Image.open("./Images/Zandvoort/Zandvoort8.jpeg")
z9 = Image.open("./Images/Zandvoort/Zandvoort9.jpeg")
z10 = Image.open("./Images/Zandvoort/Zandvoort10.jpeg")
z11 = Image.open("./Images/Zandvoort/Zandvoort11.jpeg")
z12 = Image.open("./Images/Zandvoort/Zandvoort12.jpeg")
z13 = Image.open("./Images/Zandvoort/Zandvoort13.jpeg")
application = Image.open("./Images/application.png")

def article():
    date = "Saturday 12/20/2025"
    author = "The Intern"

    st.subheader('''Race Recap: Zandvoort An Alpine Christmas Miracle''')
    st.markdown('''
                > No cap? I can do the memes first? - GOATed Intern
                >
                > Yeah whatever. - Jerk Boss

                That's right folks, we're doing dessert first this time. If you're a nerd and like the full recaps, I will still do one at the end of the memes. But we are diving straight into the memery.
                ''')
    with st.expander("DANK MEMES"):
        st.image(z1)
        st.image(z2)
        st.image(z3)
        st.image(z4)
        st.image(z5)
        st.image(z6)
        st.image(z7)
        st.image(z8)
        st.image(z9)
        st.image(z10)
        st.image(z11)
        st.image(z12)
        st.image(z13)
    st.markdown('''
                **NOT SO DANK RECAP**

                Ok so now that the whole race is spoiled by the memes, why even read this?
                
                Oh, ... you're still here ... er ... ok ... read on I guess, *under breath: weirdo...*

                The race got off to a pretty standard start, Erick was late, technical difficulties, Eddie didn't pick his tires, etc. Qualifying was pretty standard except for that moment when Del railed the banked corner's high wall.

                His pit crew got him back out for Q2 though so that was pretty epic. After qualifying finished Erick hopped into a car and started from last. Jaden was also starting out of position because he was essentially in league timeout for being naughty in the last race's start.

                The race started uneventfully, honestly pretty lame of everyone not to just take each other out in turn 1. Whatever. The lap was going well until Jairo double, or maybe triple, tapped Nick. Take him out for dinner first mate. That caused some debris to fly right under Eddie's tires causing a lovely puncture that truly blessed viewers with some magical Eddie wanking and tire GOATed tire management.

                Most of the race was pretty standard after that with standout moments from Jaden and Newman who flew up the ranks. Patrick, once again, did nothing and got a podium. Seems like he's the new sheriff in town if you catch my drift.

                Oh and I guess Joshua finally won a race or something. He was all giddy about it. Negative aura if you ask me.

                **RUMOR MILL**

                Even with his win, Joshua is not content with his situation at Alpine. This is less of a rumor and more of a PSA, homie wants a teammate that wants to win it all next season. He provided The Alternative F1 Media with a teammate application. Please review below and submit directly to Joshua for further considerations.
                ''')
    st.image(application)
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