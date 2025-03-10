import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

def Calculations():
    # Read in excel sheet
    df = pd.read_excel('The_Alternative_F1.xlsx', sheet_name='Season4')

    race_points = [col for col in df.columns if col.endswith('Points')]
    race_place = [col for col in df.columns if col.endswith('Place')]
    races = [col[:-6] for col in race_points]

    df['Total'] = 0
    for i in range(len(race_points)):
        df['Total'] = df['Total'] + df[race_points[i]]

    team_race_totals = pd.DataFrame([]) 
    for i in range(len(race_points)):
        if i == 0:
            team_race_totals[race_points[i]] = df.groupby('Team')[race_points[i]].sum()
        else:
            team_race_totals[race_points[i]] = df.groupby('Team')[race_points[i]].sum() \
                                                    + team_race_totals[race_points[i-1]]

    driver_race_totals = pd.DataFrame([])
    for i in range(len(race_points)):
        if i == 0:
            driver_race_totals[race_points[i]] = df.groupby('Driver')[race_points[i]].sum()
        else:
            driver_race_totals[race_points[i]] = df.groupby('Driver')[race_points[i]].sum() \
                                                    + driver_race_totals[race_points[i-1]]

    # Define team colors
    team_colors = {
        'Alpine': 'hotpink', 
        'Aston Martin': 'teal',
        'Ferrari': 'red',
        'McLaren': 'darkorange',
        'Red Bull': 'darkblue',
        'VCARB': 'blue',
        'AlphaTauri': 'LightSlateGray',
        'Alfa Romeo': 'Maroon',
        'Mercedes': 'black',
        'Haas': 'gray',
    }  

    # Driver colors
    driver_colors = {
        'Nick': 'darkorange', 
        'Travis': 'orange',
        'Patrick': 'blue',
        'Brently': 'lightblue',
        'Erick': 'red',
        'Del': '#ff6060',
        'Joshua': 'hotpink',
        'Eddie': 'lightpink',
        'Yeti': 'darkblue',
        'Boz': '#8888c9',
        'Newman': 'LightSlateGray',
        'Gary': 'black',
        'Zane': 'black'
    } 

    for i in range(len(race_place)):
        if df.loc[0,race_points[i]] == 0:
            index = i
            index_x = index-0.5
            break
        elif race_place[i] == race_place[-1]:
            index = i+1
            index_x = index
        else:
            x = 0

    # --- Team Plot ---

    # Add a new column of zeros at the beginning
    team_race_totals.insert(0, 'Start', 0)  
    team_race_totals = team_race_totals.T

    races.insert(0, 'Start') 

    # Create Plotly figure
    fig1 = go.Figure()

    for team in team_race_totals.columns:
        fig1.add_trace(go.Scatter(x=races,
                                y=team_race_totals[team], 
                                mode='lines+markers',
                                name=team, 
                                line=dict(color=team_colors.get(team))))

    fig1.update_layout(
        xaxis_range=[0,index],
        xaxis_title="Race",
        yaxis_title="Total Points",
        title="Constructor's Championship",
        hovermode="x unified" 
    )

    # --- Driver Plot ---

    # Add a new column of zeros at the beginning
    driver_race_totals.insert(0, 'Start', 0)  
    driver_race_totals = driver_race_totals.T 

    # Create Plotly figure
    fig2 = go.Figure()

    for driver in driver_race_totals.columns:
        fig2.add_trace(go.Scatter(x=races,
                                y=driver_race_totals[driver], 
                                mode='lines+markers',
                                name=driver,
                                line=dict(color=driver_colors.get(driver))))

    fig2.update_layout(
        xaxis_range=[0,index],
        xaxis_title="Race",
        yaxis_title="Total Points",
        title="Driver's Championship",
        hovermode="x unified" 
    )

    # Creates a list of all the points columns in the excel sheet
    points_columns = [col for col in df.columns if col.endswith(('Points', 'SprintPoints'))]
    fastest_lap_columns = [col for col in df.columns if col.endswith(('FastestLap'))]
    qualifying_columns = [col for col in df.columns if col.endswith(('Qualifying'))]
    place_columns = [col for col in df.columns if col.endswith(('Place'))]

    # Creates the order of the races to be graphed along the x-axis
    races_points_only = races.copy()
    del races_points_only[0]

    # Creates a new dataframe with only the drivers and points columns
    new_df = df.set_index('Driver')[points_columns]
    new_df = new_df.reset_index()

    # Creates a new dataframe with only the drivers and fastest laps columns
    new_df_FL = df.set_index('Driver')[fastest_lap_columns]
    new_df_FL = new_df_FL.reset_index()

    # Creates a new dataframe with only the drivers and qualifying columns
    new_df_Q = df.set_index('Driver')[qualifying_columns]
    new_df_Q = new_df_Q.reset_index()

    # Creates a new dataframe with only the drivers and placement columns
    new_df_Place = df.set_index('Driver')[place_columns]
    new_df_Place = new_df_Place.reset_index()

    drivers_total_points = []
    for i in range(len(new_df['Driver'])):
        driver_points = new_df.iloc[i, 1:].tolist()
        total_pointsN = sum(driver_points)
        drivers_total_points.append(total_pointsN)

    return team_race_totals,driver_race_totals,df,races,team_colors,fig1,fig2,race_place,race_points,index_x, \
        new_df,new_df_FL,new_df_Q,new_df_Place,races_points_only,drivers_total_points,driver_colors