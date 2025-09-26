import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

# Expands for each constructor: race results bar graph, best finish callout, total points callout,
# Total points bar graph for all constructors
# Add expands for each constructor with:
# - Number of fastest laps callout
# - Number of wins callout
# - Driver/Team Bios
def Tab3(team_df,team_races_points_only,index_x,drivers_points_df,colors_driver_team,colors_driver_df):
    # wins_df = new_df.copy()
    # wins_df = wins_df.mask(wins_df < "25", 0)
    # wins_df = wins_df.mask(wins_df > "24", 1)
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('''**Stacked Constructor Points**''')
        fig_name000 = "Stacked Constructor Points"

        # Ensure 'Points' column is numeric
        drivers_points_df['Points'] = pd.to_numeric(drivers_points_df['Points'], errors='coerce').fillna(0)

        # Get the list of teams, sorted by total points
        team_total_points = drivers_points_df.groupby('Team')['Points'].sum().sort_values(ascending=True)
        sorted_teams = team_total_points.index.tolist()

        # 1. Initialize an empty Figure
        globals()[fig_name000] = go.Figure()

        # 2. Define bar appearance and positions
        bar_height = 0.4  # This is the new 'width' for our horizontal bars
        offset = bar_height / 2.0  # We will shift each bar by half its height

        # 3. Create a set to track which drivers are already in the legend
        drivers_in_legend = set()

        # 4. Loop through each team to manually place bars
        for i, team in enumerate(sorted_teams):
            # Get the two drivers for the current team
            team_drivers_df = drivers_points_df[drivers_points_df['Team'] == team].reset_index(drop=True)

            # There might be one or two drivers
            if not team_drivers_df.empty:
                # --- Bar for the first driver ---
                driver_1_name = team_drivers_df.loc[0, 'Driver']
                driver_1_points = team_drivers_df.loc[0, 'Points']
                driver_1_color = dict(zip(colors_driver_df['Driver'], colors_driver_df['Color'])).get(driver_1_name)
                
                # Add to legend only if it's the first time we see this driver
                show_legend_1 = driver_1_name not in drivers_in_legend
                drivers_in_legend.add(driver_1_name)

                globals()[fig_name000].add_trace(go.Bar(
                    y=[i - offset], # Position below the centerline for the team
                    x=[driver_1_points],
                    name=driver_1_name,
                    orientation='h',
                    width=bar_height,
                    marker_color=driver_1_color,
                    legendgroup=driver_1_name,
                    showlegend=show_legend_1
                ))

                # --- Bar for the second driver (if they exist) ---
                if len(team_drivers_df) > 1:
                    driver_2_name = team_drivers_df.loc[1, 'Driver']
                    driver_2_points = team_drivers_df.loc[1, 'Points']
                    driver_2_color = dict(zip(colors_driver_df['Driver'], colors_driver_df['Color'])).get(driver_2_name)

                    # Add to legend only if it's the first time we see this driver
                    show_legend_2 = driver_2_name not in drivers_in_legend
                    drivers_in_legend.add(driver_2_name)
                    
                    globals()[fig_name000].add_trace(go.Bar(
                        y=[i + offset], # Position above the centerline for the team
                        x=[driver_2_points],
                        name=driver_2_name,
                        orientation='h',
                        width=bar_height,
                        marker_color=driver_2_color,
                        legendgroup=driver_2_name,
                        showlegend=show_legend_2
                    ))

        # 5. Final Layout Configuration
        globals()[fig_name000].update_layout(
            barmode='stack', # This mode works best with pre-positioned bars
            yaxis=dict(
                tickvals=list(range(len(sorted_teams))), # Set ticks at integer positions 0, 1, 2...
                ticktext=sorted_teams  # Label those ticks with team names
            ),
            legend_tracegroupgap=0 # Adds a little space between driver groups in the legend
        )

        st.plotly_chart(globals()[fig_name000],use_container_width=True)
    
    with col4:
        st.markdown('''**Individual Constructor Statistics**''')
        # Loops through each constructor to create an expand with their information only
        for i in range(len(team_df['Team'])):
            with st.expander(team_df['Team'][i]):
                team_name = team_df['Team'][i]  # Get the team's name
                team_points = team_df.iloc[i, 1:].tolist()

                # Create the figure name using the constructor's name
                fig_name = f"{team_name} Points Per Race"
                
                # 15 unique colors
                colors = [
                    '#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', 
                    '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', 
                    '#800000'
                ]

                # Use globals() to dynamically create the variable
                globals()[fig_name] = px.bar(x=team_races_points_only, y=team_points, title=fig_name,
                                             color=team_races_points_only,
                                             color_discrete_sequence=colors)
                
                globals()[fig_name].update_traces(width=0.8) 
                
                globals()[fig_name].update_xaxes(categoryorder='array', categoryarray=team_races_points_only)

                # Update x-axis title
                globals()[fig_name].update_xaxes(title_text="Race", categoryorder='array', categoryarray=team_races_points_only)

                # Update y-axis title
                globals()[fig_name].update_yaxes(title_text="Points")

                # Update layout
                # globals()[fig_name].update_layout(xaxis_range=[-0.5,index_x], showlegend=False)

                # Calculates the highest placement a driver has achieved
                highest_score = max(team_points)
                index = team_points.index(highest_score)
                best_result = 'Best Result: ' + team_races_points_only[index] + ' (' + str(highest_score) + ' points)'
                button_key = 'TeamButton' + "_" + str(i)

                # Calculates the total points for a team
                button_key1 = button_key + "_" + str(i)
                total_pointsN = sum(team_points)
                total_points = 'Total Points: ' + str(total_pointsN)
                # Create full list of team total points
                team_total_points = []
                team_total_points.append(total_pointsN)

                # Creates the layout for each expand
                col1, col2 = st.columns(2)
                with col1:
                    st.button(total_points,key=button_key1)
                with col2:
                    st.button(best_result,key=button_key)
                st.plotly_chart(globals()[fig_name])

    return colors