import dash_html_components as html


from app import app

home_layout = html.Div([



        html.Div([

            html.H1('Welcome to Mental Health Analysis ', id="title"),

        ]),



        html.P("Analysis on Younger people and Suicides with gross disposable household income (GDHI)"
               " and house prices."),

        html.Br(),

        html.P("Gross disposable household income should be the amount of money that individuals have available f"
               "or spending after tax has been taken off.  "),

        html.Br(),

        html.P("House prices are the average across the selected areas which will be showed."
               "I have attempted to accurately only show areas which the datasets overlap with both house prices "
               "and GDHI"),




        html.Div(id='home-content'),



])

html.Div([


    html.P("Analysis on Younger people and Suicides with economical data"),

    html.Div(id='para-content')


])
