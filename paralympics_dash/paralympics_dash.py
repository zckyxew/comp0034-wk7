from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World')
])

if __name__ == '__main__':
    app.run(debug=True)
    # Runs on port 8050 by default. If you have a port conflict, add the parameter port=   e.g. port=8051
