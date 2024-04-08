from flask import current_app as app, render_template
from paralympics_flask import db
from paralympics_flask.models import Event
from paralympics_flask.figures import line_chart


# STARTER CODE FOR ACTIVITY 7
@app.route('/', methods=['GET'])
def index():
    """
    Returns the home page.
"""
    # Query the database to get all the events and arrange in date order
    events = db.session.execute(db.select(Event).order_by(Event.year)).scalars()
    return render_template('index.html', events=events)


@app.get('/events/<event_id>')
def get_event(event_id):
    """ Returns an event details page. """
    event = db.get_or_404(Event, event_id)
    return render_template('events.html', event=event)


@app.get('/chart')
def display_chart():
    """ Returns a page with a line chart. """
    line_fig_html = line_chart(feature="participants", db=db)
    return render_template('chart.html', fig_html=line_fig_html)
