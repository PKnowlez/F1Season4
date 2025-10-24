import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

qualifying = Image.open("./Images/Spain Qualifying.png")
race = Image.open("./Images/Spain Race.png")
alpine = Image.open("./Images/Spain Alpine Statement.png")

def article():
    date = "Friday 10/23/2025"
    author = "The Intern"

    st.subheader('''Alpine Team Statement: Spain Incident''')
    st.image(alpine)

    st.subheader('''Race Recap: Spain - Un Tango Turbulento''')
    st.markdown('''
                Now that's what I call racing. Dirty air, mistakes, and battles for every single position. From qualifying, to the start, to the finish, this race was insane.

                Let's just get qualifying out of the way. McLaren came in without even a tiny bit of a game plan. Something to do with Papaya Rules and making things fair... This lack of a plan lead to them starting in 13th and 14th, with Aston Martin's Del showing up hella late and starting in 15th.

                The Mercedes wunderkinds showed out. Jairo took his second pole position of the season and is starting to show up as a mainline contender, and the dude is just a rookie. Jayden was cooking during Q1 and Q2 but slowed up a bit in Q3, landing 5th on the gird for the race start.

                A shock performance from VCARB's Josh put him way the heck up the grid into 3rd and the Red Bull rookie Matthew also out performed his teammate to start in 4th.

                But, that's enough of all that reading, please enjoy the two major highlights of qualifying in meme form.
                ''')
    st.image(qualifying)
    st.markdown('''
                Now, once qualifying was settled Del decided he would grace the league with his presence and joined the race. And boy did he have a race! Something about some super powers from something he ate or something. It wasn't clear what he ate in Patrick's notes, but whatever it was, he should do that again. From 15th to 8th in a normal race format is in--wait for it--sane.

                But that was not the only insanity that the race brought ot us. Oh no, we had much, much more. I'm bringing back a classic format here for this recap. If you're a fan of my origin story, you'll recognize this as an homage to the first ever article that the league let me write. Enjoy.
                ''')
    st.image(race)
    st.markdown('''
                1) Sabotage - Matthew did his best to crash out Patrick
                2) The power of friendship - Josh and Patrick unite as a team
                3) Top tier tango - Jairo and Joshua go all out
                4) A new career approaches, bus driver - Erick reveals a hidden talent
                5) Eddie "No Balls" Tavera Jr. - Eddie's failed overtake on Erick
                6) Mystery VSC - Who knows why this even happened
                7) Eddie "Delta Denier" Tavera Jr. - Eddie ignores his delta
                8) Del sees red - Something about whatever he ate
                9) Blue flag of death - Boz's race ending moment
                10) Josh "Delta Denier" Anderson - Josh ignores his delta
                11) Wide boi Josh - The SoCal Minister of Defense
                12) Jairo the hero - A first win!

                For those who came to watch some racing, there were some epic moments. For those who came for the soap opera, don't worry there was DRAMA after the race in the cooldown room.

                Pink and orange clashed just like they do in color theory. The McLaren duo argued that Eddie drove erratically while the boys in pink defended that it was just a racing incident.

                The verdict is still out on this one, but one thing is clear, the McLaren and Alpine rivalry is alive and well.

                Enough with that nonsense though, how does this change the standings? VCARB jumps up back into the lead of the Constructor's fight and Nick slips behind Joshua and Patrick in the Driver's Championship.

                Jairo and Matthew both made up 4 places in the field, while also skyrocketing their team's standings. Most importantly, this is Jairo's first win in the league.

                The season is still young, but it is turning out to be a banger thus far. I can't lie, I live for this drama. Until next time nerds.
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