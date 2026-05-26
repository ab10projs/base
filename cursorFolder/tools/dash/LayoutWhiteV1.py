

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
from datetime import date

# --------------------------------
# App
# --------------------------------
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

# --------------------------------
# Sample Data
# --------------------------------
df = pd.DataFrame({
    "category": ["A", "B", "C", "D"],
    "value": [30, 20, 25, 25]
})

BG_WHITE = "#ffffff"
TEXT_BLACK = "#000000"
GRID_GREY = "#e6e6e6"

# --------------------------------
# Figures (WHITE BACKGROUND)
# --------------------------------
def bar_fig():
    fig = go.Figure(
        go.Bar(
            x=df["category"],
            y=df["value"]
        )
    )
    fig.update_layout(
        paper_bgcolor=BG_WHITE,
        plot_bgcolor=BG_WHITE,
        font=dict(color=TEXT_BLACK),
        title=dict(text="Production by Category", font=dict(color=TEXT_BLACK)),
        margin=dict(l=10, r=10, t=40, b=10),
        height=240,
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor=GRID_GREY)
    )
    return fig


def pie_fig():
    fig = go.Figure(
        go.Pie(
            labels=df["category"],
            values=df["value"],
            hole=0.5,
            textfont=dict(color=TEXT_BLACK)
        )
    )
    fig.update_layout(
        paper_bgcolor=BG_WHITE,
        font=dict(color=TEXT_BLACK),
        title=dict(text="Category Share", font=dict(color=TEXT_BLACK)),
        margin=dict(l=10, r=10, t=40, b=10),
        height=240
    )
    return fig


# --------------------------------
# Layout
# --------------------------------
app.layout = dbc.Container(
    fluid=True,
    style={"backgroundColor": BG_WHITE},
    className="p-2",
    children=[

        # ================= HEADER =================
        dbc.Row(
            dbc.Col(
                html.H5(
                    "Manufacturing Analytics Dashboard",
                    className="text-center",
                    style={"color": TEXT_BLACK}
                )
            ),
            className="g-2 mb-2"
        ),

        # ================= FILTERS =================
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        options=[{"label": i, "value": i} for i in df["category"]],
                        value=["A", "B"],
                        multi=True,
                        placeholder="Select Category",
                        style={
                            "backgroundColor": BG_WHITE,
                            "color": TEXT_BLACK
                        }
                    ),
                    md=4
                ),
                dbc.Col(
                    dcc.DatePickerRange(
                        start_date=date(2024, 1, 1),
                        end_date=date.today(),
                        display_format="YYYY-MM-DD"
                    ),
                    md=4
                ),
            ],
            className="g-2 mb-2"
        ),

        # ================= KPI CARDS =================
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H6("Total Output", style={"color": TEXT_BLACK}),
                            html.H4("1,245", style={"color": TEXT_BLACK})
                        ]),
                        className="shadow-sm",
                        style={"backgroundColor": BG_WHITE}
                    ),
                    md=3
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H6("Defects", style={"color": TEXT_BLACK}),
                            html.H4("32", style={"color": TEXT_BLACK})
                        ]),
                        className="shadow-sm",
                        style={"backgroundColor": BG_WHITE}
                    ),
                    md=3
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H6("Efficiency", style={"color": TEXT_BLACK}),
                            html.H4("96%", style={"color": TEXT_BLACK})
                        ]),
                        className="shadow-sm",
                        style={"backgroundColor": BG_WHITE}
                    ),
                    md=3
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H6("Downtime", style={"color": TEXT_BLACK}),
                            html.H4("1.8 hrs", style={"color": TEXT_BLACK})
                        ]),
                        className="shadow-sm",
                        style={"backgroundColor": BG_WHITE}
                    ),
                    md=3
                ),
            ],
            className="g-2 mb-2"
        ),

        # ================= CHARTS =================
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dcc.Graph(
                            figure=bar_fig(),
                            config={"displayModeBar": False}
                        ),
                        className="shadow-sm",
                        style={"backgroundColor": BG_WHITE}
                    ),
                    md=6
                ),
                dbc.Col(
                    dbc.Card(
                        dcc.Graph(
                            figure=pie_fig(),
                            config={"displayModeBar": False}
                        ),
                        className="shadow-sm",
                        style={"backgroundColor": BG_WHITE}
                    ),
                    md=6
                ),
            ],
            className="g-2"
        ),
    ]
)

# --------------------------------
# Run
# --------------------------------
if __name__ == "__main__":
    app.run(debug=True)