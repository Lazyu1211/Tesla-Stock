from dash import Dash,html
import dash_bootstrap_components as dbc
from components import line_charts, bar_charts, dropdown, scatter_charts

image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6Aevp--whIvGgmLCBkqulT0kXj7gTyJuIKA&usqp=CAU"
image_path1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTcd-pgI73QLis9L0sEeq_FSgNBnBP1L08CQ&usqp=CAU"

def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.P(children="✨✨✨✨✨✨✨✨✨", className="header-emoji"),
        html.H1(
                "Tesla Stock Price Analysis!!!", className="header-title"
              ),
        html.P(
                "Base on the dataset we can analysis the Tesla Stock!!!🔥🔥🔥✨✨✨",
                className="header-description",
                ),
        html.Img(src=image_path, style={"width": "660px", "height": "400px"}),
        html.Img(src=image_path1, style={"width": "660px", "height": "400px"}),
        dropdown.render(app)
        
,       
    ],className="mt-4"),
        dbc.Row([
            dbc.Col(line_charts.render(app),lg=4),
            dbc.Col(line_charts.render1(app),lg=4),
            dbc.Col(line_charts.render2(app),lg=4),
            dbc.Col(bar_charts.render(app),lg=6),
            dbc.Col(line_charts.render5(app),lg=6),
            dbc.Col(line_charts.render3(app),lg=6),
            dbc.Col(line_charts.render4(app),lg=6),
            dbc.Col(scatter_charts.render(app),lg=12),
            dbc.Col(scatter_charts.render1(app),lg=12),
            dbc.Col(scatter_charts.render2(app),lg=12)
        ],className="mt-4")
    ])