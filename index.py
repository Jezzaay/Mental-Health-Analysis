import dash_core_components as dcc # This is needed for e.g. the location changing on the nav page or dcc.graph
import dash_html_components as html # html is needed for Header, Paragraph and Div tags.
from dash.dependencies import Input, Output
from app import app
import younger_people, suicides, home, error # Importing Other pages for the nav page.
import dash_bootstrap_components as dbc


#Navigation Bar.
navbar = dbc.NavbarSimple(
      children=[
        dbc.NavItem(dbc.NavLink("Younger People", href="/younger_people")),
          dbc.NavItem(dbc.NavLink("Suicides", href="/suicides")),

    ],
    brand="Mental Health Analysis",
    brand_href="/", # Goes back to home page
    sticky="top", # Stays on top of the page no matter when scrolling.
)

app.layout = html.Div([navbar,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content') # displays the page information in this div.
], style={'margin':25}) # margin of 25 so the page isn't across to edges of the web browser.


# Site layout to change pages
# "/" goes back to the home page if not included the title text would ultimately do nothing
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