import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

image = Image.open("./Images/Mexico Missing.png")

def article():
    date = "Thursday 10/30/2025"
    author = "Patrick"

    st.subheader('''Race Recap: Mexico - Mundane Moist Madness''')
    st.markdown('''
                Howdy folks, Patrick here. The Intern read my notes and literally threw them back at me saying this was so incredibly boring that even they, in all their incredible content skills, could not create a reasonable recap.

                So, you've got me. This'll be a bit of a throwback, much more analytical, and hopefully a nice break from the insanity that is The Intern. So without further ado, please enjoy this formal race recap of this week's throwdown in Mexico.

                **PRE-RACE SHENANIGANS**

                At the end of last week's race in Spain, Eddie announced he would not be in attendance for Mexico's festivities. His teammate, Joshua, expressed his distain during the conversation and throughout the lead up to the race in both private messages and group threads.

                Eddie was not the only driver to bail on the race this week though. His brother, and archrival, Erick also announced his inability to make the race. Ferrari rookie Leo did not make any public comments on this, but it is safe to assume this was not Plan A for the team.
                
                **QUALIFYING**
                
                As qualifying got underway, a few drivers struggled with their cars and had technical challenges during their outlaps. Both McLaren's Travis and Aston Martin's Boz struggled with their power units and steering wheels respectively.

                However, after those incidents, the drivers made their way rather uneventfully through Q1.

                With Q2 underway, the Mercedes duo began to show their prowess over one lap again, with Alpine's Joshua hot on their heels. Others found themselves in the midst of the top 10, but both Travis and Boz were unable to fully regain their rhythm after their mishaps during Q1 and missed the cut.

                Jairo proceeded to take home yet another Pole Position during Q3 with Joshua right behind. Most surprising though was the speed that VCARB's Josh was able to demonstrate during the third qualifying session, finding himself in third right next to reigning champion Nick in fourth.

                **THE RACE**

                During qualifying the drivers had noticed a chance for rain during the race. Most analysts, however, expected it to be a dry race. But as the cars rolled up to their starting blocks, the heavens opened and it began to steadily rain for the first 10 or so laps.

                Surprisingly the start went off without a hitch. No major incidents, only little bumps and shoves during some of the light braking zones like Turn 2. Pole sitter Jairo got off to an incredibly strong start in the wet, while Joshua and Josh battled side-by-side all the way up and into the esses of the second half of the lap.

                Inevitably, this lead to Jario being able to pull away and create a strong gap that likely helped him throughout the remainder of the race. Further back, Jayden had an equally strong start and made up a few places.

                As the rain continued Nick and VCARB's Patrick had a small skirmish on the main straight as Nick's setup was evidently much higher in downforce than Patrick's.

                In the mid and back field, there were a few different results for drivers. Leo had a smooth and steady approach to his race, finishing just shy of a two point finish in 10th. While, the Red Bull drivers both had different strategies on how to handle the start and rain. Brently took a cautious but still with good pace approach, while Matthew determined falling back early would prevent damage and allow him to pit more effectively when the rain did fade.

                His suspicion was almost true. When the dry weather rolled in and the rain rolled away, everyone was able to pit and those who were there at just the right time took a minor advantage over their competitors. Aston Martin's Del was one who, unfortunately, was unlucky in this moment fitting the wrong tires during his first stop and falling off as the soft tires wore in quickly.

                Both McLaren's Nick and Aston Martin's Boz also had disappointing pit stops as the weather shifted. Both drivers ended up with a second set of intermediate weather tires instead of slicks.

                The race continued rather smoothly without a single VSC or SC. Again, only a few bumps and shoves occurred throughout the race. But as time wound down, penalties started to stack up. Joshua, on nearly completely worn tires, ended up spinning and gaining nine seconds worth of penalties that helped Patrick leap frog him.

                Nick, desparate to make some standings shaking moves, fitted the soft tires and attempted to streak up the results, but was unable to do so and ended up losing two places in the end from when he put on the soft tires. Even with all these mishaps, the league accomplished a race with zero DNFs.

                All in all, this was a strong showing from Mercedes with the first 1-2 finish for a team since the Brackley outfit managed it at Monza during Season 1 with Marcus and Erick at the wheel.

                **STANDINGS**

                This incredible finish by Mercedes has them leaping from dead last two races back to first place in the Constructor's Championship. It also pushes Jairo into 4th overall in the Driver's Championship.

                Last year's runner up, Joshua, still leads the Driver's while VCARB is just two points behind Mercedes in the Constructor's.

                The season is finally starting to heat up with major swaps possible at each race due to how tight the overall standings are.

                As a gift for everyone who made it this far, I asked the intern to create one single meme for us. Enjoy.
                ''')
    st.image(image)
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