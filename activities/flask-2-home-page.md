# Home page

## Current home page

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

## Route

Edit the route to get the data.

1. Query the database and get for each event get the 'id', 'host' and 'year' columns.
2. Construct a URL to get the relevant image from the `static/img` folder using the format year_host.jpg
3. Construct a URL that calls the '/events/<event_id>' route for each event
4. Pass the data and URLs to a jinja template

Use [Flask-SQLAlchemy query syntax](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#query-the-data)
to find the data. The example they use is as follows:

```python
users = db.session.execute(db.select(User).order_by(User.username)).scalars()
```

```python
@app.route('/', methods=['GET'])
def index():
    """ Returns the home page."""
    # Query the database to get all the events and arrange in date order
    events = db.session.execute(db.select(Event)).order_by(Event.year).scalars()
    return render_template('index.html', events=events)
```

## Template

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

## Run the app

Run the flask app  `flask --app paralympics_flask run --debug` and check that the route works.
