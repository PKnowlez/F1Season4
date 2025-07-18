import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy_garden.graph import Graph, MeshLinePlot

import kivy
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
# import Calculations

# team_race_totals,driver_race_totals,df,races,team_colors,fig1,fig2,race_place,race_points,index_x, \
#         new_df,new_df_FL,new_df_Q,new_df_Place,races_points_only,drivers_total_points,driver_colors \
#             = Calculations.Calculations()

class TheAlternativeMobileApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button1 = Button(text='Hello from Python!')
        button2 = Button(text='Another Button')
        layout.add_widget(button1)
        layout.add_widget(button2)
        return layout

if __name__ == '__main__':
    TheAlternativeMobileApp().run()

    
    
