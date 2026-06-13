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


app.layout = dbc.Container(
    fluid=True,
    className="p-3",
    children=[

        dbc.Tabs(
            [
                # Tab 1
                dbc.Tab(
                    label="Dashboard",
                    children=[

                        dbc.Row(
                            dbc.Col(
                                html.H2(
                                    "Live Data Streaming",
                                    className="text-center mb-4"
                                )
                            )
                        ),

                        dbc.Row(
                            [
                                # Left Scatter Plot
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            dcc.Graph(
                                                id="scatter-chart",
                                                style={"height": "250px"}
                                            )
                                        )
                                    ),
                                    width=4,
                                ),

                                # Middle Column
                                dbc.Col(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                dcc.Graph(
                                                    id="line-chart-1",
                                                    style={"height": "100px"}
                                                )
                                            ),
                                            className="mb-3",
                                        ),

                                        dbc.Card(
                                            dbc.CardBody(
                                                dcc.Graph(
                                                    id="line-chart-2",
                                                    style={"height": "100px"}
                                                )
                                            )
                                        ),
                                    ],
                                    width=4,
                                ),

                                # Right Column
                                dbc.Col(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                dcc.Graph(
                                                    id="line-chart-3",
                                                    style={"height": "100px"}
                                                )
                                            ),
                                            className="mb-3",
                                        ),

                                        dbc.Card(
                                            dbc.CardBody(
                                                dcc.Graph(
                                                    id="line-chart-4",
                                                    style={"height": "100px"}
                                                )
                                            )
                                        ),
                                    ],
                                    width=4,
                                ),
                            ],
                            className="g-3",
                        ),
                    ],
                ),

                # Tab 2
                dbc.Tab(
                    label="Tab 2",
                    children=[
                        html.Div("Coming Soon...", className="p-4")
                    ],
                ),

                # Tab 3
                dbc.Tab(
                    label="Tab 3",
                    children=[
                        html.Div("Coming Soon...", className="p-4")
                    ],
                ),
            ]
        ),

        dcc.Interval(
            id="interval-component",
            interval=500,
            n_intervals=0,
        ),
    ],
)



@app.callback(
    Output("scatter-chart", "figure"),
    Output("line-chart-1", "figure"),
    Output("line-chart-2", "figure"),
    Output("line-chart-3", "figure"),
    Output("line-chart-4", "figure"),
    Input("interval-component", "n_intervals")
)



def update_chart(n_intervals):
    print(n_intervals)
    if n_intervals % len(xListDate) == 0:
        counter = 0
    else:
        counter = n_intervals % len(xListDate)
 
    #--- this filtered dataframe is common to all the plots starting from here----
    filtered = df.filter(
        pl.col("DATE1") == xListDate[counter]
    )
    #--- this filtered dataframe is common to all the plots ending here----

    #--- Fig1 is for scatter plot live simulation---- start
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
    margin=dict(l=20, r=20, t=30, b=20),
    template="plotly_white",
)
#--- Fig1 is for scatter plot live simulation---- end

#--- Fig2 is for line plot of a particular symbol---- start
    filteredScrip1 = df.filter([(pl.col("SYMBOL") == "ICICIBANK") & (pl.col("DATE1") <= xListDate[counter])])
    fig2 = go.Figure(
        go.Scatter(
            x=filteredScrip1["DATE1"].to_list(),
            y=filteredScrip1["CLOSE_PRICE"].to_list(),
            mode='markers',
            marker=dict(size=3,
                        color= filteredScrip1["CLOSE_PRICE"],
                        colorscale="Viridis",  
                        opacity=0.9, 
                        line=dict(width=0.8)  
                        ),
        )
    )
    fig2.update_layout(
    margin=dict(l=20, r=20, t=30, b=20),
    template="plotly_white",
)
#--- Fig2 is for line plot of a particular symbol---- end 
#--- Fig3 is for line plot of a particular symbol---- start
    filteredScrip3 = df.filter([(pl.col("SYMBOL") == "RELIANCE") & (pl.col("DATE1") <= xListDate[counter])])
    fig3 = go.Figure(
        go.Scatter(
            x=filteredScrip3["DATE1"].to_list(),
            y=filteredScrip3["CLOSE_PRICE"].to_list(),
            mode='markers',
            marker=dict(size=3,
                        color= filteredScrip3["CLOSE_PRICE"],
                        colorscale="Viridis",  
                        opacity=0.9, 
                        line=dict(width=0.8)  
                        ),
        )
    )
    fig3.update_layout(
    margin=dict(l=20, r=20, t=30, b=20),
    template="plotly_white",
)
#--- Fig3 is for line plot of a particular symbol---- start
#--- Fig4 is for line plot of a particular symbol---- start
    filteredScrip4 = df.filter([(pl.col("SYMBOL") == "BHEL") & (pl.col("DATE1") <= xListDate[counter])])
    fig4 = go.Figure(
        go.Scatter(
            x=filteredScrip4["DATE1"].to_list(),
            y=filteredScrip4["CLOSE_PRICE"].to_list(),
            mode='markers',
            marker=dict(size=3,
                        color= filteredScrip4["CLOSE_PRICE"],
                        colorscale="Viridis",  
                        opacity=0.9, 
                        line=dict(width=0.8)  
                        ),
        )
    )
    fig4.update_layout(
    margin=dict(l=20, r=20, t=30, b=20),
    template="plotly_white",
)
#--- Fig4 is for line plot of a particular symbol---- end



#--- Fig5 is for line plot of a particular symbol---- start
    filteredScrip5 = df.filter([(pl.col("SYMBOL") == "HAL") & (pl.col("DATE1") <= xListDate[counter])])
    fig5 = go.Figure(
        go.Scatter(
            x=filteredScrip5["DATE1"].to_list(),
            y=filteredScrip5["CLOSE_PRICE"].to_list(),
            mode='markers',
            marker=dict(size=3,
                        color= filteredScrip5["CLOSE_PRICE"],
                        colorscale="Viridis",  
                        opacity=0.9, 
                        line=dict(width=0.8)  
                        ),
        )
    )
    fig5.update_layout(
    margin=dict(l=20, r=20, t=30, b=20),
    template="plotly_white",
)
#--- Fig5 is for line plot of a particular symbol---- end

    return fig1, fig2 , fig3  ,fig4, fig5

if __name__ == "__main__":
    app.run(debug=True)



