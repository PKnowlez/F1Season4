import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

image = Image.open("./Images/1000 Points Nick.png")
image2 = Image.open("./Images/Travis 1000 Points.jpg")

def article():
    date = "Thursday 10/30/2025"
    author = "Patrick"

    st.subheader('''A Monumental Milestone''')
    st.image(image)
    st.markdown('''
                **McLAREN TEAM STATEMENT**
                
                > The team here at McLaren is so excited to congratulate Nick on achieving 1000 career points. Over the course of the last four seasons, Nick has battled to earn each of these points and his three Driver's Championships.
                > 
                > We know this feat is momentous regardless of circumstances, but to be the league's first 1000 point driver is an extraordinary accomplishment. As the season continues, we look forward to watching Nick smash more records and compete for a fourth Driver's Championship.

                Prior to hitting this mark in Mexico, Nick was interviewed and wanted to make sure he could express his gratitude for his teammate Travis and the man that pushed him to join the league Erick.

                > Without both Travis and Erick this would never have been possible.

                Our reporters also caught up with his teammate Travis who shared this sentimental image and had this to say:

                > Nick, thanks for carrying me since 2023. Congratulations on this huge win.
                ''')
    st.image(image2)
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