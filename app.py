import dash
import dash_bootstrap_components as dbc





app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX], url_base_pathname='/',
                meta_tags=[

                {
                    'http-equiv':'X-UA-Compatible',
                     'content': 'IE=edge'
                },
                {
                    'name': 'viewport',
                    'content': 'width=device-width, inital-scale=1.0'
                }])
app.title = 'Mental Health Analysis'
server = app.server
app.config.suppress_callback_exceptions = True


