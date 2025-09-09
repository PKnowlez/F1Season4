import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image
import pandas as pd
import plotly.graph_objects as go

intern = Image.open("./Images/Intern Track Ranking.png")
average = Image.open("./Images/Average Votes.png")
most = Image.open("./Images/Most Votes.png")

rankings_order = {
    "Week":     [
        'Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8',
        'Week 9', 'Week 10', 'Week 11', 'Week 12', 'Week 13', 'Week 14'
    ],
    "Track":    [
        'Bahrain', 'Miami', 'Spain', 'Mexico', 'Baku', 'Austria (R)', 'Spa', 'Brazil',
        'Austria', 'Zandvoort', 'Jeddah', 'Las Vegas', 'Abu Dhabi', 'Imola'
    ],
    "Ranking":  [
        '2', '4', '3', '2', '0', '2', '4', '4', '3', '3', '0', '0', '3', '1'
    ]
}

carousel_images = [
            {
                "title": "",
                "text": "",
                "img": "./Images/W1 - Bahrain.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W2 - Miami.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W3 - Spain.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W4 - Mexico.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W5 - Baku.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W6 - Austria Reverse.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W7 - Spa.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W8 - Brazil.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W9 - Austria.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W10 - Zandvoort.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W11 - Jeddah.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W12 - Las Vegas.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W13 - Abu Dhabi.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/W14 - Imola.png"
            },
        ]

def article():
    date = "Sunday 09/07/2025"
    author = "Patrick"

    st.subheader('''Track Rankings, Driver's Edition''')
    st.markdown('''
                **A Word From Our Intern**
                > Just know, if your favorite track got bodied in these rankings, it's time to rethink your favorite track.
                >
                > -The Intern
                ''')
    st.markdown('''
                With our intern's rankings released and driver voting complete, it is time to reveal how we all view this season's calendar. Below you will find a comparison of the intern's ranking, the average voting position per track, and rankings based on which tier each track was voted most for. Additionally, at the end of the article, there is a synopsis of when these tracks occur on the calendar and which stints might be the most enjoyable for the league.
                ''')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('''**The Intern's Rankings**''')
        st.image(intern)
    with col2:
        st.markdown('''**Average Ranking**''')
        st.image(average)
    with col3:
        st.markdown('''**Most Votes Rankings**''')
        st.image(most)
    st.markdown('''
                Reviewing this data, it is clear to see that, indeed, Miami is a liked track. This comes contrary to some of the league's more prolific drivers, but will come as a delight to Erick "Miami ~~Fan~~ Lover" Tavera.

                Some additional insights are clear in this data as well. First and maybe foremost, the league generally prefers dedicated circuits as opposed to street circuits. So much so that the most eggregious of street circuits all received their most votes in the lowest tier.

                Second, Baku is clearly the most disliked track on the calendar. Even though last year it provided one of the most hotly competed races of the season. With tire degredation seemingly a larger impact than in previous seasons, there is a chance Baku provides another thriller.

                Finally, the league seems to love a Sprint. All three of the tracks that received S-Tier as their top vote getting tier are Sprints this season. Hopefully this leads the drivers to some excellent racing during the Sprints and the reverse grid regular races.
                ''')
    step_graph = create_step_graph(rankings_order)
    st.markdown('''**Rankings Across the Season**''')
    st.plotly_chart(step_graph, use_container_width=True)
    st.markdown('''
                Above we see the rankings of the tracks, based on their Most Votes ranking, plotted against the order in which they occur over the course of this season.

                What this tells us is that the middle stint of the season from Spa to Zandvoort is sure to be a memorable series of races regardless of results.

                Coming back from the Winter Break, drivers are faced with a gauntlet as they take on Jeddah and Las Vegas back to back. Both of these tracks fall into the D-Tier with respect to Most Votes.

                Finally, the season is both beginning and closing with tracks that find themselves lost in the quagmire of the middle tiers. Which should allow drivers to simply focus on the racing and not let the emotions of a track they love or hate take over during those moments.
                ''')
    st.markdown('''**Per Track Results**''')
    carousel(items=carousel_images, interval=20000)
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()

def create_step_graph(data):
    """
    Creates a Plotly step function graph from the provided data.

    Args:
        data (dict): A dictionary containing 'Track' and 'Ranking' data.
    
    Returns:
        plotly.graph_objects.Figure: The step function plot.
    """
    # Create a pandas DataFrame from the input data
    df = pd.DataFrame(data)

    # Convert the 'Ranking' column to a numeric type, as it's initially a string
    df['Ranking'] = pd.to_numeric(df['Ranking'])

    # Create the Plotly figure
    fig = go.Figure()

    # Add a scatter plot trace with a step-like line shape.
    # The 'hv' shape ensures a horizontal-vertical step pattern.
    fig.add_trace(go.Scatter(
        x=df['Track'],
        y=df['Ranking'],
        mode='lines',
        line=dict(shape='hv', color='red', width=2),
        name='Ranking',
        hovertemplate='Track: %{x}<br>Ranking: %{y}<extra></extra>'
    ))
    
    # Customize the graph layout
    fig.update_layout(
        xaxis_title="Track",
        yaxis_title="Ranking",
        # Use custom tick values and text for the y-axis to display grades
        yaxis=dict(
            tickvals=[0, 1, 2, 3, 4],
            ticktext=['D', 'C', 'B', 'A', 'S'],
            range=[-0.5, 4.5]
        ),
        # Center the x-axis labels
        xaxis=dict(
            tickangle=45,
            range=[-0.5,13.5]
        ),
        # Add a grid for better readability
        xaxis_showgrid=True,
        yaxis_showgrid=True
    )
    
    return fig

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