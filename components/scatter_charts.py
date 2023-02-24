from dash import Dash,html,dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_data


def render(app):
    df = get_data()
    fig = px.scatter(
            df, 
            x="Open", 
            y="Close",
            title="Open and Close Price",
            color="Volume",
            size="Volume",
            )
    return html.Div(dcc.Graph(figure=fig), id="scatter")

def render1(app):
    df = get_data()
    fig = px.scatter(
            df, 
            x="High", 
            y="Low",
            title="Highest and lowest Price",
            color="Volume",
            size="Volume",
            )
    return html.Div(dcc.Graph(figure=fig), id="scatter1")

def render2(app):
    df = get_data()
    fig = px.scatter(
            df, 
            x="range_high_low", 
            y="change_open_close",
            title="Highest and lowest Price",
            color="Volume",
            size="Volume",
            )
    return html.Div(dcc.Graph(figure=fig), id="scatter2")