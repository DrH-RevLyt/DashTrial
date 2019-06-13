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
    'light-grey': '#cccccc',
    'dark': '#333',
    'light-text': '#ccc',
    'white': '#fff'
}

app.layout = html.Div(style={'backgroundColor': colors['dark']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['white']
        }
    ),

    html.Div(children='''
        Dash: A web application framework for python.
    ''',
         style={
             'textAlign': 'center',
             'color': colors['light-text']
         }
     ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['dark'],
                'paper_bgcolor': colors['dark'],
                'font': {
                    'color': colors['orange']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

