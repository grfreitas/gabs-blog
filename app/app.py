import importlib

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

app = dash.Dash(__name__, url_base_pathname='/')

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

app.title = 'Gabs Blog'


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname is None or pathname == '/':
        pathname = '/home'

    uri = pathname.split('/')[1:]
    page = 'pages.' + '.'.join([folder for folder in uri]) + '.layout'

    resource = importlib.import_module(page)

    return resource.layout
