import plotly.express as px
import numpy as np
import pandas as pd


x = np.random.randint(0,101, size=1000)
y = np.random.randint(0,101, size=1000)
df = pd.DataFrame({'x':x, 'y': y})

fig = px.scatter(df, x=x, y=y, title="Scatter Plot")
fig.show()