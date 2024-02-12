# 1. Line chart

| Activity                           | Chart type | Data access method | Chart library  |
|:-----------------------------------|:-----------|:-------------------|:---------------|
| [Activity 1](dash-1-line-chart.md) | Line chart | pandas / .csv      | Plotly Express |

## Create the chart

Add a line chart that displays for each paralympics the total number of events, competitors and
sports. The data will be displayed over time, i.e. from 1960 through to 2022.

The data is in `data/paralympic_events.csv`. The columns needed
are: `["type", "year", "host", "events", "sports", "participants", "countries"]`.

The code to create the chart is written as a function in a new module, `figures.py`. You do not have to put the
code in a function, however it
makes the code easier to change when you add callbacks next week. Adding the code to `figures.py` both keeps the code to
generate the charts in one place and also stops the main app module getting too long to read and edit.

The function to create the line chart will take a parameter that accepts whether the chart should display events, sports
or participants.

The following code is commented to explain what it does:

```python
from pathlib import Path

import pandas as pd
import plotly.express as px

event_data = Path(__file__).parent.parent.joinpath("data", "paralympic_events.csv")


def line_chart(feature):
    """ Creates a line chart with data from paralympics_events.csv

    Data is displayed over time from 1960 onwards.
    The figure shows separate trends for the winter and summer events.

     Parameters
     feature: events, sports or participants

     Returns
     fig: Plotly Express line figure
     """

    # take the feature parameter from the function and check it is valid
    if feature not in ["sports", "participants", "events", "countries"]:
        raise ValueError(
            'Invalid value for "feature". Must be one of ["sports", "participants", "events", "countries"]')
    else:
        # Make sure it is lowercase to match the dataframe column names
        feature = feature.lower()

    # Read the data from pandas into a dataframe
    cols = ["type", "year", "host", "events", "sports", "participants", "countries"]
    line_chart_data = pd.read_csv(event_data, usecols=cols)

    # Create a Plotly Express line chart with the following parameters
    #  line_chart_data is the DataFrane
    #  x="year" is the column to use as a x-axis
    #  y=feature is the column to use as the y-axis
    # color="type" indicates if winter or summer
    fig = px.line(line_chart_data, x="year", y=feature, color="type")
    return fig
```

then in paralympics_dash.py before the layout add:

```python
# Add an import to import the line_chart function
from figures import line_chart

# Create the Plotly Express line chart object, e.g. to show number of sports
line = line_chart("sports")
```

In row_three, replace the placeholder image with a dash core components chart object, dcc.Chart(). The parameters are

- `id="line"` sets the HTML id to "line". The id can be anything you want, it just has to be unique within the HTML
  page.
- `figure=line` is the 'line' chart figure variable you just created in the code above.

```python
# Add dcc import to imports section
from dash import Dash, html, dcc

# Modify row_three
row_three = dbc.Row([
    dbc.Col(children=[
        # Add this line:
        dcc.Graph(id="line", figure=line),
        # Delete this line:
        html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),

# code continues... 
```

If the app is running and your code did not fail, then it should now display the chart you created. If the app is not
running, then run it.

### Style the line chart

A Plotly Go figure has three top level attributes: data, layout and frames. The layout contains attributes such as
titles, legend, margins, size, fonts, colors. There are many attributes to a figure and far more than can be covered in
this course. You may need to search the documentation for a particular effect you wish to achieve.

The [documentation for styling Express](https://plotly.com/python/styling-plotly-express/) can be used for this
activity.

For this activity:

- set the title to "How has the number of {feature} changed over time?"
- change the legend to remove the word 'type' from the legend and 'feature' from the Y axis and change the X axis label
  to start with a capital letter
- use a template to apply a more simple style that has no background

Edit the code in `figures.py`:

```python
# Set the title for the chart using the value of 'feature'
title_text = f"How has the number of {feature} changed over time?"

'''
Create a Plotly Express line chart with the following parameters
  line_chart_data is the DataFrane
  x="year" is the column to use as a x-axis
  y=feature is the column to use as the y-axis
  color="type" indicates if winter or summer
  title=title_text sets the title using the variable title_text
  labels={} sets the X label to Year, sets the Y axis and the legend to nothing (an empty string)
  template="simple_white" uses a Plotly theme to style the chart
'''
fig = px.line(line_chart_data,
              x="year",
              y=feature,
              color="type",
              title=title_text,
              labels={'year': 'Year', feature: '', 'type': ''},
              template="simple_white"
              )
```

Check the app is running, it should now display the line chart with the revised styling.

## 2. Bar chart

### Create the chart using pandas and Plotly Express

Create a stacked bar chart that shows the ratio of female:male competitors for either winter or summer events.

This requires further manipulation of the DataFrame before the chart can be created. See the comments in the code below.

Add the code to `figures.py`:

```python
def bar_gender(event_type):
    """
    Creates a stacked bar chart showing change in the number of sports in the summer and winter paralympics
    over time
    An example for exercise 2.

    :param event_type: str Winter or Summer
    :return: Plotly Express bar chart
    """
    cols = ['type', 'year', 'host', 'participants_m', 'participants_f', 'participants']
    df_events = pd.read_csv(event_data, usecols=cols)
    # Drop Rome as there is no male/female data
    df_events.drop([0], inplace=True, )
    df_events.reset_index(drop=True)
    # Add new columns that each contain the result of calculating the % of male and female participants
    df_events['M%'] = df_events['participants_m'] / df_events['participants']
    df_events['F%'] = df_events['participants_f'] / df_events['participants']
    # Sort the values by Type and Year
    df_events.sort_values(['type', 'year'], ascending=(True, True), inplace=True)
    # Create a new column that combines Location and Year to use as the x-axis
    df_events['xlabel'] = df_events['host'] + ' ' + df_events['year'].astype(str)
    # Create the stacked bar plot of the % for male and female
    df_events = df_events.loc[df_events['type'] == event_type]
    fig = px.bar(df_events,
                 x='xlabel',
                 y=['M%', 'F%'],
                 title='How has the ratio of female:male participants changed?',
                 labels={'xlabel': '', 'value': '', 'variable': ''},
                 color_discrete_map={'M%': 'blue', 'F%': 'green'},
                 template="simple_white"
                 )
    fig.update_xaxes(ticklen=0)
    return fig
```

### Add styling

Have a look at styling options and try and change some of
the [styling options](https://plotly.com/python/styling-plotly-express/) of the bar chart e.g. add a title, change the
colour of the bars.

## 3. Scatter Mapbox

You need to have the latitude and longitude of each event. These have been added to the SQLite database in a locations
table.

In week 2 we looked at creating a database using SQLite. One method is to use the sqlite3 library to create a database
connection and create a cursor to execute queries. The following code uses pandas to read from a SQLite database.

```python
paralympic_db = Path(__file__).parent.joinpath("paralympics.sqlite")


def scatter_geo():
    # create database connection
    connection = sqlite3.connect(paralympic_db)

    # define the sql query
    sql = '''
        SELECT event.id, event.host, event.year, location.lat, location.lon
        FROM event
        JOIN location ON event.host = location.city 
        '''

    df_locs = pd.read_sql(sql=sql, con=connection, index_col=None)
    # The lat and lon are stored as string but need to be floats for the scatter_geo
    df_locs['lon'] = df_locs['lon'].astype(float)
    df_locs['lat'] = df_locs['lat'].astype(float)
    # Adds a new column that concatenates the city and year e.g. Barcelona 2012
    df_locs['name'] = df_locs['host'] + ' ' + df_locs['year'].astype(str)

    fig = px.scatter_geo(df_locs,
                         lat=df_locs.lat,
                         lon=df_locs.lon,
                         hover_name=df_locs.name,
                         title="Where have the paralympics been held?",
                         )
    return fig 
```

In paralympics_dash.py add code to create the figure using the function above, e.g.

```python
from figures import scatter_geo

# Create the scatter map
map = scatter_geo()
```

In the layout for row 3 add the dcc.Graph() and remove the placeholder image, e.g.

```python
row_four = dbc.Row([
    dbc.Col(children=[
        dcc.Graph(id="map", figure=map)
        # html.Img(src=app.get_asset_url('map-placeholder.png'), className="img-fluid"),
    ], width=8),
    dbc.Col(children=[
        card,
    ], width=4),
], align="start")
```

Run the app if not already running. You should see a map of the world with small dots for each event. When you hover on
a dot it will show the city and year.

There are options for styling the markers, though this requires some Plotly Go syntax. Refer to the [Plotly maps
documentation](https://plotly.com/python/scatter-plots-on-maps/) if you want to try to change the marker styles.

## 4. Card

The last example isn't a figure. This is a Bootstrap card using
the [dash-bootstrap-components card](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/).

It will display the details for a selected event. Next week you will add a callback that changes the event card based on
clicks on the map markers.

For this example, we will use the REST API route /events/<event_id>. You need to make sure that the REST API app is
running on your computer, to run it: `flask --app paralympics_rest run --debug`

To get data from an API you can use the Python requests library (part of the Python base library, you don't need to
install it separately).

The code to generate the card is moved into a function.

- The function takes an event id.
- It uses requests to make a request to the `http://127.0.0.1:5000/events/<event_id>` route using the event id passed to
  the function to generate the url string.
- The response from the request contains json.
- Variables to created with values from the json object.
- The card html is generated with the variables

```python
def create_card(event_id):
    """
    Generate a card for the event specified by event_id.

    Uses the REST API route.

    Args:
        event_id:

    Returns:
        card: dash boostrap components card for the event
    """
    # Use python requests to access your REST API on your localhost
    # Make sure you run the REST APP first and check your port number if you changed it from the default 5000
    url = f"http://127.0.0.1:5000/events/{event_id}"
    event_response = requests.get(url)
    ev = event_response.json()

    # Variables for the card contents
    logo = f'logos/{ev['year']}_{ev['host']}.jpg'
    dates = f'{ev['start']} to {ev['end']}'
    host = f'{ev['host']} {ev['year']}'
    highlights = f'Highlights: {ev['highlights']}'
    participants = f'{ev['participants']} athletes'
    events = f'{ev['events']} events'
    countries = f'{ev['countries']} countries'

    card = dbc.Card([
        dbc.CardBody(
            [
                html.H4([html.Img(src=app.get_asset_url(logo), width=35, className="me-1"),
                         host]),
                html.Br(),
                html.H6(dates, className="card-subtitle"),
                html.P(highlights, className="card-text"),
                html.P(participants, className="card-text"),
                html.P(events, className="card-text"),
                html.P(countries, className="card-text"),
            ]
        ),
    ],
        style={"width": "18rem"},
    )
    return card


# Set to display event 12, this will be changed next week using a callback
card = create_card(12)
```

This [Charming Data video](https://www.youtube.com/watch?v=NEMDvIUaI6A) has more detail on getting data from an API.

This [Charming Data video](https://www.youtube.com/watch?v=THB9AEwdSXo) has more on the dbc Card.

## Further practice

This is optional for those that want to try and challenge themselves. There is no prepared solution for this.

- Add a new Row() with one or more columns to the layout.
- Use the event_data in the `figures.py`
- Create a new Plotly Expres chart .e.g. [bubble chart](https://plotly.com/python/bubble-charts/) or choose
  another [chart type](https://plotly.com/python/basic-charts/)
- Add the chart to a dcc.Graph() element in one of the columns you created.

Rather than using a card to display the statistics, create
a [table](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/table/) instead (or as well). Add
different event
attributes to what was used in the Card example.


