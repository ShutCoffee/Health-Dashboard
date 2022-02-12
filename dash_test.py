import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import strong_evaluation

app = dash.Dash()

fig = px.scatter(
    strong_evaluation.df,
    x="GDP",
    y="Life expectancy",
    size="Population",
    color="continent",
    hover_name="Country",
    log_x=True,
    size_max=60,
)

app.layout = html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig)])


if __name__ == "__main__":
    app.run_server(debug=True)