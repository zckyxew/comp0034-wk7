# Plotly Dash version of the activities: Creating and adding charts to a Dash app layout

## Check the Dash app runs

1. `python paralympics_dash/paralympics_dash.py`

   You may need to change the port number if you already have something running on the default port 8050
   e.g. `flask --app paralympics_flask run --debug --port=5050`.

2. Go to the URL that is shown in the terminal. By default, this is <http://127.0.0.1:8050>.
3. Stop the app using `CTRL+C`

## Introduction

In this activity you will learn to create and add charts to a Dash app layout. You will then replace the chart images
you added to the chart last week with charts.

Next week you will add the callback functionality that will allow the charts to be dynamically updated.

Plotly graphing library for Python (NOT the version for JavaScript) can be accessed through two libraries, Plotly
Express and Plotly Go. Plotly Express API provides Python classes and functions to create most types of charts, and in
most cases will be sufficient for the coursework. Sometimes you may need to edit aspects of a chart that isn't available
through Express functions, and then you need to use Go instead. Many of the
chart examples in the [Plotly documentation](https://plotly.com/python/) start with an Express example, then show
features that require Go, and include a version that can be added to a Dash app.

The Plotly documentation shows examples of code for many types of chart, however this assumes you already know the type
of chart you want to create. To help you decide which type of chart may be suited to your particular data and audience,
then try one of the many tools to help you select the type of chart/data visualisation:

- [Data Visualisation Catalogue](https://datavizcatalogue.com/index.html)
- [Depict Data Studio](https://depictdatastudio.com/charts/)
- [Page with links to other chart choosers](https://coolinfographics.com/dataviz-guides)

This activity covers the following data visualisations:

1. line chart
2. bar chart
3. map with markers
4. summary statistics presented in card format

The first two access data from a pandas DataFrame; the third from a SQLite database; and the final one uses data from a
REST API. This is to introduce different ways of accessing the data. For your coursework, pick one method to use.

The general approach to create and add a chart to a Dash application is:

1. Access the required data
2. Create a chart object using the data
3. Add the chart object to the Dash app layout

## Line chart

### Create a line chart using pandas and Plotly Express

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

## Create a bar chart

Create a stacked bar chart that shows the ratio of female:male competitors for either winter or summer events.

This requires further manipulation of the DataFrame before the chart can be created.

Add the code to `figures.py`

> NOT COMPLETE YET!