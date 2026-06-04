import polars as pl
import numpy as np
import time
import pandas as pd
import os
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
from datetime import date
import plotly.graph_objects as go




df = pl.read_excel("C:\\Anupam\\GIT\\base\\cursorFolder\\tools\\BhavData\\BhavData\\*_Feb*_sec_bhavdata_full.xlsx")
print(df)
print(df.shape)

# df = df.filter([(pl.col('SYMBOL') == 'ACC') & (pl.col(' DATE1').str.strip_chars() == ('04-Feb-2020'))])
df = df.filter([
     (pl.col(' DATE1').str.strip_chars() == ('04-Feb-2020'))
     &
     (pl.col(' SERIES').str.strip_chars() == 'EQ')
     ])


# df = df.with_columns(pl.col(' DATE1').str.to_date("%YW%W-%u"))
df = df.with_columns(pl.col(' DATE1').str.strip_chars())

# print("--------------------------------")
# print(df)


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)


BG_WHITE = "#ffffff"
TEXT_BLACK = "#000000"
GRID_GREY = "#e6e6e6"

app.layout = dbc.Container(
    fluid=True,
    style={"backgroundColor": BG_WHITE},
    className="p-2",
    children=[
        dbc.Row(
            dbc.Col(
                html.H3("Scatter Plot of PREV_CLOSE and SYMBOL"),
            )
        ),
        dbc.Row(
            dbc.Col(
                dcc.Graph(
                    config={"displayModeBar": False},
                    figure=go.Figure(go.Scatter(
                        x=df['SYMBOL'], y=df[' PREV_CLOSE'], mode='markers', 
                        marker=dict(size=1,
                        color='rgba(152, 0, 153, 0.7)', 
                        line=dict(width=1, color='rgb(0, 0, 0)'))
                        )).update_yaxes(range=[0, 1000]
                        ).update_xaxes(tickfont=dict(size=8)
                        ).update_layout(
                            title= dict(
                                text='Your Custom Title',
                                xanchor='center',
                                x=0.5
                            ),
                            xaxis= dict(
                            tickangle=-45,
                            title='Your Custom X-Axis Title',
                            gridcolor='white',
                            ), yaxis= dict(
                                title='Your Custom Y-Axis Title',
                                showgrid=True,
                                gridcolor='white',
                                gridwidth=1
                            ),
                            paper_bgcolor='white',
                            plot_bgcolor='white'
                        ))
            )
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)






