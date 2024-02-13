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

Some page activities are introduced in week 8.

| Week | Page                                                                                                     | Data access                                       | Route                                                                                                                                                        | Jinja                                                                                        | Form                                                              | Other                                                        |
|:-----|:---------------------------------------------------------------------------------------------------------|:--------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|:------------------------------------------------------------------|:-------------------------------------------------------------|
| 7    | [Event details](flask-1-event-page.md)                                                                   | SQLAlchemy query                                  | GET: Find an event by id and pass it to the template                                                                                                         | Template with bootstrap rows and columns                                                     |                                                                   |                                                              |
| 7    | [Home with hyperlinked logos](flask-2-home-page.md)                                                      | SQLAlchemy query                                  | GET: Find all events and pass to the template                                                                                                                | Template with for loop generates logos + event year & host + hyperlink to events detail page |                                                                   | Access image files from /static<br>Dynamically generate URL. |
| 7    | [Chart](flask-3-chart-page.md)                                                                           | SQLAlchemy query with results to pandas DataFrame | GET: Get the HTML for the chart and pass to the template                                                                                                     | Displays HTML. Prevents auto-escaping of the variable with the HTML.                         |                                                                   |                                                              |
| 8    | [Add event](https://github.com/nicholsons/comp0034-wk8/blob/master/activities/flask-1-add-event-page.md) |                                                   | GET: Display the add event form.<br>POST: Use the values from the form to create a SQLAlchemy object and save to the database.                               |                                                                                              | Form to add fields for a new event. Validation. Form field macro. |                                                              |
| 8    | [Prediction](https://github.com/nicholsons/comp0034-wk8/blob/master/activities/flask-2-prediction.md)    | Use model.pkl to get a prediction                 | GET: Display the prediction form.<br>POST: Pass the values from the form to the model to get a prediction, update the page to display the prediction result. | Template with form and placeholder `<div>` for the prediction result.                        | Form to enter values for prediction. Validation. Default values.  | Create pickled ML model.                                     |
