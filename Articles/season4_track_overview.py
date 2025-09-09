import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

tracks_1 = Image.open('./Images/Tracks_1.png')
tracks_2 = Image.open('./Images/Tracks_2.png')
tracks_3 = Image.open('./Images/Tracks_3.png')
tracks_4 = Image.open('./Images/Tracks_4.png')
tracks_5 = Image.open('./Images/Tracks_5.png')
tracks_6 = Image.open('./Images/Tracks_6.png')
miami = Image.open('./Images/track_reveal_miami.png')
surfer_gif = open('./Images/surfer.gif','rb')
contents = surfer_gif.read()
data_url_surfer = base64.b64encode(contents).decode('utf-8')
no_mikey = Image.open('./Images/no_mikey.png')

def article():
    date = "Friday 8/15/2025"
    author = "A Joint Patrick & The Intern Production"

    st.subheader('''Season 4 Track Overview''')
    st.markdown('''
                Welcome one and all to the first official article of The Alternative F1 - Season 4. Below, we will cover the tracks that have been selected for this season and how the league has faired at them previously.

                The following will overview the expected perils and dangers of each track. Additionally, we will review driver reactions and what we are hearing from around the league from teams with respect to the selections that were made. To kickoff this article, we will cover the first three tracks of the season.
                ''')
    st.image(tracks_1)
    st.markdown('''
                **Pre-Season: Silverstone** Hallowed ground and home to the first ever Formula 1 race. A fitting start to the season. However, the racing that occurs here will not help drivers or constructors climb the ladder to the championship.

                Surprisingly, the sacred tarmack at the old airfield has been selected only for pre-season testing. Drivers will take to the track and rush through the high speed turns purely to test, acclimate, and prepare to do battle with each other during Week 1 of the season.

                The reigning back-to-back-to-back Driver's Champion, Nick, had this to say:

                > "I'm bummed we dont have COTA or Silverstone [this season] but we have a good line up of tracks. Minus Miami. Someone is taking the piss with that."

                It was all smiles though, as he chuckled about the dig at the Miami International Autodrome and the driver who selected the track. Even after the turmoil in the last few laps of last year's Silverstone race, Nick seemed content to let bygones be bygones with this circuit.

                **Week 1: Bahrain** The meaningful racing will begin in the Middle East. Drivers will take to the tight turns and long straights of Bahrain International Circuit. The track is known for being friendly to rookies, and should allow for some strong early season wheel to wheel action.

                The hard braking point into Turn 1 will be the first real test for the league. Each driver will need to be prepared for the concertina effect as the group bunches up into the narrow twisting turns at the beginning of the lap. 

                All eyes will be on the rookies, but the pressure will be on Nick who is the only driver in league history to win, let alone stand on this circuit's podium. In fact, the track hasn't even been selected to race on since the league's inagural season.

                **Week 2: Miami** The second week of league action takes us to the sunny Florida coast for our first Sprint of the season. However, things aren't all rainbows and butterflies with respect to this track selection. To help illustrate the turmoil, I have asked our illustrious intern to take the reigns for a moment.

                As an intern, me think, why waste time say lot word, when few word (or image) do trick.
                ''')
    st.image(miami)
    st.markdown('''
                Now back to the guy who is still refusing to pay me...smdh.

                Right...so, the league will be taking to Miami for not just one race, but also a Sprint. Now the last time the league took to the converted parking lot of the Hard Rock Stadium was for last season's pre-season testing which saw Joshua, Nick, and Patrick stand on the podium.

                However, similar to Bahrain, Miami has been off the official league calendar since the first season. That race saw the man who has whined the most about the track take home the win, with Erick and Marcus stepping up onto the podium just short of Nick.
                ''')
    st.image(tracks_2)
    st.markdown('''
                **Week 3: Spain** With Miami in the rearview mirror, the drivers will take to the incredibly high speed turns of the Circuit de Barcelona-Catalunya. With the technical driving found on this circuit, it comes as no surprise that two of the league's finest have always finished on the podium here.

                Both Nick and Erick have found their way onto the top three steps on both occasions that the league has raced here. Questions about this track in particular circulated around the league. Can Erick keep the focus to maintain his streak? Can Nick keep up with the demanding physicallity of this track at his veteran status?

                Regardless of the answer to those questions, it will be an excellent reprieve for the rookies from the narrow street circuits that are littered across this season. The sweeping turns should allow for epic wheel to wheel fights and plenty of drama.

                **Week 4: Mexico** However, the reprieve from the hyper technical tracks won't last long. As we trade *Viva Espana* for *Viva la Mexico.* Drivers will be treated to yet another throwback circuit that has not been on the calendar in the last two seasons.

                Ripping through the converted stadium, drivers and fans alike will be gifted with some spectacular views and high altitude racing. In the league's only outing here, retired driver Zane took home the win with Boz and Nick rounding out the podium.

                **Week 5: Baku** For our rookies, it only gets tougher. Here is to hoping we don't find out who is "stupid" here in the castle section. The tight, narrow, and altogether challenging streets of Baku beckon the drivers during our fifth race.

                Last year's race was the league's first ever trip to the Caspain Sea which saw nothing less than carnage in the final few laps. Nick and Patrick were the only two drivers to make it up onto the podium as we saw devastating strategies and crash outs in the closing moments of the race.

                When asked about the race last season, Eddie responded:

                > "No comment."

                However, the recently promoted Red Bull driver, Brently, who typically remains quiet and reserved, had this to say:

                > "I can't stand this track, but at least Checo won't be here to ruin my race."
                ''')
    st.image(tracks_3)
    st.markdown('''
                **Week 6: Austria (Reverse)** The league will continue its travels around the globe with its first of two stops in Austria for this season. This trip to the Red Bull Ring will have the drivers racing the circuit counter clockwise.

                We truly have no idea how this will turn out, but our intern does have some thoughts...
                ''')
    st.markdown(f'<img src="data:image/gif;base64,{data_url_surfer}" alt="Your GIF">', unsafe_allow_html=True)
    st.markdown('''
                I really hope that made sense to someone out there, our intern has returned with dyed hair and a lot more slang this year. Anyways, there really is no knowing how the race in Austria will go, but it will be exciting nonetheless.
                
                **Week 7: Spa** Will McLaren and Nick's win streak continue? Arguably one of the most famous circuits on the planet, Circuit de Spa-Francorchamps continues to remain a perennial favorite for the league's drivers.

                With plenty of room for wheel to wheel racing, along with a few spectacular opportunities to out brake your opponent, the circuit should provide some excellent racing. Even with Nick's incredible record here, drivers across the field are hopeful they can take home a win here.

                Much of that hope is spurred on by the track's Sprint race this season. With an opportunity to win twice and an opportunity to defend from the front with the reverse grid race rules in place.
                
                **Week 8: Brazil** Two Sprints back-to-back will certainly test the will power of our drivers. Particularly if the weather becomes a factor in Spa or Brazil. With what seems like a trend at this point, Brazil has not been on the calendar since Season 1.

                The last outing here saw Nick, Boz, and Erick take to the podium and bring home some hardware. Nick will likely look to reclaim the podium, but challengers like Joshua and Del seem poised and ready to pounce on any opportunity.
                ''')
    st.image(tracks_4)
    st.markdown('''
                **Week 9: Austria** Back to the future we go with the league returning to the Red Bull Ring, but this time in clockwise fashion. There has not been a season where the league has skipped a chance to rip around the Red Bull Ring.

                In the most recent two seasons, Joshua, Nick, and Del have flip flopped around on the podium with Nick playing the meat in the middle of the sandwich on both occassions. Before that, he had found himself as the winner of the race with Zane and Erick hot on his heels.

                Will we see Del return to the top step or will Joshua go back-to-back? Could this even be a rookie's first win of the season? The hills will certainly be alive with the sound of hybrid v6 engines.
                
                **Week 10: Zandvoort** With a one season hiatus, the beach front circuit returns to the calendar, and maybe for the last time. Drivers will look to claim the last winner at Zandvoort title in this all out banked corner brawl.

                In previous encounters with the sandy circuit, Erick and Nick have both taken home the largest piece of hardware at the end of the day. Will this year see the first repeat winner?

                Due to the nature of the banked turns and varying lines, I suspect this track could be where a surprise winner jumps onto the podium. Plenty of overtaking action as well as opportunities to simply surprise your opponent should allow our drivers to sneak their way through the ranks.
                
                **Week 11: Jeddah** With a long stint of permanent circuits done and dusted, the drivers will head right into one of the tightest and high speed street circuits around. There will be nearly no room for error as each driver battles those around them and themselves through the narrow corridors of Jeddah.

                Previously, the league has shied away from taking to the streets here, making this the first ever race on this circuit. Truly, all bets are fair as no real data on a circuit like this exists for the current field of drivers.
                ''')
    st.image(tracks_5)
    st.markdown('''
                **Week 12: Las Vegas** The street racing doesn't end in Jeddah as the drivers will face another daunting, high speed, and thrilling night race down the Las Vegas Strip. Following suit with many of our other tracks selected, Las Vegas hasn't had the league grace its pavement since the very first season.

                Of course, the league's top two drivers were on the podium here during Season 1, with Erick taking the win over Nick and retired driver Marcus rounding out the podium. Even though this is a street circuit, lined with walls, there is plenty of room for runoff and overtaking.

                All of this should make for a pretty ideal late season opportunity to grab a few more points and help secure each driver's position and their team's ranking going into the penultimate race of the season.

                **Week 13: Abu Dhabi** Yet another track that has always been on the calendar, and yet another track that Nick has yet to lose on. This could be the year though, as chasing the 4-peat is a daunting task. During this penultimate race of the season, last year's runner up Joshua will look to secure his first victory on this circuit.

                He has graced the podium twice, both in second place, while Marcus, Erick, and Brently have all taken home trophies from this circuit as well. Our intern was keen on adding a thought to this one too.
                ''')
    st.image(no_mikey)
    st.markdown('''
                **Week 14: Imola** Save the best for last is what they always say, and boy howdy did the league cook up a legendary finale. With another first ever appearance on the calendar, Imola will be the grounds on which we officially crown our champions.

                Drivers will be put to the test as if they are on a street circuit, but with the high speed thrills of one of the best permanent tracks out there. 

                Will Eddie cause another COTA? Will Alpine go back-to-back? Will Nick and Travis get their revenge? Can a rookie do the improbable and take home heaps of hardware and maybe a championship?

                All of this and so much more will be answered when the drivers start their engines at Imola. Hardware will be handed out and the season will come to a close. However, while it may cap off the season, Imola won't be the last time the drivers take to the pavement.
                ''')
    st.image(tracks_6)
    st.markdown('''
                **Post-Season: Monaco** The true finale of Season 4 will take place in Monaco. The famed circuit will once again host the post-season night race extravaganza.

                A special trophy will be granted to the winner of this one-off event and they will go down in the history of the league as one of the greats.
                ''')
    st.markdown(
        f"""

        <p style="color:lightgray;"> {date} - {author}</p>
        """,
        unsafe_allow_html=True,)
    st.divider()