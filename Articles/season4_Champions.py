import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

def article():
    carousel_images = [
                {
                    "title": "",
                    "text": "",
                    "img": "./Images/Championship/JoshuaChampionship.png"
                },
                {
                    "title": "",
                    "text": "",
                    "img": "./Images/Championship/MercedesChampionship.png"
                },
            ]

    carousel(items=carousel_images, interval=20000)

    date = "Thursday 01/22/2026"

    st.markdown(
        f'''
        <p style="color:lightgray;"> {date}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()

# ----- How to add a GIF: ----- #
# gif = open('./Images/surfer.gif','rb')
# contents = gif.read()
# data_url = base64.b64encode(contents).decode('utf-8')
# st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Your GIF">', unsafe_allow_html=True)

# ----- How to add a Video: ----- #
# video = "./Images/VideoFile.mp4"
# st.video(video, format="video/mp4", loop=False, autoplay=False, muted=False, width="stretch")

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