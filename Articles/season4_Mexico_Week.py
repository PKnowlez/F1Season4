import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

track = Image.open("./Images/Mexico_Circuit.png")
cover = Image.open("./Images/Mexico Cover.jpg")
sombrero = Image.open("./Images/Mexico Sombrero.jpg")

def article():
    date = "Friday 10/24/2025"
    author = "Patrick"

    st.subheader('''Race Week: Mexico''')
    st.image(cover)
    st.markdown('''
                <div style="background-color: #97978F; padding: 10px; border-radius: 5px;">
                But first, the league's first ever protest vote has concluded. Regulation 9 states that a driver can protest an official ruling within 24 hours of the ruling being released. To overturn the ruling, the league needs a super majority, or in other words 2/3rds of the vote. This amounts to 10 votes with the current league size of 14 drivers. <br>

                McLaren's Nick submitted a protest to reverse his penalty point earned in Spain. All drivers have now voted, with 9 voting to remove the point and 5 voting to keep the point. This result means Nick will retain the penalty point on his Super License for the remainder of the season.
                ''', unsafe_allow_html=True)
    st.markdown('''
                With that breaking news settled, Viva la México, because it is race week down in Mexico City. The converted stadium and street circuit rests at the highest altitude of any track the league will face all season. At 7,350 feet, even our drivers from Colorado will be feeling the thin air.
                
                That means drivers will need to be prepared with effective setups for the high-speed corners of the track's back section, while remaining as trimmed out as possible for the front straight and three DRS zones.

                After the battles of Spain, the standings are closer than ever entering this fourth event of the season. The top five teams are separated by just 16 points, with first to last only separated by 36 points. In other words, a double podium from Ferrari could send them all the way into first place overall.

                On the driver side of the championship, the top three are separated by 5 points with the majority of the field nicely bunched up within a win from the top as well. With the wide variety of winners thus far in the season, there have been no clear trends as to who might come out on top before the Thanksgiving break in just four races.
                ''')
    st.image(track)
    st.markdown('''
                But what can we expect from the circuit this week? First and foremost, this is a fast lap that includes some heavy braking zones. Definitively different than Spain, the street circuit relies on drivers being ready to lick it and send it.

                Turn 1 will be the first test of this as the drivers will have a long run from the start line to the first braking zone. This long run means that starting on time is more critical than ever for our drivers. Being behind on the start will certainly lead to losing places on the run down to Turn 1.

                From there the drivers will likely be fighting for the inside of the following two corners into what will become the first DRS straight after the first lap. This should string the drivers out and allow for an overtake attempt or two into Turn 4.

                Turn 4 also signals the beginning of Sector 2, which is the most technical part of the lap. Winding esses that require finese and are not simply flat out like in Silverstone or COTA will require every ounce of focus the drivers can muster.

                The sector ends with a short DRS straight meant to bunch up drivers in hot pursuit with their prey when entering the stadium section. While the end of the straight is a heavy braking zone, it is not the most strategic place for an overtake. In fact, most drivers will likely opt to simply keep it close through the chicane and attempt to battle the dirty air into the front straight.

                Once back on the front straight, drivers will be met with an incredibly long DRS zone that butts right up into Turn 1. This is likely to be one of the main opportunities for drivers to make up places throughout the race.
                ''')
    st.image(sombrero)
    st.markdown('''
                The real question is, who will wear the crown...er...sombrero at the end of the race? The last time the league visited the iconic street circuit was during the inagural season where retired Ferrari driver Zane took pole and the win. He was followed up by Boz who was still in his Red Bull seat and all time McLaren driver Nick in third.

                At that point in the season, Nick had scored 353 points and was neck and neck with Erick for the title. Fast forward to today, and Nick is nearly at 1000 points. With a total of 994 points, Mexico could be the first time the league sees a driver make it into the 1000 point club.

                After Spain, many question still remain. Will Nick and Eddie clash again? Will the Mercedes duo continue to impress? Will last year's runner up, Joshua, finally hit his stride and stand on the top step? Or will something unpredictable occur early on in the race leading to new winners and another standings shakeup?

                Finally, the FIA has updated one of its regulations, as new evidence surfaced exposing a flaw in the rule. Regulation 7 has been updated to remove the subsequent VSC criteria and now only a full Safety Car or Red Flag will negate the opportunity for a driver to appeal their Delta Glitch.
                ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()