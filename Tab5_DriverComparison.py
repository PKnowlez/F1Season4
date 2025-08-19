import pandas as pd
import streamlit as st
import plotly.express as px

def Tab5(new_df, average_changed, drivers_total_points, average_qualifying, average_place, fig3, rookies):

    # Combine all data into a single DataFrame
    full_data_df = pd.DataFrame({
        'Driver': new_df['Driver'],
        'average_changed': average_changed,
        'drivers_total_points': drivers_total_points,
        'average_qualifying': average_qualifying,
        'average_place': average_place
    })

    # Create a single toggle for "Rookies Only"
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        rookies_only = st.toggle('Rookies Only', value=False)

    # This is the updated section. The chart for fig3 now only displays
    # if the 'Rookies Only' toggle is True.
    if rookies_only:
        st.plotly_chart(fig3)
    
    # Filter the combined DataFrame based on the toggle state
    if rookies_only:
        filtered_df = full_data_df[full_data_df['Driver'].isin(rookies)]
    else:
        filtered_df = full_data_df

    # --------------------- #
    # Create the figure for Average Positions Gained or Lost Per Race
    fig_name4 = "Average Positions Gained or Lost Per Race"
    avg_changed_df = filtered_df.groupby('Driver')['average_changed'].sum().reset_index()
    avg_changed_df = avg_changed_df.sort_values(by='average_changed', ascending=False)
    colors = ['green' if val >= 0 else 'red' for val in avg_changed_df['average_changed']]
    globals()[fig_name4] = px.bar(
        x=avg_changed_df['Driver'], 
        y=avg_changed_df['average_changed'], 
        title=fig_name4, 
        color=colors,
        color_discrete_map="identity"
    )
    globals()[fig_name4].update_xaxes(title_text="Driver")
    globals()[fig_name4].update_yaxes(title_text="Positions Changed")

    # --------------------- #
    # Create the figure for Points Per Driver
    fig_name5 = "Points Per Driver"
    drivers_points_df = filtered_df.groupby('Driver')['drivers_total_points'].sum().reset_index()
    drivers_points_df = drivers_points_df.sort_values(by='drivers_total_points', ascending=False)
    colors = ['#FFD700', '#C0C0C0', '#CD7F32', '#0068c9', '#0068c9', '#0068c9', '#0068c9', 
              '#0068c9', '#0068c9', '#0068c9', '#0068c9', '#0068c9', '#0068c9', '#0068c9']
    globals()[fig_name5] = px.bar(
        x=drivers_points_df['Driver'],
        y=drivers_points_df['drivers_total_points'],
        title=fig_name5,
        color=colors[:len(drivers_points_df)],
        color_discrete_map="identity"
    )
    globals()[fig_name5].update_xaxes(title_text="Driver")
    globals()[fig_name5].update_yaxes(title_text="Points")

    # --------------------- #
    # Create the figure for Average Qualifying Position
    fig_name6 = "Average Qualifying Position"
    avg_qualifying_df = filtered_df.groupby('Driver')['average_qualifying'].sum().reset_index()
    avg_qualifying_df = avg_qualifying_df.sort_values(by='average_qualifying', ascending=True)
    globals()[fig_name6] = px.bar(
        x=avg_qualifying_df['average_qualifying'],
        y=avg_qualifying_df['Driver'], 
        title=fig_name6, 
        color=colors[:len(avg_qualifying_df)],
        color_discrete_map="identity",
        orientation='h'
    )
    globals()[fig_name6].update_xaxes(title_text="Qualifying Position")
    globals()[fig_name6].update_yaxes(title_text="", autorange="reversed")

    # --------------------- #
    # Create the figure for Average Place
    fig_name7 = "Average Place"
    avg_place_df = filtered_df.groupby('Driver')['average_place'].sum().reset_index()
    avg_place_df = avg_place_df.sort_values(by='average_place', ascending=True)
    globals()[fig_name7] = px.bar(
        x=avg_place_df['average_place'],
        y=avg_place_df['Driver'], 
        title=fig_name7, 
        color=colors[:len(avg_place_df)],
        color_discrete_map="identity",
        orientation='h'
    )
    globals()[fig_name7].update_xaxes(title_text="Place")
    globals()[fig_name7].update_yaxes(title_text="", autorange="reversed")

    # --- Display Leader Buttons and Charts --- #
    with col2:
        if not drivers_points_df.empty:
            button_text = "Points Leader: " + drivers_points_df.loc[drivers_points_df['drivers_total_points'].idxmax(), 'Driver']
            st.button(button_text, key='Points Leader')
    with col3:
        if not avg_changed_df.empty:
            button_text = "Positions Gained Leader: " + avg_changed_df.loc[avg_changed_df['average_changed'].idxmax(), 'Driver']
            st.button(button_text, key='Positions Gained Leader')
    with col4:
        if not avg_qualifying_df.empty:
            button_text = "Qualifying Leader: " + avg_qualifying_df.loc[avg_qualifying_df['average_qualifying'].idxmin(), 'Driver']
            st.button(button_text, key='Qualifying Leader')
    with col5:
        if not avg_place_df.empty:
            button_text = "Place Leader: " + avg_place_df.loc[avg_place_df['average_place'].idxmin(), 'Driver']
            st.button(button_text, key='Place Leader')
            
    col6, col7 = st.columns(2)
    with col6:
        st.plotly_chart(globals()[fig_name5])
        st.plotly_chart(globals()[fig_name6])
    with col7:
        st.plotly_chart(globals()[fig_name4])
        st.plotly_chart(globals()[fig_name7])
