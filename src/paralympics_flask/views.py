from flask import current_app as app, render_template
from paralympics_flask import db
from paralympics_flask.models import Event

# STARTER CODE FOR ACTIVITY 7
@app.route('/', methods=['GET'])
def index():
    """
    Returns the home page.
"""
    # Query the database to get all the events and arrange in date order
    events = db.session.execute(db.select(Event)).order_by(Event.year).scalars()
    return render_template('index.html', events=events)


@app.get('/events/<event_id>')
def get_event(event_id):
    """ Returns an event details page. """
    event = db.get_or_404(Event, event_id)
    return render_template('event.html', event=event)