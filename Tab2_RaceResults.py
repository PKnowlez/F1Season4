import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

# Expands for each race: Reports race results like post race screen
def Tab2(races,df,race_place,race_points):
    with st.expander('Preseason: Silverstone'):
        st.subheader("Winner: " + 'Jayden' + " - " + 'Mercedes')
        preseason = {
            "Place":                ['1','2','3','4','5','6','7','8','9','10','11','12','DNF','DNF/S'],
            "Driver":               ['Jayden','Joshua','Del','Nick','Jairo','Patrick','Eddie','Brently','Travis','Matthew','Erick','Josh','Leo','Boz'],
            "Team":                 ['Mercedes','Alpine','Aston Martin','McLaren','Mercedes','VCARB','Alpine','Red Bull','McLaren','Red Bull','Ferrari','VCARB','Ferrari','Aston Martin'],
            "Qualifying":           ['3','1','5','2','9','4','7','6','12','11','8','10','14','13'],
            "Fastest Lap":          ['Yes','-','-','-','-','-','-','-','-','-','-','-','-','-'],
            "Driver of the Day":    ['-','-','-','-','-','-','-','-','-','Yes','-','-','-','-'],
            "Most Overtakes":      ['-','-','-','-','-','-','-','-','-','-','-','Yes','-','-'],
            "Cleanest Driver":      ['-','-','Yes','-','-','-','-','-','-','-','-','-','-','-']
        }

        preseason_df = pd.DataFrame(preseason)
        st.dataframe(preseason_df, hide_index=True)     

    for i in range(len(races)):
        if i == 0:
            x = 0
        else:
            if not pd.isnull(df.loc[1,race_place[i-1]]):
                with st.expander(races[i]):
                    df_sorted = df.sort_values(race_place[i-1], ascending=True)
                    winner = df_sorted['Driver'].iloc[0]
                    constructor = df_sorted['Team'].iloc[0]
                    st.subheader("Winner: " + winner + " - " + constructor)
                    
                    # Construct the correct column name
                    qualifying_col = races[i] + 'Qualifying' 
                    if '(S)' in races[i]:
                        qualifying_col = races[i].replace(' (S)', '') + 'SprintQualifying'

                    fastestlap_col = races[i] + 'FastestLap'
                    if '(S)' in races[i]:
                        fastestlap_col = races[i].replace(' (S)','') + 'SprintFastestLap'

                    DOTD_col = races[i] + 'DOTD'
                    if '(S)' in races[i]:
                        DOTD_col = races[i].replace(' (S)','') + 'SprintDOTD'

                    MOT_col = races[i] + 'MOT'
                    if '(S)' in races[i]:
                        MOT_col = races[i].replace(' (S)','') + 'SprintMOT'

                    CD_col = races[i] + 'CD'
                    if '(S)' in races[i]:
                        CD_col = races[i].replace(' (S)','') + 'SprintCD'

                    race_results_df = pd.DataFrame({
                    'Place': df_sorted[race_place[i-1]],
                    'Driver': df_sorted['Driver'],
                    'Team': df_sorted['Team'],
                    'Qualifying': df_sorted[qualifying_col],
                    'Points': df_sorted[race_points[i-1]],
                    'Fastest Lap': df_sorted[fastestlap_col],
                    'Driver of the Day': df_sorted[DOTD_col],
                    'Most Overtakes': df_sorted[MOT_col],
                    'Cleanest Driver': df_sorted[CD_col]
                    })

                    race_results_df['Place'] = race_results_df['Place'].replace({
                        21: 'DNF', 
                        22: 'DNS',
                        '21': 'DNF', 
                        '22': 'DNS'
                    })

                    race_results_df['Qualifying'] = race_results_df['Qualifying'].replace({
                        21: 'DNF', 
                        22: 'DNS',
                        '21': 'DNF', 
                        '22': 'DNS'
                    })
                    
                    loop_columns = ['Fastest Lap','Driver of the Day','Most Overtakes','Cleanest Driver']

                    for n in range(len(loop_columns)):
                        race_results_df[loop_columns[n]] = race_results_df[loop_columns[n]].replace({
                            'y': 'Yes', 
                            'n': '-',
                            'Y': 'Yes',
                            'N': '-'
                        })

                    st.dataframe(race_results_df, hide_index=True)
            else:
                x = 0