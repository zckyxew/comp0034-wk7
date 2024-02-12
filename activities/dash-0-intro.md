# Plotly Dash version of the activities: Creating and adding charts to a Dash app layout

The text below assumes you are using the single page app in paralympics_dash. You could instead apply the same to the
multi-page app in paralympics_dash_multi editing the layouts in the pages rather than the main dashboard python file.

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

The general approach to create and add a chart to a Dash application is:

1. Access the required data
2. Create a chart object using the data
3. Add the chart object to the Dash app layout

This week's activities cover the data visualisations listed in the table below. The examples use different ways to
access the data. The purpose of this is to introduce different ways of accessing the data. For your coursework don't do
this, pick one method to use.

| Activity                            | Chart type                                       | Data access method       | Chart library  |
|:------------------------------------|:-------------------------------------------------|:-------------------------|:---------------|
| [Activity 1](dash-1-line-chart.md)  | Line chart                                       | pandas / .csv            | Plotly Express |
| [Activity 2](dash-2-bar-chart.md)   | Bar chart                                        | pandas / .csv            | Plotly Express |
| [Activity 3](dash-3-scatter-map.md) | Scatter Mapbox, map with markers                 | pandas / SQLite database | Plotly Go      |
| [Activity 4](dash-4-stats-card.md)  | Summary statistics presented in a Bootstrap card | pandas / REST API        | None           |

## Check the Dash app runs

1. `python src/paralympics_dash/paralympics_dash.py`
2. Go to the URL that is shown in the terminal. By default, this is <http://127.0.0.1:8050>.
3. Stop the app using `CTRL+C`
