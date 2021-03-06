import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px

colors = {
    'background': '#636161',
    'text': '#B2ACAB'
}

youth = pd.read_csv("C:/Users/Utilisateur/Desktop/cours/Python_pour_la_data/projet/youth_alcohol/bdd_utiles/youth_cont.csv")
youth_eu = youth[youth.Continent == 'EU']
fig_1 = px.choropleth(youth_eu , locations='Alpha-3 code', color='15-19 years old, current drinkers both sexes (%)',
                           color_continuous_scale=px.colors.sequential.Greys,
                           range_color=(youth_eu['15-19 years old, current drinkers both sexes (%)'].min(), youth_eu['15-19 years old, current drinkers both sexes (%)'].max()),
                           scope="europe", color_discrete_map = colors['background'],
                           labels={'unemp':'unemployment rate'}
                          )
fig_1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

util = pd.read_csv("C:/Users/Utilisateur/Desktop/cours/Python_pour_la_data/projet/youth_alcohol/bdd_utiles/util_cont.csv")
util = util[util.Continent == 'EU']
fig_2 = px.choropleth(util , locations='COUNTRY', color='Value',
                           color_continuous_scale=px.colors.sequential.Greys,
                           range_color=(util.Value.min() , util.Value.max()),
                           scope="europe", color_discrete_map = colors['background'],
                           animation_frame = 'Year' ,
                           labels={'unemp':'unemployment rate'}
                          )
fig_2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])


fig_3 = px.bar_polar(util, r="Value", theta="Country", color="Value", template='ggplot2',
        color_continuous_scale= px.colors.sequential.amp , color_discrete_map = colors['background'])
fig_3.update_layout(
plot_bgcolor=colors['background'],
paper_bgcolor=colors['background'],
font_color=colors['text'])


row_1 = dbc.Row(style = {'backgroundColor' : colors['background'] , 'width': '100%'} , children =[
                dbc.Col(
                    dbc.FormGroup([
                        html.H1(children="Consommation d'alcool en Europe" ,
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']}),
                        dcc.Graph(
                            style = {'backgroundColor' : colors['background'] , 'width': '100%', 'display': 'inline-block'},
                            id='map',
                            figure=fig_1
                        )
                    ]),width = 6),

                dbc.Col(
                    dbc.FormGroup([
                        html.H1(children="Evolution du nombre d'accidents chez les jeunes" ,
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']}),
                        dcc.Graph(
                            style = {'backgroundColor' : colors['background'] , 'width': '100%', 'display': 'inline-block'},
                            id='bar',
                            figure=fig_2
                        )
                    ]))])#, width = 6 ,  style={"height": "100%"})])

row_2 = dbc.Row(style = {'backgroundColor' : colors['background'] , 'width': '100%'} , children =[
        dbc.Col(
            dbc.FormGroup([
                html.H1(children="Deuxième colonne" ,
                        style={
                            'textAlign': 'center',
                            'color': colors['text']}),
                dcc.Graph(
                    style = {'backgroundColor' : colors['background'] , 'width': '100%', 'display': 'inline-block'},
                    id='bar',
                    figure=fig_3
                )
            ]),  style={"height": "100%"})
])

page_test_layout = html.Div(style = {'backgroundColor' : colors['background'] , 'width': '100%' , 'height' : '100%'} , children = [
                                row_1,

                                row_2
                    ])
