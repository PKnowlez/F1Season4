import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

# memes = Image.open("./Images/Austria_Memes.png")
austria1 = Image.open("./Images/Austria/austria1.jpg")
austria2 = Image.open("./Images/Austria/austria2.jpg")
austria3 = Image.open("./Images/Austria/austria3.jpg")
austria4 = Image.open("./Images/Austria/austria4.jpg")
austria5 = Image.open("./Images/Austria/austria5.jpg")
austria6 = Image.open("./Images/Austria/austria6.jpg")
austria7 = Image.open("./Images/Austria/austria7.jpg")
austria8 = Image.open("./Images/Austria/austria8.jpg")
austria9 = Image.open("./Images/Austria/austria9.jpg")
austria10 = Image.open("./Images/Austria/austria10.jpg")

def article():
    date = "Thursday 12/11/2025"
    author = "The Intern"

    st.subheader('''Race Recap: Austria...so much carnage''')
    st.markdown('''
                WHAT A BANGER! Best race in a long time. Penalties everywhere, drivers crashing out literally and figuratively, and so many flipping safety cars.

                Making the memes for this one was a true honor. Truly blessed with this gift of a race. I am not even mad that I've got to write the recap part. This is gonna rock actually.

                So they try to start the race and Jaden goes MAD. Brother totally forgets to brake and turn, cutting a corner, smashing into Joshua (thank you), and doing so much damage the game bugs and gives people blue flags during a restart.

                This also gave Del the opportunity to show off his pilot skills, taking full flight and sending Brently into a laughing fit live on stream. Once the league got it all settled they got the race going and nearly made it half a lap without being a pathetic bunch of bumper car drivers.

                No cap, disappointing what we saw into turn 3. But alas the race goes on. And just two laps later Leo decides he doesn't like being teammates with Erick all that much and tries to straight up eliminate him. I kind of think bro must be playing Mortal Kombat too often and he just heard, "Finish Him" play in his head and made that move.

                This caused a mega long safety car that Erick barely beat out of the pits. Some laps went by and the squad elected another tribute to be annihilated, this time it was Nick. Straight into the pit wall like a numbskull.
                
                With all this going on, drivers were getting penalties left, right, and center. And truly, this mattered. A third safety car was triggered when Leo got a little reckless and slammed into an AI. With two laps left, the race restarted with Joshua, Jairo, and Jaden up front, all with penalties.

                Somehow, my boss came out on top while the other three tumbled down the results because of their poor driving skills. VCARB's rookie also suffered with a big chunk of penalties right at the end where he plummetted down the standings too.

                Fun fact, Patrick has literally never finished first when winning, bro is just a penalty merchant. Regardless, enjoy the memes. They slap. Oh and stay tuned for some rumors and an FIA announcement below.
                ''')
    # st.image(memes)
    st.image(austria1)
    st.image(austria2)
    st.image(austria3)
    st.image(austria4)
    st.image(austria5)
    st.image(austria6)
    st.image(austria7)
    st.image(austria8)
    st.image(austria9)
    st.image(austria10)
    st.markdown('''
                **RUMOR MILL ROUNDUP**

                Last time we wrapped the rumor mill up there were a few different rumors floating around the paddock. One of which was that a super alliance between two drivers signing with Cadillac and two drivers signing with Haas was coming together. Nothing new on who those drivers might be, but the alliance itself has been rumored to already exist this season.

                We also heard about a McLaren driver preparing for retirement, and now we are hearing that with that driver's departure the other may choose to sign with another perenial power house team. More to come on this as it evolves.

                More recently, we are hearing rumbles of trouble with our reigning champions. From practice contracts not being fullfilled, to something akin to the Kyler Murray COD effect going on as well. Could the dynamic duo break up? Only time will tell.
                ''')
    st.divider()
    st.markdown('''
                <div style="background-color: #97978F; padding: 10px; border-radius: 5px;">

                **Press Release** <br>
                **For Immediate Release** <br>
                Date: December 11, 2025 <br>
                From: The Stewards <br>
                To: All Competitors, All Teams <br>

                **SUBJECT:** Decision – Jaden Turn 1 Incident <br>

                **JADEN TURN 1** <br>
                **Summary** <br>
                As the race started, Jaden (Mercedes) cut Turn 1 and ran their front left tire into the rear right tire of Joshua (Alpine). Thiscaused both drivers to spin. Upon the Red Flag restart that ensued, many drivers were met with electrical and mechanical failures (game bugs) resulting in a full race restart.

                **Decision** <br>
                Per the new regulation on race restarts, Jaden should be subject to a mandatory last place start in the next race. However, because there was a full race restart and the regulation is new, league officials have chosen to bend the regulation and allow Jaden to qualify as high as 10th place. In other words, Jaden will be allowed to drive in Q1 and Q2 of the next full race they compete in.
                - Ineligibility to compete in Q3 at the next full race they compete in
                - 1 total penalty point for:
                    - Ruining Joshua's race position
                    - Ruining other driver's races subsequently when spun out on track
                    - Endangering multiple driver's races
                
                **DECISION ISSUED BY** <br>
                FIA Stewards - The Alternative F1 League <br>
                Red Bull Ring <br>
                December 11, 2025

                <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div> <br>

                <p style="color:lightgray;">The Alternative F1 League <br> Where racing meets integrity and fair competition.</p>
                ''', unsafe_allow_html=True)
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()