import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

screenshot = Image.open("./Images/bahrain_start.png")
intern_smashing = Image.open("./Images/intern_smashing.png")
mclaren_livery = Image.open("./Images/bahrain_mclaren_livery.png")
bahrain_qualifying = Image.open("./Images/bahrain_qualifying.png")
bahrain_race = Image.open("./Images/bahrain_race.png")
gif = open('./Images/bahrain-newman.gif','rb')
contents = gif.read()
data_url = base64.b64encode(contents).decode('utf-8')

def article():
    date = "Thursday 10/02/2025"
    author = "A Joint Patrick & The Intern Production"

    st.subheader('''Race Recap: Bahrain - Carnage from Cover to Cover ''')
    st.image(screenshot)
    st.markdown('''             
                Nothing could have prepared the drivers for the events of last night. From Safety Cars to glitches galore, the drivers were faced with perils from before they even got to the paddock all the way through the fireworks.
                
                Interestingly enough, the stewards were a bit unenthused throughout the chaos. But before we get into that and let our illustrious intern unravel the ongoings of last night, there is a bit of late breaking news from the FIA about the race results.
                ''')
    st.markdown('''
                <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div>
                ''', unsafe_allow_html=True)
    st.markdown('''
                **Press Release** \n
                **For Immediate Release**  
                _Date: October 2 2025_

                **Race Results Update:***

                After reviewing new evidence, the FIA has determined that Red Bull's Brently was wrongly given a 10 second penalty during the second safety car. This penalty led to him finishing in 8th place which has now been corrected to be 4th place with the reduction in finishing time.
                
                There will be no further room for appeals, but the FIA directors are still open to inquiries or clarifications. For further inquiries or clarification, please contact Erick Tavera or Nick Beglin.
                    
                To all our drivers, it is our responsiblity to ensure a fair and balanced racing environment for all competitors. If there is ever an unprecedented issue within a race, please provide video evidence to the FIA as soon as possible to allow for review of any issues.
                ''')
    st.markdown('''
                <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div>
                ''', unsafe_allow_html=True)
    st.markdown('''
                _The Alternative F1 League_
                <p style="color:lightgray;">Where racing meets integrity and fair competition.</p>
                ''',
                unsafe_allow_html=True,)
    st.markdown('''
                <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div>
                ''', unsafe_allow_html=True)
    st.image(intern_smashing)
    st.markdown('''
                Aaaaaaaaaand with the boring stuff out of the way, let's get into the juicy details of the race and all the gossip around the paddock before hand.
                
                Let's just recap some of the pre-race drama first. The power rankings had Red Bull complaining like they had lost the right to breathe. Maybe don't crash out in Q1 of the first event of the season.

                Allegations flew about the Season 3 controversial finale. Teams were yapping about Alpine using controllers to secure their championship or some other kind of fraud.

                But the juicest pre-race gossip is that McLaren's Travis was caught running a livery that did not live up to the FIA's pretentious standards. He ended up serving a race ban instead of serving looks in this throwback livery.
                ''')
    st.image(mclaren_livery)
    st.markdown('''
                But it wasn't just the race ban that was juicy, it's the rumors that Papaya Rules may be in play and that Nick may need to sit out all of Miami to ensure a fair battle between the two drivers.
                
                Our paparazzi cornered Nick pre-race and this is what he had to say:

                > *The situation is a frustrating way to start the championship but I stand with my teammate [and with daddy Zak's Papaya Rules] against the powers that be and hope a resolution can be found quickly.*

                With Travis in the timeout corner, drivers started qualifying. Well, most of them did... To recap qualifying, please enjoy this amuse-bouche of memes (wait when did I learn French...)
                ''')
    st.image(bahrain_qualifying)
    st.markdown('''
                To those who love memes, don't worry there will be more, but my management has asked that I also add "a bit of race recap that has some journalistic integrity," or whatever that means. So read through the next bit or skip to the memes at the bottom if you're more of a picture book kind of adult.
                
                The teammate-less showed out big time in qualifying with Mercedes driver Jayden clutching his first pole of the season and McLaren's Nick completing the front row.

                The race got off to a predictably terrible start with Alpine's Eddie absolutely flooring it through Turn 1 forgetting entirely that braking is part of racing. Damage, more damage, and then a tiny bit more damage, occurred in a matter of seconds leading to a Virtual Safety Car right out of the gate.

                Once the FIA stopped being the no fun police and let the drivers race again, Nick and Alpine's Joshua got into a side-by-side battle for a lap. The way those two shut up the second they started racing each other was music to the rest of the grid's ears. With them up at the front, the two VCARBs were surprisingly in 3rd and 4th. Rookie Josh helped his teammate create a reasonable gap to the likes of Aston Martin's Del and Ferrari's Erick.

                The race continued from there and Patrick has some kind of note about strategies or something stupid like that. I ain't here to write about one-stops vs. two stops vs. whatever the heck some of you did. So let's fast forward a bit. After drivers like Eddie, Aston Martin's Boz, and Mercedes' Jayden and Jairo spent all their time battling back up the ranks, a plague of Safety Cars erupted. I'll let the memes do the rest of the talking though.
                ''')
    st.image(bahrain_race)
    st.markdown('''
                With all the racing said and done, VCARB's Patrick took home the team's first win of the season with a ballsy one-stop strategy and a penalty-less drive. The usual suspects rounded out the podium with Alpine's Joshua and McLaren's Nick standing on the next two steps respectively.

                Noteworthy drives came from the two Aston Martins who both battled the mid-field admirably and brought home a strong points haul for their team.

                Alpine's Eddie and the Mercedes duo also artificially created noteworthy drives due to their errors, spectacular qualifying, and somehow also lack of qualifying.

                The Red Bull team couldn't figure out how to stay out of the limelight either with Matthew finding a sick ramp to do a little trick on mid-race (see below) and Brently practicing his banishing spells on Eddie creating a whole slew of FIA reviews. Both drivers had their positions reinstated, because the FIA is Charmin Ultra Soft when it comes to glitches.

                Finally, our Ferrari friends had a bit of a howler with a DNF from Leo and a surprisingly mediocre drive from Erick. I guess there's always next year or whatever the Tifosi say. 
                ''')
    st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Your GIF">', unsafe_allow_html=True)
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