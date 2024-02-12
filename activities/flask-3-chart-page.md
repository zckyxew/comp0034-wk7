# Chart page

To create a chart in a page you need:

1. Code that creates a chart
2. A template that displays the chart
3. A route the calls the code to create the chart and passes this to the template

## Chart

Use a plotting library to create the chart and then convert it to a format that can be embedded in a webpage.

This example uses Plotly.express python as this is used in the Dash app activities;
and [converts the chart to HTML using the .to_html function](https://plotly.com/python/interactive-html-export/).

Add the following code to figures.py:

```python
import plotly.express as px
import pandas as pd

from paralympics_flask.models import Event


def line_chart(feature, db):
    """ Creates a line chart with data from paralympics_events.csv

     Parameters
     feature: events, sports, countries or participants
     
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

    # Get the data from the database using FlaskSQLAlechmy. Returns Event objects.
    events = db.session.execute(db.select(Event)).scalars()
    # Create a dataframe from the Event objects
    line_chart_df = pd.DataFrame([vars(e) for e in events])

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
    fig = px.line(line_chart_df,
                  x="year",
                  y=feature,
                  color="type",
                  title=title_text,
                  labels={'year': 'Year', feature: '', 'type': ''},
                  template="simple_white"
                  )

    # Convert to HTML
    plotly_jinja_data = {"fig": fig.to_html(full_html=False, include_plotlyjs=True, div_id="line-chart")}
    return plotly_jinja_data
```

## Route

The route code creates the chart html by calling the function you just created above from figures.py.

```python
from flask import current_app as app, render_template

from paralympics_flask.figures import line_chart
from paralympics_flask import db


@app.get('/chart')
def display_chart():
    """ Returns a page with a line chart. """
    line_fig_html = line_chart(feature="participants", db=db)
    return render_template('chart.html', fig_html=line_fig_html)
```

## Template

The chart template needs to have code that will display a plotly chart.

In the route above you passed a variable named `fig_html` that has the html for the chart in. To access the figure in
this use `fig_html.fig`.

You need to turn off auto-escaping when rendering the html which you can do using the `|safe` filter.

All you need to add to the content block of the template is: `{{ fig_html.fig | safe }}`

```jinja
{% extends 'base.html' %}

{% block title %}Chart{% endblock %}

{% block content %}
    {{ fig_html.fig | safe }}
{% endblock %}
```

## Run the app

Run the flask app  `flask --app paralympics_flask run --debug` and check that the route
works <http://127.0.0.1:5000/chart>