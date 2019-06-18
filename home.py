import dash_html_components as html


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
