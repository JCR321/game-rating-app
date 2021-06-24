# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
from joblib import load
pipeline = load("pages/pipeline.joblib")

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='nb-5'),
        dcc.Markdown('#### alcohol_reference'),
        dcc.Slider(
            id='alcohol_reference',
            min=0,
            max=1,
            step=1,
            value=0.05,
            marks={n: str(n) for n in range (0,1,1)},
            className='nb-5',
        ),
        dcc.Markdown('#### Continent'),
        dcc.Dropdown(
            id='continent',
            options = [
                {'label': 'Africa', 'value': 'Africa'},
                {'label': 'Americas', 'value': 'Americas'},
                {'label': 'Asia', 'value': 'Asia'},
                {'label': 'Europe', 'value': 'Europe'},
                {'label': 'Oceania', 'value': 'Oceania'},
            ],
            value = 'Africa',
            className = 'nb-5'
        )
    ]
)

layout = dbc.Row([column1, column2])