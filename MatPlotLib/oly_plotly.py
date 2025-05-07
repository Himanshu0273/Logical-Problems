import plotly.express as px
import pandas as pd

# Create the data as a DataFrame
medals = {
    "Country": ["USA", "UK", "India", "China"],
    "Medals": [45, 27, 26, 19]
}

df = pd.DataFrame(medals)

# Create a bar plot
fig = px.bar(df, x="Country", y="Medals", title="Olympic Gold Tally")
fig.show()
