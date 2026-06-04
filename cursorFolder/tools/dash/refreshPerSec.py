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
from datetime import datetime

from dash import dcc, html, Input, Output

import polars as pl


df = pl.read_excel("C:\\Anupam\\GIT\\base\\cursorFolder\\tools\\BhavData\\BhavData\\*_Dec*_sec_bhavdata_full.xlsx")
# Source - https://stackoverflow.com/a/78318470
# Posted by Dean MacGregor
# Retrieved 2026-05-31, License - CC BY-SA 4.0

df.columns=pl.Series(df.columns).str.strip_chars()
df_clean = df.with_columns(
    pl.col(pl.String).str.strip_chars()
)


df = df.with_columns(
    pl.col("DATE1").str.strptime(
        pl.Date,
        format="%d-%b-%Y"
    ).alias("DATE")
)

datelist = df.select(pl.col("DATE")).unique()

datelist = pl.Series(datelist).sort()

xListDate = []
xListSymbol = []
yList = []


for i in range(len(datelist)-1):
    # print(datelist[i])
    # print(df.filter(pl.col("DATE") == datelist[i]))
    # time.sleep(1)
    xListDate.append(datelist[i])
    xListSymbol.append(df.filter(pl.col("DATE") == datelist[i])['SYMBOL'])
    yList.append(df.filter(pl.col("DATE") == datelist[i])['CLOSE_PRICE'])


# print(xListSymbol)
# print(yList)


#---------------------

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)


BG_WHITE = "#ffffff"
TEXT_BLACK = "#000000"
GRID_GREY = "#e6e6e6"


app.layout = html.Div([
    dcc.Graph(id="scatter-chart"),
    dcc.Graph(id="line-chart"),
    # Fires every second
    dcc.Interval(
        id="interval-component",
        interval=300,  # milliseconds
        n_intervals=0
    )
])

fig2xAxis = []

@app.callback(
    Output("scatter-chart", "figure"),
    Output("line-chart", "figure"),
    Input("interval-component", "n_intervals")
)



def update_chart(n_intervals):
    print(n_intervals)
    if n_intervals >= len(xListDate):
        n_intervals = 0
    else:
        n_intervals = n_intervals



    # Cycle through TradeDate values
    # filter_value = filter_values[
    #     n_intervals % len(filter_values)
    # ]

    filtered = df.filter(
        pl.col("DATE") == xListDate[n_intervals]
    )

    fig = go.Figure(
        go.Scatter(
            x=filtered["SYMBOL"].to_list()[:5000],
            y=filtered["CLOSE_PRICE"].to_list(), mode='markers', 
                        marker=dict(size=1,
                        color='rgba(0, 0, 0, 0.1)', 
                        line=dict(width=1, color='rgb(0, 0, 0)'))
        )
    ).update_yaxes(range=[0, 800]
                        ).update_xaxes(tickfont=dict(size=1)
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
                        )


    #------ Second Chart Start ------
    filtered_scrip = filtered.filter(pl.col("SYMBOL") == "20MICRONS")
    
    fig2yAxis = fig2xAxis.append (filtered.filter(pl.col("SYMBOL") == "20MICRONS"))

    fig2 = go.Figure(
        go.Scatter(
            x=fig2xAxis,
            y=filtered_scrip["CLOSE_PRICE"].to_list().sort(),
            mode="markers"
        )
    )
    
    fig2.update_layout(
        title=f"DATE = {xListDate[n_intervals]}"
    )

    fig2.update_yaxes(range=[0, 100])    

    return fig, fig2

if __name__ == "__main__":
    app.run(debug=True)