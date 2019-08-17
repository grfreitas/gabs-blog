import importlib

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

external_stylesheets = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
]

app = dash.Dash(__name__,
                url_base_pathname='/',
                external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

app.title = 'Blog do Gabs'


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname is None or pathname == '/':
        pathname = '/home'

    uri = pathname.split('/')[1:]
    page = 'pages.' + '.'.join([folder for folder in uri]) + '.layout'

    resource = importlib.import_module(page)

    return resource.layout
