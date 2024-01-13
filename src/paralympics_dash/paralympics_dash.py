# Version after the final activity in week 6
from dash import Dash, html
import dash_bootstrap_components as dbc

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap
# components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Pass the stylesheet variable to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Variables that define the three rows and their contents
card = dbc.Card(
    [
        dbc.CardImg(src=app.get_asset_url('logos/2022_Beijing.jpg'), top=True, style={
            "width": "200px",
            "align": "left"
        }),
        dbc.CardBody(
            [
                html.H4("TownName 2026", className="card-title"),
                html.P(
                    "Highlights of the paralympic event will go here. This will be a sentence or two.",
                    className="card-text",
                ),
                html.P(
                    "Number of athletes: XX",
                    className="card-text",
                ),
                html.P(
                    "Number of events: XX",
                    className="card-text",
                ),
                html.P(
                    "Number of countries: XX",
                    className="card-text",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

dropdown = dbc.Select(
    id="type-dropdown",  # id uniquely identifies the element, will be needed later
    options=[
        {"label": "Events", "value": "events"},
        # The value is in the format of the column heading in the data
        {"label": "Sports", "value": "sports"},
        {"label": "Countries", "value": "countries"},
        {"label": "Athletes", "value": "participants"},
    ],
    value="events"  # The default selection
)

checklist = dbc.Checklist(
    options=[
        {"label": "Summer", "value": "summer"},
        {"label": "Winter", "value": "winter"},
    ],
    value=["summer"],  # Values is a list as you can select both winter and summer
    id="checklist-input",
)

row_one = dbc.Row([
    dbc.Col([html.H1("Paralympics Dashboard"), html.P(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida. Fusce "
        "efficitur posuere metus posuere malesuada. ")
             ], width=12),
]),

row_two = dbc.Row([
    dbc.Col(children=[
        dropdown
    ], width=2),
    dbc.Col(children=[
        checklist,
    ], width={"size": 2, "offset": 4}),
], align="start")

row_three = dbc.Row([
    dbc.Col(children=[
        html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
    ], width=4),
    dbc.Col(children=[
        html.Img(src=app.get_asset_url('bar-chart-placeholder.png'), className="img-fluid"),
    ], width=4),
], align="start")

row_four = dbc.Row([
    dbc.Col(children=[
        html.Img(src=app.get_asset_url('map-placeholder.png'), className="img-fluid"),
    ], width=8),
    dbc.Col(children=[
        card,
    ], width=4),
], align="start")

# Add an HTML layout to the Dash app.
# The layout is wrapped in a DBC Container()
app.layout = dbc.Container([
    row_one,
    row_two,
    row_three,
    row_four
])

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)
    # Runs on port 8050 by default. If you have a port conflict, add the parameter port=   e.g. port=8051
