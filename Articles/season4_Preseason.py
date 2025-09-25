import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

mumscar = Image.open("./Images/MumsCar.jpg")
preseason_memes = Image.open("./Images/PreseasonMemes.png")

def article():
    date = "Wednesday 09/24/2025"
    author = "The Intern"

    st.subheader('''Preseason Race Recap: We Are So Back''')
    st.image(mumscar)
    st.markdown('''
                What a flipping mess. Terrible settings (thanks Patrick), VSC and SC, carbon fiber everywhere, and some drivers failed to even start their cars...

                Everyone was a rookie during this one. Surprisingly two of the rookies were the only ones who drove like veterans, with Jairo and Jayden putting Mercedes on the podium and well up the midfield respectively. The same cannot be said for some of our returning drivers.

                Some of the driving seen today was disgraceful, no cap. So what if it was raining, these guys shouldn't be that bad. Some of them even forgot where their clutches were in the pits, sheesh.

                Beyond all the rust being dusted off, there were some bright moments. Rookie Matthew crashed out during Q1 and his mechanic team miraculously had him up and running for Q2. Others, like Nick battled back from setbacks and completed plenty of overtakes. Joshua qualified well and kept his ish together to remain on the podium, honestly a shocker he even finsied Q1 the way he ended last season.

                But let's talk about the stupidity that ran through everyone's veins, and as I always say, memes are worth 1,000,000 words.
                ''')
    st.image(preseason_memes)
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