
from dash import Dash, html, dcc
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_dropdown_list


def render(app):
    list_year = get_dropdown_list()
    all_year = [{'label':i,'value':i} for i in list_year]
    @app.callback(
    Output(component_id='year_dropdown', component_property='value'),
    Input(component_id='select_all_button', component_property='n_clicks')
    )
    def update_all_bedroom(n):
        return list_year

    return html.Div(
        children=[
            html.H6("Select year"),
            dcc.Dropdown(
                options=all_year,
                multi=True,
                id = "year_dropdown",
                value= 0
            ),
             dbc.Button(
                children=["Select all"],
                color="primary",
                className="me-1",
                id="select_all_button",
                n_clicks=0
             )
        ]
    )

