import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import numpy as np
import scipy
import matplotlib as plt
import seaborn
import plotly

import suicides
import younger_people
from dash.dependencies import Input, Output

#import csv
london_young_people = pd.read_csv('data/children & Younger people/indicators-CountyUA.data london young people.csv')


#gdhi = pd.read_csv("/data/")


navbar = dbc.NavbarSimple(
      children=[
        dbc.NavItem(dbc.NavLink("Younger People", href="/younger_people")),
          dbc.NavItem(dbc.NavLink("Suicides", href="/suicides")),
    ],
    brand="Mental Health Analysis",
    brand_href="#",
    sticky="top",
)


body = dbc.Container([
    dbc.Row(
        [
            dbc.Col([

                html.H1("Welcome to Mental Health Analysis"),
                html.Br(),
                html.H2("Please select one of the links in the navigation bar")



            ])
        ]
    )
])

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = html.Div([navbar,
    dcc.Location(id="url", refresh=False),
                       html.Div(id="page-content")])



index_page = html.Div([
    html.H1("Please Select a Page on the navigation Bar")
])

# Younger People callback


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == 'younger_people':
        return younger_people
    elif pathname == 'suicides':
        return suicides
    else:
        return index_page
    # You could also return a 404 "URL not found" page here



if __name__ == "__main__":
    app.run_server(debug=True)