# Flask version of the activities

The design for the pages is inspired by the https://www.paralympic.org website.

## Check the Flask app runs

Check that the app runs before starting any of the activities.

1. `flask --app paralympics_flask run --debug`
2. Go to the URL that is shown in the terminal. By default, this is <http://127.0.0.1:5000>
3. Stop the app using `CTRL+C`

## Paralympics Flask app overview

The paralympics app will have the following pages:

1. Event page that displays details for given event.
2. Home page with logos for all the events. When you click on a logo it will display a page for that event.
3. A page that allows a new event data to be added.
4. A page that includes a chart

This will require:

- A variable route for the event details page and a Jinja template for the event page
- Changes to the route for the homepage and the index template
- A route for the add event page, a form class with validation, and a Jinja template
- A route that allows a prediction

These cover most of the things you are likely to need for your app whether it deploys a machine learning model, or
provides 'other' functionality such as displaying and editing event data.

This builds on the Flask app as at the end of the week 6 activities.

The routes for: `index_css()`, `index_html()`, `index_jinja()`, `index_responsive()` can all be deleted. These are
example solutions to week 6 activities. You only need to keep `index()` for this week's activities.

## Event page

### Add a route

Add a variable route to the views.py file. This is a GET request. It takes the 'id' of an event. You did something
similar when you created the REST API.

```python
@app.get('/events/<event_id>')
def get_event(event_id):
```

The route needs to find the data for the given event and pass that to a Jinja template. The template will be created in
the subsequent step.

Use [Flask-SQLAlchemy query syntax](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#query-the-data)
to find the data. This has a method that will find an Event and if the event is not found returs a 404 not found error.
The example given is `user = db.get_or_404(User, id)`.

The data can then be passed to the page template.

```python
from flask import current_app as app, render_template

from paralympics_flask import db
from paralympics_flask.models import Event


@app.get('/events/<event_id>')
def get_event(event_id):
    """ Returns an event details page. """
    event = db.get_or_404(Event, event_id)
    return render_template('event.html', event=event)
```

Add the code to the views.py file. You will not be able to run the app yet as the events.html does not exist.

### Create the events template

Add an events.html to the templates directory. It should look like this:

```jinja
{% extends 'base.html' %}

{% block title %}{% endblock %}

{% block content %}
    
{% endblock %}
```

In the route you passed a variable named 'event' to the template. You can use Jinja syntax to access values from that
variable in `{{ }}`.

To set the page tutle for example, add:

```jinja
{% block title %}
   {{ event['host']  }} {{ event['year'] }}
{% endblock %}
```

For the 'content' block, use a [Bootstrap grid](https://getbootstrap.com/docs/5.3/layout/grid/) with 2 columns and rows
6 rows to add the event details.

The basic structure of a row is:

```html

<div class="container text-center">
    <div class="row">
        <div class="col">col</div>
        <div class="col">col</div>
    </div>
</div>
```

The rows will have strings using data from the event attributes:

- Host City: `event['host']`
- Dates: `event['start']` and `event['end']`
- Events: `event['events']` in `event['sports']` sports
- Countries: `event['countries']`
- Participants: `event['participant']` (`event['participants_f']` female and `event['participants_m']` male)
- Highlights: `event['highlights'

Add the HTML to the `{% block content %}` section of the page. Use the `{{ }}` to add the variables. For example:

```jinja
<div class="row">
    <div class="col">Highlights</div>
    <div class="col">{{ event['countries'] }}</div>
</div>
```

Run the app and go to <http://127.0.0.1:5000/events/12>.

The styling is basic. You could alter the column widths, change the font type/size etc. You will need to refer to the
Bootstrap documentation to find the relevant classes.

## Home page

### Current home page

The code looks something like this:

```python
@app.route('/', methods=['GET'])
def index():
    """ Returns the home page."""
    return render_template('index.html')
```

The `index.html` template is a Jinja template that inherits from the page layout and looks like this:

```jinja
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    <p>This is the {{ self.title() }} page.</p>
{% endblock %}
```

### Edit the route to get the data

1. Query the database and get for each event get the 'id', 'host' and 'year' columns.
2. Construct a URL to get the relevant image from the `static/img` folder using the format year_host.jpg
3. Construct a URL that calls the '/events/<event_id>' route for each event
4. Pass the data and URLs to a jinja template

Use [Flask-SQLAlchemy query syntax](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#query-the-data)
to find the data. The example they use is as follows:

```python
users = db.session.execute(db.select(User).order_by(User.username)).scalars()
```

We only want 3 attributes: id, host and year:

```python
@app.route('/', methods=['GET'])
def index():
    """ Returns the home page."""
    # Query the database to get all the events and arrange in date order
    events = db.session.execute(db.select(Event)).order_by(Event.year).scalars()
    return render_template('index.html', events=events)
```

### Edit the Jinja template

Edit Jinja template that iterates the data and generates a list of logos and event year plus host that is a
hyperlink to that events detail page.

You can iterate the data passed to the template using a Jinja for loop e.g.

```jinja
    {%  for event in events %}
        
    {% endfor %}
```

For each event you can define the logo using an HTML <img>
e.g. `<img src="img_girl.jpg" alt="Girl in a jacket" width="500" height="600">`.
The src is the file location which you can determine using the file name format `{event.year}_{event.host}.png`
and the URL using the flask url_for url_for('static', filename=f'img/{logo_file}')

The hyperlink is created using an `<a href="someurlhere"></a>` tag where the url is "/events/{event.id}"

Use a column/row style layout again.

```jinja
{% block content %}
    <div class="container">
        {# For loop to iterate each event and add a row with the logo and linked text #}
        {% for event in events %}
            <div class="row">
                {# first column has the logo. You can't nest Jinja variables so you need to set the filename then use it #}
                <div class="col-2">
                    {% set path = url_for('static', filename='img/' + event.year|string + '_' + event.host + '.jpg') %}
                    <img src="{{ path }}" alt="Paralympic logo" height="50">
                </div>
                {# column has text with a hyperlink to the page #}
                <div class="col-10"><a
                        href="{{ url_for('get_event', event_id=event.id) }}">{{ event.host }} {{ event.year }}</a>
                </div>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

### Run the app

Run the flask app and check that the route works.

## Add event page

## Edit event page

This is an optional challenge, code solution is not provided.

Add a page to edit an existing event.

1. Generate a page with a form that contains the existing data for an event.
2. Allow the fields to be edited.
3. Verify that any changes meet the validation criteria.
4. Update the database with the changes.
5. Display the event page with the edited data.

## Page that returns a prediction

There is no ML model for the paralympics app so this example creates a simple one-page Flask app with a form to predict
the species of Iris.

The code in the src/flask_iris directory structure creates a basic Flask app that includes a form to get a prediction
from a pickled model.

There is a form defined in [/src/flask_iris/forms.py](../src/flask_iris/forms.py) which 4 fields for each value required
to get a prediction.

There is a single route in [src/flask_iris/routes.py](../src/flask_iris/routes.py) which on GET returns a form, and on
POST if all the fields of the form have been completed .

The code to generate the model is in [/src/flask_iris/create_ml_model.py](../src/flask_iris/create_ml_model.py).

To run the app: `flask --app flask_iris:create(app) run --debug`

