# COMP0034 Week 7 Coding activities

## Set-up

1. Fork the repository
2. Clone the forked repository to create a project in your IDE
3. Create and activate a virtual environment in the project folder e.g.

    - MacOS: `python3 -m venv .venv` then `source .venv/bin/activate`
    - Windows: `py -m venv .venv` then `.venv\Scripts\activate`
4. Check `pip` is the latest versions: `pip install --upgrade pip`
5. Install the requirements. You may wish to edit [requirements.txt](requirements.txt) first to remove the packages for
   Flask or Dash if you only want to complete the activities for one type of app.

    - e.g. `pip install -r requirements.txt`
6. Install the paralympics apps code e.g. `pip install -e .`

## Running the apps in the src directory

This repository contains 4 apps used in the activities which may cause some confusion for imports.

Remember to run `pip install -e .`

The apps can be run from the terminal as follows, you may need to use 'py' or 'python3' instead of 'python' depending
on your computer:

- Dash app: `python src/paralympics_dash/paralympics_dash.py`
- Dash multi-page app: `python src/paralympics_dash_multi/paralympics_app.py`
- Flask REST API app (coursework 1): `flask --app paralympics_rest run --debug`
- Flask app: `flask --app paralympics_flask run --debug`
- Flask ML app (Iris): `flask --app flask_iris:create(app) run --debug`

## Activity instructions

There are two sets of activities. You can complete both, or just the version for the framework you intend
to use for coursework 2.

### Dash activities

**The activities are designed to be completed in order**, skills are introduced in an activity and specific instructions
are not then repeated in subsequent activities.

| Activity                                        | Chart type                                       | Data access method       | Chart library  |
|:------------------------------------------------|:-------------------------------------------------|:-------------------------|:---------------|
| [Introduction](/activities/dash-0-intro.md)     |                                                  |                          |                |
| [Activity 1](/activities/dash-1-line-chart.md)  | Line chart                                       | pandas / .csv            | Plotly Express |
| [Activity 2](/activities/dash-2-bar-chart.md)   | Bar chart                                        | pandas / .csv            | Plotly Express |
| [Activity 3](/activities/dash-3-scatter-map.md) | Scatter Mapbox, map with markers                 | pandas / SQLite database | Plotly Go      |
| [Activity 4](/activities/dash-4-stats-card.md)  | Summary statistics presented in a Bootstrap card | pandas / REST API        | None           |

### Flask activities

**The activities are designed to be completed in order**, skills are introduced in an activity and specific instructions
are not then repeated in subsequent activities.

| Activity                                        | Data access | Jinja template | Form |
|:------------------------------------------------|:------------|:---------------|:-----|
| [Introduction](/activities/flask-0-intro.md)    |             |                |      |
| [Activity 1](/activities/flask-1-event-page.md) |             |                |      |
| [Activity 2](/activities/flask-2-home-page.md)  |             |                |      |
| [Activity 3](/activities/flask-3-chart-page.md) |             |                |      |
| [Activity 4](/activities/flask-1-event-page.md) |             |                |      |
