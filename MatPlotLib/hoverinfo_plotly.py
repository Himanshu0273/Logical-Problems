import plotly.graph_objects as go
import pandas as pd

url = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'
df = pd.read_csv(url)
fig = go.Figure(data=go.Scatter(
    x=df['Rank'], 
    y=df['Population'],
    mode='markers',
    text=df.apply(lambda row: f"State: {row['State']}<br>Population: {row['Population']}", axis=1), 
    hoverinfo='text',  
    marker=dict(
        size=10, 
        color='blue',  
        opacity=0.7, 
        line=dict(width=1, color='DarkSlateGrey') 
    )
))

fig.update_layout(
    title="State Population by Rank",
    xaxis_title="Rank",
    yaxis_title="Population"
)

fig.show()
