
import dash_html_components as html
from app import  app


# 404 page

# In case users type something in the url which is not valid



empty_layout = html.Div([
    html.H1(' '),

#images have to be in asset folder
    html.Img(src=app.get_asset_url('404.png')),

    html.Div(id='404-content'),


])
