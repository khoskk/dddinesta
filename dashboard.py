# import dash
# from dash import dcc, html
# import plotly.express as px
# import pandas as pd


# df = pd.read_csv('CarPrice_Assignment.csv')


# avg_price = df['price'].mean()


# df_body_price = df.groupby('carbody', as_index=False)['price'].mean()


# app = dash.Dash(__name__)


# fig_scatter = px.scatter(
#     df, x='horsepower', y='price', color='fueltype',
#     title='Зависимость цены от мощности двигателя',
#     labels={'horsepower': 'Лошадиные силы', 'price': 'Цена ($)'},
#     height=400
# )


# fig_bar = px.bar(
#     df_body_price, x='carbody', y='price',
#     title='Средняя цена по типу кузова',
#     labels={'carbody': 'Тип кузова', 'price': 'Средняя цена ($)'},
#     height=400
# )


# app.layout = html.Div(style={'font-family': 'Arial, sans-serif', 'padding': '20px'}, children=[
#     html.H1("Анализ стоимости автомобилей", style={'text-align': 'center'}),
    
    
#     html.Div(children=[
#         html.H3("Средняя цена автомобиля:", style={'margin-bottom': '5px'}),
#         html.H2(f"${avg_price:,.2f}", style={'color': '#2c3e50', 'margin-top': '0px'})
#     ], style={'background-color': '#f0f2f6', 'padding': '20px', 'border-radius': '10px', 'text-align': 'center', 'margin-bottom': '20px'}),

    
#     html.Div(style={'display': 'flex', 'flex-wrap': 'wrap'}, children=[
        
#         html.Div(children=[
#             dcc.Graph(figure=fig_scatter)
#         ], style={'flex': '1', 'min-width': '400px', 'padding': '10px'}),
        
        
#         html.Div(children=[
#             dcc.Graph(figure=fig_bar)
#         ], style={'flex': '1', 'min-width': '400px', 'padding': '10px'})
#     ])
# ])

# if __name__ == '__main__':
#     app.run(debug=True)

import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('CarPrice_Assignment.csv')


avg_price = df['price'].mean()
df_body_price = df.groupby('carbody', as_index=False)['price'].mean().sort_values('price', ascending=False)
df_fuel_price = df.groupby('fueltype', as_index=False)['price'].mean()


app = dash.Dash(__name__)


fig_scatter = px.scatter(
    df, x='horsepower', y='price', color='carbody',
    title='Зависимость цены от мощности двигателя по типам кузова',
    labels={'horsepower': 'Лошадиные силы', 'price': 'Цена ($)', 'carbody': 'Тип кузова'},
    height=420,
    opacity=0.7
)
fig_scatter.update_layout(font=dict(size=11))


fig_bar_body = px.bar(
    df_body_price, x='carbody', y='price',
    title='Средняя цена по типу кузова',
    labels={'carbody': 'Тип кузова', 'price': 'Средняя цена ($)'},
    height=420,
    color='price',
    color_continuous_scale='Viridis'
)
fig_bar_body.update_layout(font=dict(size=11))


df_body_fuel = df.groupby(['carbody', 'fueltype'], as_index=False)['price'].mean()

fig_bar_fuel = px.bar(
    df_body_fuel,
    x='carbody',
    y='price',
    color='fueltype',
    barmode='group',
    title='Средняя цена по типу кузова и типу топлива',
    labels={
        'carbody': 'Тип кузова',
        'price': 'Средняя цена ($)',
        'fueltype': 'Тип топлива'
    },
    height=420,
    color_discrete_map={'gas': '#FF6B6B', 'diesel': '#4ECDC4'}
)
fig_bar_fuel.update_layout(
    font=dict(size=11),
    legend_title_text='Топливо',
    xaxis_title='Тип кузова',
    yaxis_title='Средняя цена ($)'
)



app.layout = html.Div(style={'font-family': 'Segoe UI, Arial, sans-serif', 'padding': '30px', 'background-color': '#f5f7fa'}, children=[
    
    
    html.Div(style={'background-color': '#2c3e50', 'color': 'white', 'padding': '30px', 'border-radius': '10px', 'margin-bottom': '30px'}, children=[
        html.H1(" Анализ рынка автомобилей", style={'margin': '0 0 15px 0', 'font-size': '32px'}),
        
    
        
        html.P([
            "Этот дашборд раскрывает ",
            html.B("ключевые факторы, влияющие на стоимость автомобилей"),
            ". Анализируя данные из 205 автомобилей, мы видим, что цена зависит от нескольких параметров: "
        ], style={'font-size': '15px', 'line-height': '1.6', 'color': '#ecf0f1', 'margin': '0'}),
        
        html.Ul(style={'font-size': '15px', 'line-height': '1.8', 'margin': '10px 0 0 20px', 'color': '#ecf0f1'}, children=[
            html.Li(" Мощность двигателя (horsepower) — одна из основных детерминант цены. Более мощные автомобили стоят значительно дороже."),
            html.Li(" Тип кузова влияет на стоимость: некоторые кузова (например, convertible) традиционно дороже других (например, hatchback)."),
            html.Li(" Тип топлива также важен: дизельные автомобили дороже на 22% в среднем, чем работающие на газе."),
        ]),
        
        
    ]),
    
    
    html.Div(style={'display': 'flex', 'justify-content': 'space-around', 'margin-bottom': '30px', 'flex-wrap': 'wrap'}, children=[
        
        
        html.Div(children=[
            html.Div(style={'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', 'padding': '25px', 'border-radius': '10px', 'text-align': 'center', 'color': 'white', 'min-width': '220px', 'box-shadow': '0 4px 6px rgba(0,0,0,0.1)'}, children=[
                html.P("Средняя цена", style={'font-size': '14px', 'margin': '0 0 10px 0', 'opacity': '0.9'}),
                html.H2(f"${avg_price:,.0f}", style={'margin': '0', 'font-size': '28px'})
            ])
        ], style={'flex': '1', 'padding': '10px'}),
        
        
        html.Div(children=[
            html.Div(style={'background': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)', 'padding': '25px', 'border-radius': '10px', 'text-align': 'center', 'color': 'white', 'min-width': '220px', 'box-shadow': '0 4px 6px rgba(0,0,0,0.1)'}, children=[
                html.P("Всего автомобилей", style={'font-size': '14px', 'margin': '0 0 10px 0', 'opacity': '0.9'}),
                html.H2(f"{len(df)}", style={'margin': '0', 'font-size': '28px'})
            ])
        ], style={'flex': '1', 'padding': '10px'}),
        
        
        html.Div(children=[
            html.Div(style={'background': 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)', 'padding': '25px', 'border-radius': '10px', 'text-align': 'center', 'color': 'white', 'min-width': '220px', 'box-shadow': '0 4px 6px rgba(0,0,0,0.1)'}, children=[
                html.P("Средняя мощность", style={'font-size': '14px', 'margin': '0 0 10px 0', 'opacity': '0.9'}),
                html.H2(f"{df['horsepower'].mean():.0f} л.с.", style={'margin': '0', 'font-size': '28px'})
            ])
        ], style={'flex': '1', 'padding': '10px'}),
    ]),
    
    
    html.Div(style={'display': 'grid', 'grid-template-columns': 'repeat(auto-fit, minmax(500px, 1fr))', 'gap': '20px'}, children=[
        
        
        html.Div(children=[
            dcc.Graph(figure=fig_scatter)
        ], style={'background-color': 'white', 'border-radius': '10px', 'box-shadow': '0 2px 4px rgba(0,0,0,0.1)', 'padding': '10px'}),
        
        
        html.Div(children=[
            dcc.Graph(figure=fig_bar_body)
        ], style={'background-color': 'white', 'border-radius': '10px', 'box-shadow': '0 2px 4px rgba(0,0,0,0.1)', 'padding': '10px'}),
        
        
        html.Div(children=[
            dcc.Graph(figure=fig_bar_fuel)
        ], style={'background-color': 'white', 'border-radius': '10px', 'box-shadow': '0 2px 4px rgba(0,0,0,0.1)', 'padding': '10px'}),
    ]),
    
    
    html.Hr(style={'margin-top': '30px', 'border': 'none', 'border-top': '1px solid #ddd'}),
    html.P("Дашборд создан на основе датасета CarPrice_Assignment. Данные включают 205 автомобилей с характеристиками цены, мощности и типов кузова.",
           style={'text-align': 'center', 'color': '#7f8c8d', 'font-size': '13px', 'margin-top': '20px'}),
    
    # Мы
    html.Div(style={'text-align': 'center', 'margin-top': '30px', 'margin-bottom': '20px'}, children=[
        html.H3("Created by ", 
                style={'color': '#2c3e50', 'font-family': 'Courier New, monospace'}),
        html.P("Melikhov • Elhennauy • Ahmedov", 
               style={'color': '#e74c3c', 'font-size': '20px', 'font-weight': 'bold', 
                      'letter-spacing': '2px', 'text-shadow': '2px 2px 4px rgba(0,0,0,0.1)'})
    ])
])

if __name__ == '__main__':
    app.run(debug=True)

