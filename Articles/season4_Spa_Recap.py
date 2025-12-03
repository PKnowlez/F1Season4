import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

pk2 = Image.open("./Images/Spa/PK_roast2.png")
pk3 = Image.open("./Images/Spa/PK_roast3.jpg")
pk4 = Image.open("./Images/Spa/PK_roast4.jpg")
pk5 = Image.open("./Images/Spa/PK_roast5.jpg")
pk6 = Image.open("./Images/Spa/PK_roast6.jpg")
pk7 = Image.open("./Images/Spa/PK_roast7.jpg")
jo1 = Image.open("./Images/Spa/joshua_roast1.jpg")
jo2 = Image.open("./Images/Spa/joshua_roast2.jpg")
js1 = Image.open("./Images/Spa/Josh_roast1.jpg")
js2 = Image.open("./Images/Spa/Josh_roast2.jpg")
leo1 = Image.open("./Images/Spa/leo_roast1.jpg")
leo2 = Image.open("./Images/Spa/leo_roast2.jpg")
leo3 = Image.open("./Images/Spa/leo_roast3.jpg")
leo4 = Image.open("./Images/Spa/leo_roast4.jpg")
lg1 = Image.open("./Images/Spa/league_roast1.jpg")
lg2 = Image.open("./Images/Spa/league_roast2.jpg")
lg3 = Image.open("./Images/Spa/league_roast3.jpg")
lg4 = Image.open("./Images/Spa/league_roast4.jpg")
rb1 = Image.open("./Images/Spa/RB_roast.jpg")
ea1 = Image.open("./Images/Spa/EA_roast.jpg")

def article():
    date = "Monday 12/01/2025"
    author = "The Intern"

    st.subheader('''Race Recap: Spa - The Roast''')
    st.markdown('''
                In a McConaughey accent "Alright, alright, alright, I think it's time for some roastin'. "

                That's right folks, today the long wait is over. I have assembled a great army of memers to roast Patrick, Joshua, and Leo along with a few select memes about the rest of the league.

                Spa was an actual disaster and I needed this whole Thanksgiving break simply to watch the replays and determine who was truly at fault. And I have come to my decision. It's all of you. Flipping get better at racing you big bunch of benders.

                Anyway, per the usual, I am forced to author a "hIStoRicaLlY aCcuRaTE" (insert Spongebob arms) race recap before roasting. So skip this next section like normal and get onto the good stuff.

                **OFFICIAL RECAP - AKA MY BOSS' MANDATORY BS**

                A night at the Spa was anything but that. It was a sprint night to begin with, which means the Mercedes duo who can't start from the back were in for some trouble. League officials made it clear that no funny business would be tolerated to gerrymander the sprint results and get a better starting position.

                So after qualifying, the Mercedes boyz were 2nd and 3rd with Joshua finally finding some form and qualifying 1st. Behind the top three were the VCARBs followed closely by Nick, Matthew, Eddie, and Brently. Further down the field some guys just simply forgot how to perform a hot lap with Erick, Boz, and Leo starting 13th-15th.

                But, while qualifying was a disaster for a number of reasons, the session ended and we got to the sprint itself. It got off to a surprisingly ok start...unless you're Brently, then you will likely want to forget the lights ever went out.

                However after some shuffling and a few mistkaes here and there, everyone made it back to the pit who started. Travis and Del though, they never showed up.

                The race grid was then set, and after numerous restarts because these guys seem to forget where their brake pedals are every week, the race got underway.

                Jaden and Jairo started last with Patrick and Joshua in front of them as the top four from the sprint. But they did not stay in the rear too long.

                After some smooth passing and some...well...ridiculously ballsy passing concluded, the league found themselves nearly fully right side up just before a safety car struck. A total disaster-class for VCARB's Josh as he forgot to pit under the safety car and likely lost the race due to it.

                Others were much luckier and cruised in for fresh tires. As the rest of the race proceeded, another safety car struck right near the end. This bunched up the psychos and the more subdued drivers and allowed for one psycho in particular to pit for fresh soft tires.

                This one particular driver was Joshua. But I will not recount the tales of the final few laps here, instead you can simply know that Nick ended up winning and the VCARBs found themselves flanking him on the podium.

                **THE ROASTS**

                Before this whole section begins, I want to take a moment to thank the great memers of the league. Josh, Newman, Nick, Travis, and others who provided ideas, you are all appreciated. Mostly because I am lazy and had no desire to do anything remotely creative over the break, lol, get taken advantage of newbs. And with that, enjoy the roasts.
                ''')
    with st.expander('''**THE ROAST OF PATRICK**'''):
        gif = open('./Images/Spa/PK_roast1.gif','rb')
        contents = gif.read()
        data_url = base64.b64encode(contents).decode('utf-8')
        st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Your GIF">', unsafe_allow_html=True)
        st.image(pk2)
        st.image(pk3)
        st.image(pk4)
        st.image(pk5)
        st.image(pk6)
        st.image(pk7)
    with st.expander('''**THE ROAST OF JOSHUA & JOSH**'''):
        st.markdown('''
                    That's right, these two both had a howler and deserve to be jointly roasted because who ever knows which is which anyways.
                    ''')
        st.image(jo1)
        st.image(jo2)
        st.image(js1)
        st.image(js2)
    with st.expander('''**THE ROAST OF LEO**'''):
        st.image(leo1)
        st.image(leo2)
        st.image(leo3)
        st.image(leo4)
    with st.expander('''**THE ROAST OF THE LEAGUE**'''):
        st.image(lg1)
        st.image(lg2)
        st.image(lg3)
        st.image(lg4)
        st.image(rb1)
        st.image(ea1)
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()