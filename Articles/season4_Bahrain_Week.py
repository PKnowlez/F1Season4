import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

raweceek = Image.open("./Images/RaweCeek1.png")
bahrain = Image.open("./Images/Bahrain_Circuit.png")

def article():
    date = "Thursday 09/25/2025"
    author = "Patrick"

    st.subheader('''Race Week: Bahrain''')
    st.image(raweceek)
    st.markdown('''
                It is finally a true race week. Points are on the line. Tensions will be high. Nerves will be frayed. So drivers and teams must come prepared for battle. With a long front and back straight and twisting corners in between, Bahrain has the makes of an excellent season opener.

                Sector 1 contains two DRS zones that will allow drivers to overtake and battle back immediately each lap. The heavy braking into Turn 1 will certainly lead to carnage at some point throughout the race. The smartest drivers will realize that Turn 1 is a great place to overtake mid-stint but a terrible one during the first lap. Predominantly this is because the first turn of the race will have drivers two to three wide going into Turn 2 and 3 which will leave no room for a strong exit. However, later on in the race, when there are one-on-one battles to fight, this will be a perfect place to get a little aggressive up the inside.

                As the drivers continue the first lap, they will sweep into Sector 2. Those with properly heated tires may be able to go full tilt through the first few corners of Sector 2, but those without the grip may find themselves in the run off quickly.

                The second sector also includes a strong DRS zone where drivers may find opportunities to overtake if they time their entry corners just right. Once the pack reaches Sector 3, they may find themselves simply sticking to the status quo as Sector 3 has an incredibly long straight with no DRS zone. Due to the engineering complexity of each vehicle, the slipstream has been significantly reduced this season, so the straight that wraps up the lap is likely to be useless for overtaking.
                ''')
    st.image(bahrain)
    st.markdown('''
                The circuit may certainly provide an avenue for good racing, but it's up to our drivers to truly let it rip and create this week's light show.

                However, there is very little league data on how the race will play out, as the league hasn't held an event here since the inaugural race of the first season. That season the league qualified well but carnage ensued that helped hand McLaren's Nick the first ever win in league history. Nick, Zane, Erick, Josh L., and David qualified 1-5 respectively with Boz in 10th, Marcus in 18th, and Travis and Gary missing qualifying and the start.

                From there, the race was anything but predictable. Marcus battled up to 14th, Boz fell to 13th, David and Josh L. took tumbles all the way to 10th and 11th, and Erick fell down to 7th. As noted before, Nick won and Zane barely missed the podium in 4th.

                If this week's race is anything like what we saw in preseason or what was demonstrated last time out in Bahrain, we are sure to see some fireworks and not just at the finish line.
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