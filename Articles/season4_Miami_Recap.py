import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

sprint_memes = Image.open("./Images/miami_sprint_memes.png")
race_memes = Image.open("./Images/miami_race_memes.png")
joshua = Image.open("./Images/miami_joshua.png")
cover = Image.open("./Images/miami_cover.png")

def article():
    date = "Friday 10/10/2025"
    author = "The Intern"

    st.subheader('''Race Recap - Miami: Vice City Magic''')
    st.image(cover)
    st.markdown('''
                Tuh-tuh-tuh-today Junior, or, well, maybe next race. Last week one of the McLaren's served a race ban, and this week Alpine's Eddie simply decided not to show up. Something about "I'm going to a party and I don't care if my teammate needs me."

                But that's not where the juice was this week. No, no, no, the drama this week would give reality TV a run for its money. A fast paced sprint, a reverse grid race, restarts, virtual safety cars, safety cars, and a whole lot of FIA intervention.

                Honestly, y'all need to get it together with the race starts. Pit-i-ful. Also, veterans and rookies BOTH crashing out during safety cars, smh, pa-the-tic. Truly hard to watch.

                But let's talk the sprint. Teamwork? In The Alternative's league? WILD - truly wild. And to come from two rookies. IN-CRED-IBLE. A stunning sprint race from the Mercedes tandem. But that was pretty much the only positive thing I have in the notes from the sprint.

                The rest of y'all, dreadful racing. Turn 1 turned into a near standstill, Aston Martin's Boz turning himself into a spinning top and Alpine's Joshua forgetting that running into people is bad. Per the usual, my words can only be so good at retelling these tales.                
                ''')
    st.image(sprint_memes)
    st.markdown('''
                Enlightening right? Well, let me learn you something about the main race. Because it was stupid. Alpine's Joshua forgot that you have to start when the lights go out not while they are still on. An incredibly smooth brained maneuver that earned him an immediate driver through. SOMEHOW everyone just let him by and he finished third??? Do better people.

                But that was after the race actually started...and that did not happen right away...I'm surprised anyone kept watching any of the streams.

                You know what, I'm over it. Enjoy the memes and I'll be back at the end to do some "journalism" or whatever.
                ''')
    st.image(race_memes)
    st.markdown('''
                After the FIA put down the hammer on Mercedes' Jayden, the podium was finalized with McLaren's Nick, Red Bull's Brently, and Alpine's Joshua. Somehow the Alpine driver made up for his boneheaded decision at the start of the race and landed on the podium...maybe I should have saved that George Russell meme template for this guy instead of Patrick.

                This was McLaren's first win of the season and Brently's first podium of the season. But for both Nick and Brently, they were the stars of their teams while their teammates finished in 5th...and...well...Matthew didn't finish. Ferrari's Erick somehow started 4th and finished 4th with only Brently and two AI in front of him. Maybe he really is in his Daniel Ricciardo era.

                Aston Martin's Del and Mercedes' Jayden found themselves in pitched combat as well as being right near each other in the final standings as they probably would have been if not for the in-chi-dent.

                VCARB's Patrick and Ferrari's Leo also found themselves right next to each other, but instead of being up fighting for a podium they battled for 9th and 10th place respectively. A fall from graces for the driver who was leading the championship.

                Aston Martin's Boz rounded out those who finished in 11th. Comfortably ahead of the three rookies who DNF-ed. Really living up to their rookie standings I see. And of course, last but not least, Eddie scored a whopping 0 points and +1 penalty point throughout this week.

                The final results mean McLaren and Nick take over both championships. Maybe the team can close it out this year? But when I asked ChatGPT, it told me to go pound sand, Max Verstappen will make a comeback.
                ''')
    st.image(joshua)
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