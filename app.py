import dash
import dash_bootstrap_components as dbc





app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX], url_base_pathname='/',
                meta_tags=[
#meta tags could be useful in the future, added for now.
                {
                    'http-equiv':'X-UA-Compatible',
                     'content': 'IE=edge'
                },
                {
                    'name': 'viewport',
                    'content': 'width=device-width, inital-scale=1.0'
                }])
app.title = 'Mental Health Analysis' #Title on top of the webpage.
# Not dynmaic when changing as Dash interface to include this takes a workaround which is not needed for the project.
server = app.server
app.config.suppress_callback_exceptions = True


