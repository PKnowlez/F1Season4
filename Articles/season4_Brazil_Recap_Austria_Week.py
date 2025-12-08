import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

erick0 = Image.open("./Images/Brazil/erick0.jpg")
erick1 = Image.open("./Images/Brazil/erick1.jpg")
erick2 = Image.open("./Images/Brazil/erick2.jpg")
erick3 = Image.open("./Images/Brazil/erick3.jpg")
erick4 = Image.open("./Images/Brazil/erick4.jpg")
erick5 = Image.open("./Images/Brazil/erick5.jpg")
erick6 = Image.open("./Images/Brazil/erick6.jpg")
erick7 = Image.open("./Images/Brazil/erick7.jpg")
erick8 = Image.open("./Images/Brazil/erick8.jpg")
joshua1 = Image.open("./Images/Brazil/joshua1.jpg")
joshua2 = Image.open("./Images/Brazil/joshua2.jpg")
austria = Image.open("./Images/Austria_Circuit.png")

def article():
    date = "Sunday 12/07/2025"
    author = "A Patrick and The Intern Production"

    st.subheader('''Race Recap: Brazil & Race Week: Austria''')
    st.markdown('''
                That's right, a two for one article. Even better yet, my boss Patrick and I are co-authoring this. That means I am simply sticking to the memes and he is going to do all the boring official nonsense.

                So to start this off, please skip his boring sprint and race recap. You'll find a nice little roast of our great leader Erick and his absolute dumpster fire of a race just afterwards. Just go straight there tbh.

                **RACE RECAP**

                As our illustrious intern pointed out, this is a co-authored double trouble article. The first section here will be a quick synopsis of the sprint qualifying and sprint, followed by a detailed analysis of the full race itself.

                Qualifying was a single session shootout for all who were able to make it. This is an important note because both the Aston Martins of Boz and Del were unable to make it as well as McLaren's Travis. With those drivers out, the league got to it and Joshua found himself on top of the leaderboard once again.

                Behind him were the two Mercedes of Jairo and Jaden followed closely by Nick. With the first two rows of the grid set, the Red Bull and VCARB teams sorted in from 5th to 8th with Patrick, Josh, Matthew, and Brently. The second Alpine, Eddie, found himself in 9th with the two Ferraris in 10th and 11th. Notably, rookie Leo out qualified his senior teammate Erick.

                The sprint itself had a few intriguing moments as Jaden spun out early and found himself fighting in the mid-field. Erick tumbled from his starting position to last, and Leo and Eddie fought for the final two points scoring positions. Joshua, Jairo, and Nick found themselves on the podium and subsequently starting in the back of the main race.

                The main race itself was full of shocking overtakes, mid-filed battles, and unprovoked errors that lead to Jaden taking home his first win of the season. Joshua, Nick, and Patrick all finished above current championship leader Jairo, beginning to close the gap in the standings. 

                Further down the field, Josh battled back from a minor incident with Joshua, which cost him a few positions. Leo and Eddie were once again found scrapping for 7th and 8th, and the Red Bulls brought home a double points finish.

                However, the most noteworthy moments were all centered around Ferrari's Erick. With crumby connection issues and tens of penalities, Erick simply had quite the evening. For the more detailed review, I will turn the reigns back over to the intern for some lovely roasting.
                ''')
    with st.expander("**THE ROAST OF ERICK**"):
        st.markdown('''
                    Ok, so, this dude Erick, what a poo-storm of a race. From joining the session to the sprint to the race itself, Erick could not find a single moment of success this week. He did, however, finish the race...sorta...
                    
                    Let's start with this boomer trying to just boot the game and join the session. Homie could barely login.
                    ''')
        st.image(erick0)
        st.image(erick1)
        st.image(erick2)
        st.image(erick3)
        st.markdown('''
                    You'd think once he got into the lobby things would, well, be smooth. Wrong. The below memes summarize Erick's eventful participation in this week's race.
                    ''')
        st.image(erick4)
        st.image(erick5)
        st.image(erick6)
        st.image(erick7)
        st.image(erick8)
        st.markdown('''
                    All in all, a very Ferrari coded race. Oh, and Patrick mentioned the Josh on Josh crime. I've taken the liberty to ensure Joshua does not escape with literally zero punishment for him crimes.
                    ''')
        st.image(joshua1)
        st.image(joshua2)
    st.subheader('''Race Week: Austria''')
    st.markdown('''
                With the intern's roasting of Erick and a few strays to Newman and Joshua over, it's time to do an abbreviated race week article for Austria. The shortest circuit on the calendar rears its head again. This time, in the clockwise direction.
                
                Unlike the league's last outing here in reverse, this time there is ample data from previous seasons to analyze. In fact, this is a perenial staple on the league's set of tracks. For the fourth time, the league will rip laps around the Red Bull Ring. There has never been a repeat winner where the hills are alive with the sound of V6 engines.

                So what does all this mean? Realistically, it means a current league favorite is likely to win the race. In each previous season, the winner of this race was in contention for the title at the time of their win here.

                But, that does not rule out the rest of the league. This track is known for early and late safety cars pulling the drivers back together. It is extremely likely that the league encounters a safety car this week. Will it be timed perfectly to allow for opportune pit stops? Only time will tell.
                ''')
    st.image(austria)
    st.markdown('''
                As driver's put the pedal to the floor, they will race up a steep incline to the even sharper right hand Turn 1. From there the drivers will likely all be side-by-side into Turn 2 and continuing up the hill to Turn 3.

                Turn 3's hard braking zone will prove to be an opportune time to overtake and can even be timed to allow for the overtaking driver to takeoff with DRS down the next straight.

                Sector 2 then progresses to wrap back downhill with twisting sweepers and narrow straights into the full tilt final two corners where track limits are sure to become a challenge. With such a short circuit, we are bound to see cars lapped, drivers battling, and incidents here, there, and everywhere.
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