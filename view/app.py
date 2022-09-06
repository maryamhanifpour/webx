
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

path = ['/tmp/elastic.txt', '/tmp/github.txt', '/tmp/api.txt']

def read_file(p):
    with open(p, 'r') as f:
        lines = f.read().split('\n')
    lines = [eval(l) for l in  lines if len(l) > 0]
    dfItem = pd.DataFrame.from_records(lines)
    dfItem['time'] = pd.to_datetime(dfItem.checkTime)
    dfItem['label'] = p
    return(dfItem[['label', 'time', 'responseTimeMilSec']])

def concatDf(path):
    df2 = pd.DataFrame()
    for p in path:
        df = read_file(p)
        df2 = pd.concat([df,df2])
    return df2


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4('responseTimeMilSec'),
    dcc.Graph(id="time-series-chart1"),
    dcc.Dropdown(
        id="ticker",
        value="responseTimeMilSec",

        clearable=True,
    ),
])

@app.callback(
    Output("time-series-chart1", "figure"), 
    Input("ticker", "value"))
def display_time_series(ticker):
    df = concatDf(path) # replace with your own data source
    fig = px.line(df, x='time', y=ticker, color='label')
    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)