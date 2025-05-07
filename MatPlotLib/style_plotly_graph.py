import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd


x = np.random.randint(1,101, size=100)
y = np.random.randint(1,101, size=100)

df = pd.DataFrame({'x':x, 'y': y})

fig=go.Figure()
fig.add_trace(go.Scatter(x=df['x'], y=df['y'], mode='markers', marker=dict(
    size=10,
    color=np.random.rand(500),
    colorscale='Viridis',
    opacity=0.7,
    line=dict(width=1, color="DarkSlateGreyx")
    ), name="Scatter Plot"))

fig.update_layout(
    title="Line and Scatter Graph together",
    xaxis_title="X Coordinates",
    yaxis_title="Y Coordinates",
    template="plotly_dark"
)
fig.show()