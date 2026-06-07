'''
 This script is used for simulate live data streaming in real time.
'''
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

# ### ---- Data Preparation Starts Here ----

# path = "C:\\Anupam\\GIT\\base\\cursorFolder\\tools\\BhavData\\BhavData\\"

# allFiles = [file for file in os.listdir(path) if file.endswith('.xlsx')]

# dfMerged = pl.DataFrame()
# for file in allFiles:
#     df = pl.read_excel(f"{path}{file}").with_columns(pl.all().cast(pl.String))
#     dfMerged = dfMerged.vstack(df)


# dfMerged.columns = pl.Series(dfMerged.columns).str.strip_chars()
# dfMerged = dfMerged.with_columns(pl.col("DATE1").str.strptime(pl.Date,format="%d-%b-%Y").alias("DATE1"))
# columns = dfMerged.columns

# for i in range(3, len(columns)-2):
#     dfMerged = dfMerged.with_columns(pl.col(columns[i]).cast(pl.Float64, strict=False).fill_null(0))  

# print(dfMerged.schema)  
# print(dfMerged.head())
# print(dfMerged.shape)

# dfMerged.write_csv("C://Anupam//GIT//base//cursorFolder//tools//BhavData//dfMerged.csv")
# ### ---- Data Preparation Ends Here ----


# #----- Dash App Starts Here -----

df = pl.read_csv("C://Anupam//GIT//base//cursorFolder//tools//BhavData//dfMerged.csv")

datelist = df.select(pl.col("DATE1")).unique()

datelist = pl.Series(datelist).sort()

xListDate = []
xListSymbol = []
yList = []


for i in range(len(datelist)-1):
    
    xListDate.append(datelist[i])
    xListSymbol.append(df.filter(pl.col("DATE1") == datelist[i])['SYMBOL'])
    yList.append(df.filter(pl.col("DATE1") == datelist[i])['CLOSE_PRICE'])


# print(xListSymbol)
# print(yList)


# #---------------------

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)


BG_WHITE = "#ffffff"
TEXT_BLACK = "#000000"
GRID_GREY = "#e6e6e6"


app.layout = html.Div([
    dcc.Graph(id="scatter-chart"),
    # Fires every second
    dcc.Interval(
        id="interval-component",
        interval=350,  # milliseconds
        n_intervals=0
    )
])


@app.callback(
    Output("scatter-chart", "figure"),
    Input("interval-component", "n_intervals")
)



def update_chart(n_intervals):
    print(n_intervals)
    if n_intervals % len(xListDate) == 0:
        counter = 0
    else:
        counter = n_intervals % len(xListDate)
 

    filtered = df.filter(
        pl.col("DATE1") == xListDate[counter]
    )

    fig1 = go.Figure(
        go.Scatter(
            x=filtered["SYMBOL"].to_list()[:5000],
            y=filtered["CLOSE_PRICE"].to_list(), mode='markers', 
                        marker=dict(size=2,
                        color= filtered["CLOSE_PRICE"],
                        colorscale="Viridis",  
                        opacity=0.6, 
                        line=dict(width=0.8)  
                        )
        )
    ).update_yaxes(range=[0, 500]
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

    fig1.update_layout(
    width=600,   # chart width in pixels
    height=400   # chart height in pixels
)

    return fig1

if __name__ == "__main__":
    app.run(debug=True)



