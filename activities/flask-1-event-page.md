# Event page

## Route

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

## Template

Add an events.html to the /templates directory. The basic structure is:

```jinja
{% extends 'base.html' %}

{% block title %}{% endblock %}

{% block content %}
    
{% endblock %}
```

In the route you passed a variable named 'event' to the template. You can use Jinja syntax to access values from that
variable in `{{ }}`.

To set the page title, update the title block to display the values you want. The code below gets the host and year from
the event object that was passed to the template:

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

Add the HTML to the `{% block content %}` section of the page. Use the `{{ }}` to add the variables. For example, the
first row would be:

```jinja
<div class="row">
    <div class="col">Host City</div>
    <div class="col">{{ event['host'] }}</div>
</div>
```

Repeat the code for the remaining rows (dates, events, etc.).

Run the app `flask --app paralympics_flask run --debug` and go to <http://127.0.0.1:5000/events/12>.

The styling is basic. You could alter the column widths, change the font type/size etc. You will need to refer to the
Bootstrap documentation to find the relevant classes.
