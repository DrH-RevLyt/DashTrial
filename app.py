# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'dark-green': '#006600',
    'light-green': '#66cc00',
    'lighter-green': '190,240,160',
    'orange': '#ff9900',
    'anthrazit-grey': '#666666',
    'dark-grey': '#999999',
    'light-grey': '#cccccc'
}

app.layout = html.Div(style={'backgroundColor': colors['anthrazit-grey']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['light-grey']
        }
    ),

    html.Div(children='''
        Dash: A web application framework for python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['anthrazit-grey'],
                'paper_bgcolor': colors['background'],
                'font': {}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

