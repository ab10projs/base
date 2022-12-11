import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

import plotly.express as px
import pandas as pd

# owner: Dustin Childers on Kaggle, source: https://data.brla.gov/Public-Safety/Animal-Control-Incidents/qmns-hw3s
df = pd.read_csv("BR_Animal_Control_Calls.csv" )

df1 = df.astype(object)
df1[df.isna()]= 'NA'
df = df1
print(df['CONDITION'].unique())



app = dash.Dash(__name__,
                meta_tags=[{'name': 'viewport',
                             'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
                )

app.layout = html.Div([
    html.Div([
        html.Div('Baton Rouge Animal Control and Rescue Center',
                 style={'textAlign':'center', 'fontSize':30}),

        html.Br(),
    ], className='row'),

    html.Div([

        html.Div([
            html.P("Animal Condition:", style={'fontSize':15}),
            dcc.Dropdown(id='drpdn1', value='FAIR',
                         options=[{'label': x, 'value': x} for x in sorted(df['CONDITION'].unique())]
                                  #for x in sorted(df.condition.unique())]

                         ),
            dcc.Graph(id='graph1'),
        ],className='six columns'),

        html.Div([
            html.P("Animal Characteristics:", style={'fontSize': 15}),
            dcc.Dropdown(id='drpdn2', value='SIZE',
                         options=[{'label': x, 'value': x}
                                  for x in df[['SIZE','CONDITION','TEMPERMENT','SEX']]],
                         ),
            dcc.Graph(id='graph2'),
        ],className='six columns')

    ], className='row'),

], className='ten columns offset-by-one')


@app.callback(
    Output(component_id='graph1', component_property='figure'),
    Input('drpdn1', 'value')
)
def update_graph1(chosen_condition):
    dff1 = df[df['CONDITION'] == chosen_condition][:100]
    fig1 = px.pie(dff1, names='SPECIES')
    return fig1


@app.callback(
    Output('graph2', 'figure'),
    Input('drpdn2', 'value')
)
def update_graph2(chosen_column):
    dff2 = df[chosen_column][:1000]
    fig2 = px.histogram(dff2, x=chosen_column)
    return fig2


if __name__ == '__main__':
    app.run_server(debug=True)
