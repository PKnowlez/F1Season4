import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

image = Image.open("./Images/image.png")
cover = Image.open("./Images/Baku/...")
patrick1 = Image.open("./Images/Baku/...")
patrick2 = Image.open("./Images/Baku/...")
cover = Image.open("./Images/Baku/...")
cover = Image.open("./Images/Baku/...")
cover = Image.open("./Images/Baku/...")
cover = Image.open("./Images/Baku/...")
cover = Image.open("./Images/Baku/...")
cover = Image.open("./Images/Baku/...")
cover = Image.open("./Images/Baku/...")
cover = Image.open("./Images/Baku/...")

def article():
    date = "Thursday 11/06/2025"
    author = "The Intern"

    st.markdown('''
                <div style="background-color: #97978F; padding: 10px; border-radius: 5px;">

                **Press Release** <br>
                **For Immediate Release** <br>
                Date: November 06, 2025 <br>
                Time: 5:30PM Mountain <br>
                From: The FIA and The Stewards <br>
                To: All Competitors, All Teams <br>

                **SUBJECT:** Decision – Baku Incidents: Eddie & Leo, Travis & Eddie, Erick & Boz, Josh <br>

                **DESCRIPTION OF INCIDENTS** <br>
                Eddie (Alpine) was stalled on the racing line in Sector 3 during a VSC around a blind corner, where Leo (Ferrari) ran into the back of Eddie.

                Travis (McLaren) lost control of his vehicle after hitting a wall in the middle of Sector 2, and collided with Eddie (Alpine).

                Erick (Ferrari) was given an in race 10 second penalty while two cars covered the entire width of the track due to a collision with Boz (Aston Martin).

                Josh (VCARB) was given an in race 10 second penalty while navigating between two sideways cars on the track.

                **FINDINGS & DECISION: Eddie & Leo** <br>
                Upon reviewing footage and the nature of the blind turn, the FIA and Stewards have determined that Eddie could have made evasive maneuvers to get off of the racing line in a blind corner. Due to this, Eddie caused the incident with a nearly defenseless Leo. Per league regulations, Eddie will have a 5 place penalty added to his finishing place and a penalty point added to his super license. Due to other circumstances, Eddie did not finish the race, and therefore his final standing will still be classified as DNF regardless of the penalty.

                **FINDINGS & DECISION: Travis & Eddie** <br>
                After reviewing all mitigating circumstances and potential outcomes, the FIA and Stewards have come to a final verdict that Travis is at fault for teh collision with Eddie. Travis had opportunities to safely come out of AI control or retire the car that could have eliminated this outcome. Therefore, because Eddie's race was ended, Travis will be penalized for 5 places to his finishing position as well as have a penalty point added to his super license. Due to this incident, Travis did not finish the race, and therefore his final standing will still be classified as DNF regardless of the penalty.
                
                **FINDINGS & DECISION: Erick & Boz** <br>
                After reviewing the data, it is clear that the 10 second penalty provided to Erick during the race was unfairly awarded. Therefore, he will have 10 seconds removed from his finishing position, pushing him up the standings 1 position into 6th.

                **FINDINGS & DECISION: Josh** <br>
                While reviewing onboard footage, it is clear that Josh did not contact any of the vehicles in the accident. Therefore, Josh will be granted his 10 seconds back on his finishing time which results in his final place being 5th.

                **FURTHER NOTES** <br>
                The FIA Stewards remind all competitors that situational awareness and car control remain the driver’s responsibility at all times, this includes when a car is damaged. Communication is critical in scenarios like this. Additionally, league officials would like to remind all drivers that clean driving is critical to the competitiveness of the league. As the season continues, we wish each driver the best of luck and look forward to seeing how the season progresses.

                **DECISION ISSUED BY** <br>
                FIA Stewards - The Alternative F1 League <br>
                Baku City Circuit <br>
                November 06, 2025

                <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div> <br>

                <p style="color:lightgray;">The Alternative F1 League <br> Where racing meets integrity and fair competition.</p>
                ''', unsafe_allow_html=True)  

    st.subheader('''Race Recap: Skibidi Toilet Baku My Dudes''')
    st.image(cover)
    st.markdown('''
                Alright, with all that vibe killing stuff out of the way, it's time review the turbo mess that was Baku. Drivers crashing from Lap 1 all the way to the end. Even the top contenders sucked, damaging wings early and late.

                I have decided that it is time to revamp the format as well. No one will be safe in this new format. Each driver is going to be ripped into mercilessly with memes and mini-recaps of their race.

                To make this happen though, I had to make a deal with the boss. Before the memes begin, I will do a micro-recap of qualifying and the race. Enjoy the boring stuff, or skip it and go check out the memes (do that, no cap this next part blows).

                **QUALIFYING**
                Pretty standard qualifying, honestly. No real shakeups. Well...except the catastrophe at the end of Q1. VCARB driver Josh started singing 'Jesus Take the Wheel,' and demolished his entire car after already making it into Q2.

                Bro must have tipped his mechanics big time becase they got the car back together for him ASAP and he started from last on the grid for the race.

                Mercedes' Jairo took home another pole position with Alpine's Joshua right behind. Honestly, I thought Joshua was fast, but he's getting obliterated this season in qualifying. Shmuck. Last year's champ and race winner also dropped a stinker and qualified in 5th.

                **RACE**
                The race was dumb. Safety Cars left right and center. Even a Red Flag occurred. Which was boring just staring at nothing until the drivers got rolling again. But whatever.

                After the Red Flag drivers decided to be as dull as possible. Barely any overtakes, no real meaningful pitstop strategies, and truly nothing out of the ordinary.

                That was until Alpine's Joshua decided to stink it up again. But more on that below. The race finished with 1 & 2 how they started and somehow McLaren's Nick made up ground on these guys...oh, I am getting word that is because the drivers in front of him both hit walls, gotcha, nice job Patrick and Jaden.

                Ok, onto the good stuff. As always, enjoy.
                ''')
    with st.expander('DNF - Patrick'):
        st.image(patrick1)
        st.image(patrick2)
        st.markdown('''
                    This dude reeks, homie couldn't even keep it on track and finish a lap, sheesh. No cap, people calling him a contender are a few nuggets short of a Happy Meal. 
                    ''')
    with st.expander('DNF - Eddie'):
        st.image(eddie)
        st.markdown('''
                    I honestly thought I was going to get an article where this dude doesn't do something ridiculous, but nah, homie tries overtaking an AI and gets bodied. Starting to feel like back-to-back Constructor's championships are gone for Alpine because of moments like these.
                    ''')
    with st.expander('DNF - Travis'):
        st.image(travis)
        st.markdown('''
                    Honestly though, could have been galaxy brained to stay in the pause menu, psych.
                    ''')
    with st.expander('DNF - Boz'):
        st.image(boz)
        st.markdown('''
                    Truly a series of unfortunate events here. But what's actually insane is that this guy is able to crash into other people and they get the penalty instead of him. Whatever hacks he has running Eddie probably needs to install.
                    ''')
    with st.expander('10 - Leo'):
        st.image(leo1)
        st.image(leo2)
        st.markdown('''
                    Watching the onboard for this moment was bonkers. This guy turns a corner and BANG Eddie is just parked. Big ups for finishing the race after that. Most guys would have been done done.
                    ''')
    with st.expander('9 - Brently AKA Captain Slow'):
        st.image(brently)
        st.markdown('''
                    Who needs four tires and to be on the lead lap? Not this guy. No cap, I would have thrown my controller through the screen if that BS happened to me.
                    ''')
    with st.expander('8 - Matthew'):
        st.image(matthew1)
        st.image(matthew2)
        st.markdown('''
                    It might not have been his best finish, but at least bro finished. Also, first race moving forward in the standings from qualifying, maybe this guy is the real Red Bull #1.
                    ''')
    with st.expander('7 - Del'):
        st.image(DEL)
        st.markdown('''
                    BRUTAL, homie does everything he can to finish this year and still ends up two places behind due to some buggy penalties. Baku will likely haunt this guy forever. Some might even say he's cursed here.
                    ''')
    with st.expander('6 - Erick'):
        st.image(erick1)
        st.image(erick2)
        st.markdown('''
                    Horror show from this guy. First question, who puts the soft tires on? Second question, who puts on used soft tires in a race? Answer(s): Erick.
                    ''')
    with st.expander('5 - Josh'):
        st.image(josh1)
        st.image(josh2)
        st.markdown('''
                    A completely shocking race day from this guy. Who forgets to hold onto their STEERING WHEEL AT 200 MPH?!!? I guess 15th to 5th is kinda sick though.
                    ''')
    with st.expander('4 - Jaden'):
        st.image(jaden1)
        st.image(jaden2)
        st.markdown('''
                    No wall was safe from a bump from this guy or his Mercedes teammate. Somehow they both never crashed out...someone needs to investigate the Mercedes engineering department for sure.
                    ''')
    with st.expander('3 - Nick'):
        st.image(nick1)
        st.image(nick2)
        st.markdown('''
                    Potentially the quietest race we have ever seen from this dude. You might of thought he was 20 seconds ahead. But nah, he was more the Oscar Piastri to Joshua's George Russell in Mexico if you catch my drift.
                    ''')
    with st.expander('2 - Joshua'):
        st.image(joshua1)
        st.image(joshua2)
        st.markdown('''
                    To quote the man himself "Lock IN!"
                    ''')
    with st.expander('DNF - Patrick'):
        st.image(jairo1)
        st.image(jairo2)
        st.markdown('''
                    A dubs a dub I guess. Maybe next time he will finish with all his end plates and on the top step. But for now he is skyrocketing up the standings.
                    ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()