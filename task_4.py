from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

df = pd.read_csv("task_2.csv", header=0, parse_dates=[1], date_format="%Y-%m-%d")

df['sale'] = df['sale'].astype(float)
df['region'] = df['region'].astype(str)

processed_data = df.groupby('date').agg(
    daily_sales=('sale', 'sum')
)
colors = {
    'background': '#343830',
    'north': '#5097B7',
    'south': '#7EB851',
    'east': '#B88951',
    'west': '#B051B8',
    'all': '#4C5C63',
    'text': '#FFFFFF'
}

fig = px.line(processed_data, y="daily_sales", color_discrete_sequence=[colors['all']], title='Daily Sales over Time')
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app = Dash()
app.layout = html.Div(children=[
    html.Div(children=[
        html.H1(id="header", style={'color': colors['text'], 'fontSize':'48px', 'paddingTop': '16px', 'margin':'0px'}, children='Soul Foods'),
        html.Div(style={'color': colors['text']}, children='''
        Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?
    '''),
        dcc.RadioItems(
            id="selection",
            options=["north", "south", "east", "west", "all"],
            value="all",
            labelStyle={
                'color': colors['text']
            },
            inline=True)
    ],
        style={
            'paddingLeft': '5%'
        }),
    dcc.Graph(
        id='graph',
        figure=fig
    )
], id="body",
    style={
        'backgroundColor': colors['background'],
        'height': '100vh'
    })


@callback(
    Output('graph', 'figure'),
    Input("selection", 'value')
)
def select_data(region):
    if "all" == region:
        processed = df.groupby('date').agg(
            daily_sales=('sale', 'sum')
        )
    else:
        filtered_data = df[df['region'] == region]
        processed = filtered_data.groupby('date').agg(
            daily_sales=('sale', 'sum')
        )

    result = px.line(processed, y="daily_sales", color_discrete_sequence=[colors[region]],
                     title='Daily Sales over Time')
    result.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    return result


if __name__ == '__main__':
    app.run(debug=True)
