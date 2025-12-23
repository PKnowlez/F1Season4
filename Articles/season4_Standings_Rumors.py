import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image
import pandas as pd

standings_summary = {
    "Team": ['Mercedes',
'VCARB',
'Alpine',
'McLaren',
'Red Bull',
'Aston Martin',
'Ferrari',],
    "Current Points": ['294',
'256',
'219',
'161',
'103',
'80.5',
'77',],
    "Ferrari Maximum - Podium": ['-45',
'-7',
'30',
'88',
'146',
'168.5',
'249',],
    "Aston Martin Maximum - Podium": ['-41.5',
'-3.5',
'33.5',
'91.5',
'149.5',
'252.5',
'-',],
    "Red Bull Maximum - Podium": ['-19',
'19',
'56',
'114',
'275',
'-',
'-',],
    "McLaren Maximum - Win": ['39',
'77',
'114',
'333',
'-',
'-',
'-',],
    "Alpine Maximum - Win": ['97',
'135',
'391',
'-',
'-',
'-',
'-',],
    "VCARB Maximum - Win": ['134',
'428',
'-',
'-',
'-',
'-',
'-',],
    "Mercedes Maximum - Win": ['466',
'-',
'-',
'-',
'-',
'-',
'-',]
}

standings_summary = pd.DataFrame(standings_summary)

intern2 = Image.open("./Images/Intern_2.png")
standings1 = Image.open("./Images/standings1.jpeg")
standings2 = Image.open("./Images/standings2.jpeg")
standings3 = Image.open("./Images/standings3.jpeg")
standings4 = Image.open("./Images/standings4.jpeg")
standings5 = Image.open("./Images/standings5.jpeg")
standings6 = Image.open("./Images/standings6.jpeg")
standings7 = Image.open("./Images/standings7.jpeg")

def article():
    date = "Monday 12/22/2025"
    author = "A Joint Patrick & The Intern Production"

    st.subheader('''Season 4 Standings and Rumor Mill Round-Up''')
    st.markdown('''
                In this article, The Intern and I will partner once again to deliver a season standings recap as well as some updates to recent rumors from around the paddock. Rumors, as per the usual, will close out the article, so if you are more interested in hot gossip scroll on down and skip the standings summary.

                However, skipping the standings recap would be a real shame, the league has never been more hotly contested with just four races to go. Four teams capable of taking home the Constructor's Championship with all seven still in the running for a podium finish. On the driver side of the championship, there are six drivers still in the hunt for the top crown and only four have been elminiated from contention for a podium finish.

                As this article progresses, please enjoy the memes and commentary from The Intern. As a pair, we will do our best to identify which of us is slandering you so you know who to come for later.

                **STANDINGS SUMMARY - CONSTRUCTOR'S CHAMPIONSHIP**
                ''')
    st.dataframe(standings_summary, hide_index=True)
    st.markdown('''
                So, what in the world does this table actually tell you, the reader? First, please read it one column at a time. Each column depicts a winning or best case scenario for each team.

                For instance, let us take a peak at the Red Bull column first. This column displays the highest amount of points that the Red Bull team could achieve in the Red Bull row (275). This means for the dynamic Red Bull duo, the best they can do is second place over all with 1-2 finishes for each of the final races. This can be assessed by comparing their maximum to the current points in the Current Points column. Where negative points are shown in the Red Bull column, those teams are unable to be beaten by Red Bull by that many points. The other point values in the Red Bull column are the points other teams must score less than for Red Bull to achieve their maximum final position.

                Now there is one caveat in all of this. The bonus points per race are not accounted for in these calculations. There are 4 bonus points per race, in other words 16 bonus points total, available over the remainder of the season. So, for instance, Brently and Newman could improve their odds down the stretch by bringing home a few fastest laps.

                Finally, 188 is the maximum number of points a team could secure (including all the bonus points) per race. With all this explained, below we will dive into each team and their feasible scenarios.
                ''')
    st.markdown('''**PODIUM HUNT TEAMS**''')
    with st.expander("Ferrari"):
        st.markdown('''
                    The prancing horses theoretically could make their way all the way up the ranks and into third without any bonus points, and even into second with a healthy handful of bonus points.

                    However, this requires them to run 1-2 in all four of the final races and for Mercedes, VCARB, and Alpine to have some generational failures filled with DNFs for all three teams.

                    It feels moderately unlikely that the scarlett duo will find themselves on the podium steps. But at this point, I cannot, in good conscious, count them out. Crazier things have certainly happened in the world of motorsports.

                    On their current trajectory, the betting odds are on the duo finishing in 6th this season with a strong battle against Aston Martin brewing.
                    ''')
    with st.expander("Aston Martin"):
        st.markdown('''
                    The racing green need to find some pace in the coming weeks and similar luck requirements as Ferrari to make the podium. They have marginally better odds though and with a few bonus points really could make their way up the standings.

                    With only a 3.5 point lead over Ferrari, there is more than a fair chance for either Aston Martin or Ferrari to finish in 6th. However, the Silverstone based duo has a greater chance of leaping up into 5th place by the time the season finale rolls around.

                    Betting against a perennial speedster like Del typically proves to be futile. This two team battle for 6th also highlights how powerful last year's mid-season swap that paired Del and Erick could have been had they not found their new teammates.
                    ''')
    with st.expander("Red Bull"):
        st.markdown('''
                    The energy drink duo of Newman and Brently have found themselves as the first team out of contention. With 103 points to date, the team is the highest scoring of our three teams that are officially unable to win the championship.

                    However, the effort they have put in so far has given them a straighter fight for 2nd place. They do not need to rely on bonus points to make it to the the second highest step on the podium.

                    Instead, they need a whole lot of luck and for VCARB to finish with less than 19 points over the next four races. This is obvioulsy unlikely, so what is the betting man's choice for Red Bull?

                    With the papaya team lacking the umph they had last year, it is favorable for Red Bull to make up some ground in these final few races and find themselves in 4th over all. To make this bold prediction stick, the Red Bull squad will need season best performances from both drivers to close the gap and overtake McLaren. Otherwise, they are simply in a great position to defend against late Ferrari and Aston Martin charges.
                    ''')
    st.markdown('''**CHAMPIONSHIP HUNT TEAMS**''')
    with st.expander("McLaren"):
        st.markdown('''
                    McLaren is a storied team with the most consistent presence at the top. It might all finally come to an end this season. Sitting securely in 4th place in the standings, a minor miracle would be needed to make it all the way to the top.

                    However, there is a strong chance that McLaren could bolt all their wheels on and come out a place or two higher in the standings. Alpine does truly need to perform well if McLaren begins to light it up. VCARB cannot rest on their laurels either.

                    But it will take an enormous amount of luck and plenty of skill to avoid mishap and make the comeback a reality. The betters out there might, for the first time in this article, consider McLaren's current position as their most likely position. 
                    ''')
    with st.expander("Alpine"):
        st.markdown('''
                    Last year's controversial champions have found themselves in a tough situation. They have been shocked like the rest of the league by the raw speed the Mercedes duo possess. But that does not mean they are out for the count.

                    With a 1-2 finish in every race and a 4-5 finish in each race from the Mercedes duo, the French squad could bring home the championship. This all works out even if their nearest rival, VCARB, finishes 3-6 in each of the final races.

                    So it is truly not over yet for the reigning champions. However, with all bets on the table, not too many are favoring the hot pink racers. In fact, in their recent polling in the power rankings, they are squarely settled into 3rd place. Only time will tell if some luck rolls their way.
                    ''')
    with st.expander("VCARB"):
        st.markdown('''
                    The clearest contender for the crown, outside of the current leader, is VCARB. In fact, they are the only team in the chase with their destiny in their own hands. With a 1-2 finish in each of the final races, no matter how well Mercedes performs, VCARB will take home the shiniest of trophies.

                    But that might be a tall order for the team. With a rookie and a three time race winner, pulling in four wins and four second place finishes in sequence might be out of the cards.

                    However, this avenue is simply the one they have total control over. With a few DNFs or low point outings from the Mercedes duo and some strong performances from the VCARB brothers, the championship is certainly still on the table.

                    Betting odds are mixed here, with the team still polling well in power rankings, but still the chasers. Regardless, it is a promising season for the new pair with second year driver and rookie finding their groove throughout the season.
                    ''')
    with st.expander("Mercedes"):
        st.markdown('''
                    Truly, there is not much to write here. If this duo performs the way they have throughout the season, they will be the champions at the end of it all. As the only team with a 1-2 finish this season, it is very likely they can repeat that magic.

                    Now, of course, a few bad performances in qualifying, or even a DNF or two would shake this rock solid foundation. 

                    The odds are truly in Mercedes' favor this late in the season. Again, only time will tell if consistency for the Mercedes team will prevail or will a few untimely errors erode the lead they currently have.
                    ''')
    st.markdown('''
                **STANDINGS SUMMARY - CONSTRUCTOR'S CHAMPIONSHIP**
                
                Sheesh, I thought that guy would never shut up.
                ''')
    st.image(intern2)
    st.markdown('''
                So some of you have been, what we like to call, eliminated. Which, is certainly a tough pill to swallow. So, let me shove it down your throat with a meme or two. Those who have been completely eliminated from a podium finish in the Driver's Championship, enjoy.
                ''')
    st.image(standings1)
    st.markdown('''Now, there are also a few of you who need to be added to that list because everyone here is unable to win the championship, though a few of you could land on the podium still.''')
    st.image(standings2)
    st.markdown('''
                Now the good news for the rest of you is that you could still win it all this season. At least mathematically... A few of you are truly delusional to think you've actually got a shot at this one. But alas, I hate typing, so I will drag you over coals the old fashioned way, with viscious dank memes.
                ''')
    st.image(standings3)
    st.image(standings4)
    st.image(standings5)
    st.markdown('''
                Now, it isn't all rainbows and dolphins for the top three either. Joshua has somehow created a commanding lead going into the final few races. However, as we have seen time and time again, Joshua does have a magic of his own. This magic is also known as choking. Homie smashes into pit walls, spins just for fun I guess, and sometimes even just loses a wing during an overtake for the love of the game.
                ''')
    st.image(standings6)
    st.image(standings7)
    st.markdown('''And that is pretty much it. The ship is Joshua's to lose, but Patrick and Jairo theoretically have the best chances to make the comeback. Everyone else mathematically still in it would need a true Lazarus moment to bring their hopes back from the dead.''')
    st.markdown('''
                **RUMOR MILL ROUND-UP**
                
                For anyone that has been offended throughout the season by The Intern, or even in this article, they have provided a formal apology, as stated below.

                > I would like to apologize...to ABSOLUTELY NO ONE.
                >
                > If you can't handle the heat then get out of the frying pan.
                > 
                > Y'all are soft, Charmin Ultra-Soft, that bear would love wiping with some of y'all.

                Ok...so that did not go as expected. Rumor has it The Intern is truly remorseless and merciless. But that's just a rumor right?

                Now, as the season has gone on, with new regulations looming, we have noticed a flurry of drivers and teams looking for new opportunities. One of note is that the duo from Aston Martin was seen entering the Williams paddock offices together followed closely by team principal James Vowels. Now, word on the street is, the duo is simply exploring options, but many are concluding this means an end to the long standing run Del has had with Aston Martin.

                Del is not the center of these talks though, as Bos' private jet was seen landing at a small airfield just outside of the new Audi Revolut F1 Team's headquarters. Could this signal a different move for the driver? Could this mean Del and Bos are splitting up? Or was Del on that flight with Bos doing initial negotiations with one of the newest outfits on the grid?

                McLaren has begun spreading some hype for their driver lineup announcement with an official announcement expected by the end of the season. The betting favorite is still Erick, however, new names have begun surfacing. Some are speculating that the rumors were about a different Tavera. However, that feels unlikely with the history that Eddie and Nick have.

                Speaking of history, a brotherly duo has been identified as the favorites for the Cadillac seats. As mentioned previously, it was known that the Cadillac and Haas drivers would be forming what they call an "All American Alliance." Which, as we began to uncover, might already exist in today's teams. After the race in Zandvoort it is pretty clear that the Red Bull sister teams are operating under some form of teamming rules. All of this has the odds spiking around Josh and Patrick taking the driver at Cadillac for their maiden season.

                This also means that if those suspicions are correct, Brently and Matthew will be driving for Haas next season. All of this means Red Bull and VCARB will be freed up from their current driver commitments.

                Which leads us to our final rumor of the break, Joshua to Red Bull? With Eddie? Yes, you heard it here first folks. Joshua, while searching for a new teammate, might remain paired with his current teammate, and they both might make the move to Red Bull to try and bring the Austrian squad a championship.
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