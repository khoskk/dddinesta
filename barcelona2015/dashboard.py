import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd


df = pd.read_csv('CarPrice_Assignment.csv')


avg_price = df['price'].mean()


df_body_price = df.groupby('carbody', as_index=False)['price'].mean()


app = dash.Dash(__name__)


fig_scatter = px.scatter(
    df, x='horsepower', y='price', color='fueltype',
    title='Зависимость цены от мощности двигателя',
    labels={'horsepower': 'Лошадиные силы', 'price': 'Цена ($)'},
    height=400
)


fig_bar = px.bar(
    df_body_price, x='carbody', y='price',
    title='Средняя цена по типу кузова',
    labels={'carbody': 'Тип кузова', 'price': 'Средняя цена ($)'},
    height=400
)


app.layout = html.Div(style={'font-family': 'Arial, sans-serif', 'padding': '20px'}, children=[
    html.H1("Анализ стоимости автомобилей", style={'text-align': 'center'}),
    
    
    html.Div(children=[
        html.H3("Средняя цена автомобиля:", style={'margin-bottom': '5px'}),
        html.H2(f"${avg_price:,.2f}", style={'color': '#2c3e50', 'margin-top': '0px'})
    ], style={'background-color': '#f0f2f6', 'padding': '20px', 'border-radius': '10px', 'text-align': 'center', 'margin-bottom': '20px'}),

    
    html.Div(style={'display': 'flex', 'flex-wrap': 'wrap'}, children=[
        
        html.Div(children=[
            dcc.Graph(figure=fig_scatter)
        ], style={'flex': '1', 'min-width': '400px', 'padding': '10px'}),
        
        
        html.Div(children=[
            dcc.Graph(figure=fig_bar)
        ], style={'flex': '1', 'min-width': '400px', 'padding': '10px'})
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
