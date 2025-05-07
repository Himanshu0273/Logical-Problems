import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd


x = np.random.randint(1,101, size=100)
y = np.random.randint(1,101, size=100)

df = pd.DataFrame({'x':x, 'y': y})

fig=go.Figure()
fig.add_trace(go.Scatter(x=df['x'], y=df['y'], mode='lines', name="Line Plot"))
fig.add_trace(go.Scatter(x=df['x'], y=df['y'], mode='markers', name="Scatter Plot"))

fig.update_layout(
    title="Line and Scatter Graph together",
    xaxis_title="X Coordinates",
    yaxis_title="Y Coordinates"
)
fig.show()