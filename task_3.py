from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("task_2.csv", header=0, parse_dates=[1], date_format="%Y-%m-%d")

df['sale'] = df['sale'].astype(float)
df['region'] = df['region'].astype(str)

processed_data = df.groupby('date').agg(
    daily_sales=('sale', 'sum')
)

fig = px.line(processed_data, y="daily_sales", title='Daily Sales over Time')

app = Dash()
app.layout = html.Div(children=[
    html.H1(children='Soul Foods'),

    html.Div(children='''
        Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
