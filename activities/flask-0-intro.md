# Flask activities

## Introduction

The paralympics app will have the following pages. The design for some pages is inspired by
the https://www.paralympic.org website.

- Event page that displays details for given event.
- Home page with logos for all the events. When you click on a logo it will display a page for that event.
- Chart page that displays a line chart.
-

Pages involving forms are introduced in week 8:

- Paralympics app: Add event page that allows data for a new event to be added to the database.
- Iris prediction app: Page that returns a prediction.

These pages cover most of the things you are likely to need for your app whether it deploys a machine learning model, or
provides 'other' functionality such as displaying and editing event data.

| Week | Page                                                                                                     | Data access                                       | Route                                                                                                                                                        | Jinja                                                                                        | Form                                                              | Other                                                        |
|:-----|:---------------------------------------------------------------------------------------------------------|:--------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|:------------------------------------------------------------------|:-------------------------------------------------------------|
| 7    | [Event details](flask-1-event-page.md)                                                                   | SQLAlchemy query                                  | GET: Find an event by id and pass it to the template                                                                                                         | Template with bootstrap rows and columns                                                     |                                                                   |                                                              |
| 7    | [Home with hyperlinked logos](flask-2-home-page.md)                                                      | SQLAlchemy query                                  | GET: Find all events and pass to the template                                                                                                                | Template with for loop generates logos + event year & host + hyperlink to events detail page |                                                                   | Access image files from /static<br>Dynamically generate URL. |
| 7    | [Chart](flask-3-chart-page.md)                                                                           | SQLAlchemy query with results to pandas DataFrame | GET: Get the HTML for the chart and pass to the template                                                                                                     | Displays HTML. Prevents auto-escaping of the variable with the HTML.                         |                                                                   |                                                              |
| 8    | [Add event](https://github.com/nicholsons/comp0034-wk8/blob/master/activities/flask-1-add-event-page.md) |                                                   |                                                                                                                                                              |                                                                                              | Form to add fields for a new event. Validation. Form field macro. |                                                              |
| 8    | [Prediction](https://github.com/nicholsons/comp0034-wk8/blob/master/activities/flask-2-prediction.md)    | Use model.pkl to get a prediction                 | GET: Display the prediction form.<br>POST: Pass the values from the form to the model to get a prediction, update the page to display the prediction result. | Template with form and placeholder `<div>` for the prediction result.                        | Form to enter values for prediction. Validation. Default values.  | Create pickled ML model.                                     |

## Check the Flask app runs and remove unnecessary routes

Check that the app runs before starting any of the activities.

The activities build on the Flask app as at the end of the week 6 activities. The routes
for: `index_css()`, `index_html()`, `index_jinja()`, `index_responsive()` can all be deleted. These are
example solutions to week 6 activities. You only need to keep `index()` for this week's activities.

1. `flask --app paralympics_flask run --debug`
2. Go to the URL that is shown in the terminal. By default, this is <http://127.0.0.1:5000>
3. Stop the app using `CTRL+C`
