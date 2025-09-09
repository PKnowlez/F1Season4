import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

image = Image.open("./Images/Track_Tier_List.png")
gif = open('./Images/deal_with_it.gif','rb')
contents = gif.read()
data_url = base64.b64encode(contents).decode('utf-8')

def article():
    date = "Monday 08/25/2025"
    author = "The Intern"

    st.subheader('''The Definitive Ranking of Season 4 Tracks''')
    st.markdown('''
                While onboarding for this season, the editors told me that as the intern, I needed to create things that had not been done before. So, let's start that off with the league's first tier list.
                
                Let's just get one thing straight before we get into this. Don't @ me. This list is definitive. I am correct. Your oppinion is invalid and that is simply facts. #DealWithIt
                ''')
    st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Your GIF">', unsafe_allow_html=True)
    st.markdown('''
                With that out of the way, enjoy the list. If you disagree, bummer, this is objectively correct. There is nothing that can make me move any of these tracks (well except maybe money), especially the first place and last place picks.

                More importantly, if you disagree you're free to make your own trash version of the list. But just know it will be wrong. Actually, on second thought, go vote here and let's see how wrong you all are on average: https://live.tiermaker.com/84368036
                ''')
    st.image(image)
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()