import streamlit as st
from streamlit_carousel import carousel
from Articles import season4_track_overview, season4_schedule_reveal, season4_trophy_reveal, season4_track_tier_list, \
                season4_track_rankings, season4_ROTY_award, season4_Preseason, season4_Bahrain_Week, \
                season4_Bahrain_Recap, season4_Miami_Week, season4_Miami_FIA, season4_Miami_Recap, \
                season4_Spain_Week

def Tab0():
    if 'show_all_content' not in st.session_state:
        st.session_state.show_all_content = False

    #region --

    season4_Spain_Week.article()

    #endregion
    
    # ----------------------------------------------------------------------------------------------------------
    # "Show More/Less" button 
    if not st.session_state.show_all_content:
        if st.button('Show More'):
            st.session_state.show_all_content = True
            st.rerun()  # Rerun the app to show everything
    else: 
        if st.button('Show Less'):
            st.session_state.show_all_content = False
            st.rerun()

    if st.session_state.show_all_content:

        season4_Miami_Recap.article()
    
        season4_Miami_FIA.article()

        season4_Miami_Week.article()

        season4_Bahrain_Recap.article()

        season4_Bahrain_Week.article()

        season4_Preseason.article()

        season4_ROTY_award.article()
        
        season4_track_rankings.article()
        
        season4_track_tier_list.article()

        season4_trophy_reveal.article()

        season4_schedule_reveal.article()

        season4_track_overview.article()
       
        #region Driver Announcements
        st.subheader("Season 4 Driver Lineup")
        driver_announcements = [
            {
                "title": "",
                "text": "",
                "img": "./Images/Driver_Lineup.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Alpine_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/McLaren_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Red_Bull_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/VCARB_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Intern_1.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Intern_2.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Aston_Martin_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Ferrari_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Mercedes_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Tracks_1.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Tracks_2.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Tracks_3.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Tracks_4.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Tracks_5.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Tracks_6.png"
        },
        ]

        carousel(items=driver_announcements, interval=20000)
        st.divider()
        #endregion