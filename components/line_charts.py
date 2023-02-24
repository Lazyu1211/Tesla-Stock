from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_year_volume, get_year_change, get_year_range, get_data

def render(app):
    df = get_year_volume()

    @app.callback(
        Output("line_volume", component_property='children'),
        Input("year_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("year in @dropdown")
        fig = px.line(
                filtered_data,
                x="year",
                y="Volume",
                title="Total Volume of Years")
        return html.Div(dcc.Graph(figure=fig),id="line_volume")
    return html.Div(id="line_volume")

def render1(app):
    df = get_year_change()

    @app.callback(
        Output("line_volume1", component_property='children'),
        Input("year_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("year in @dropdown")
        fig = px.line(
                filtered_data,
                x="year",
                y="change_open_close",
                title="Total Change of Years")
        return html.Div(dcc.Graph(figure=fig),id="line_volume1")       
    return html.Div(id="line_volume1")

def render2(app):
    df = get_year_range()

    @app.callback(
        Output("line_volume2", component_property='children'),
        Input("year_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("year in @dropdown")
        fig = px.line(
                filtered_data,
                x="year",
                y="range_high_low",
                title="Total Range of Years")
        return html.Div(dcc.Graph(figure=fig),id="line_volume2")       
    return html.Div(id="line_volume2")

def render3(app):
    df = get_data()
    fig = px.line(df, x='Date', y="Open", title="Open in Date")
    return html.Div(dcc.Graph(figure=fig), id="line_chart3")

def render4(app):
    df = get_data()
    fig = px.line(df, x='Date', y="Close", title="Close in Date")
    return html.Div(dcc.Graph(figure=fig), id="line_chart4")

def render5(app):
    df = get_data()
    fig = px.line(df, x='Date', y="Volume", title="Volume in Date")
    return html.Div(dcc.Graph(figure=fig), id="line_chart5")
