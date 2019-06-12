import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app, server
import younger_people, suicides, home, error
import dash_bootstrap_components as dbc



navbar = dbc.NavbarSimple(
      children=[
        dbc.NavItem(dbc.NavLink("Younger People", href="/younger_people")),
          dbc.NavItem(dbc.NavLink("Suicides", href="/suicides")),

    ],
    brand="Mental Health Analysis",
    brand_href="/",
    sticky="top",
)

app.layout = html.Div([navbar,
    dcc.Location(id='url', refresh=False),

    html.Div(id='page-content')
], style={'margin':25})



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    if pathname == '/younger_people':
        return younger_people.younger_people_layout
    elif pathname == '/suicides':
        return suicides.suicides_layout
    elif pathname == '/':
        return home.home_layout
    else:
        return error.empty_layout


if __name__ == '__main__':
    app.run_server(debug=True)