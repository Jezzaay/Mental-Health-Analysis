import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table

from app import app

home_layout = html.Div([



        html.Div([

            html.H1('Welcome to Mental Health Analysis ', id="title"),

        ]),



        html.P("Analysis on Younger people and Suicides with economical data"),

        html.Div(id='home-content'),




])

html.Div([


    html.P("Analysis on Younger people and Suicides with economical data"),

    html.Div(id='para-content')


])
