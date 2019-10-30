import dash_core_components as dcc
import dash_html_components as html

from utils import get_content

search_button = dcc.Input(
    id='search-input',
    type='search',
    placeholder='Pesquisar')

layout = html.Div(
    id='app-home',
    className='page',
    children=[

        # Header
        html.Div(
            id='full-header',
            children=[
                html.Div(
                    id='app-header',
                    className='header',
                    children=[
                        html.H2('Blog do Gabs')
                    ],
                ),
                html.Div(
                    id='app-menu',
                    children=[
                        dcc.Link(
                            'Início',
                            href='/',
                            className='tab first',
                        ),
                        dcc.Link(
                            'Sobre',
                            href='/',
                            className='tab',
                        ),
                    ]
                ),
                html.Hr([])
            ]),

        # Side bar layout
        html.Div(
            id='left-side-column',
            className='three columns',
            children=[
                html.Div(
                    id='search-field',
                    style={
                        'text-align': 'center'
                    },
                    children=[
                        html.I(className='fa fa-search', style={'margin-right': '5px', 'color': '#88C0D0'}),
                        search_button,
                    ]),

                html.Div(
                    id='tag-menu',
                    children=[
                        html.H6([html.I(className='fa fa-tags', style={'color': '#88C0D0'}), ' Tags']),
                    ]),

                html.Div(
                    id='category-menu',
                    children=[
                        html.H6([html.I(className='fa fa-bookmark', style={'color': '#88C0D0'}), ' Categorias']),
                    ]),

                html.Div(
                    id='about-me',
                    style={
                        'text-align': 'center'
                    },
                    children=[
                        html.Img(src='assets/selfie.png', className='avatar'),
                        html.A(html.P('Sobre mim'), href='/'),
                        html.Div(
                            children=[
                                html.A(href='https://twitter.com/boanoitegabs',
                                       target='_blank',
                                       children=html.I(className='fa fa-twitter',
                                                       style={'font-size': '25px'})),
                                html.A(href='https://github.com/grfreitas',
                                       target='_blank',
                                       children=html.I(className='fa fa-github',
                                                       style={'font-size': '25px', 'margin-left': '20px'})),
                                html.A(href='https://www.linkedin.com/in/grfreitas/',
                                       target='_blank',
                                       children=html.I(className='fa fa-linkedin',
                                                       style={'font-size': '25px', 'margin-left': '20px'})),
                            ])
                    ]),
            ]),

        # Content layout
        html.Div(
            id='right-side-column',
            className='nine columns',
            children=get_content()
        )
    ]
)
