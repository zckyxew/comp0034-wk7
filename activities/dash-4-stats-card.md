# 4. Card

| Activity                           | Chart type                                       | Data access method | Chart library |
|:-----------------------------------|:-------------------------------------------------|:-------------------|:--------------|
| [Activity 4](dash-4-stats-card.md) | Summary statistics presented in a Bootstrap card | pandas / REST API  | None          |

The last example isn't a figure. This is a Bootstrap card using
the [dash-bootstrap-components card](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/).

It will display the details for a selected event. Next week you will add a callback that changes the event card based on
clicks on the map markers.

For this example, we will use the REST API route /events/<event_id>. You need to make sure that the REST API app is
running on your computer, to run it: `flask --app paralympics_rest run --debug`

To get data from an API you can use the Python requests library (part of the Python base library, you don't need to
install it separately).

The code to generate the card is moved into a function.

- The function takes an event id.
- It uses requests to make a request to the `http://127.0.0.1:5000/events/<event_id>` route using the event id passed to
  the function to generate the url string.
- The response from the request contains json.
- Variables to created with values from the json object.
- The card html is generated with the variables

```python
def create_card(event_id):
    """
    Generate a card for the event specified by event_id.

    Uses the REST API route.

    Args:
        event_id:

    Returns:
        card: dash boostrap components card for the event
    """
    # Use python requests to access your REST API on your localhost
    # Make sure you run the REST APP first and check your port number if you changed it from the default 5000
    url = f"http://127.0.0.1:5000/events/{event_id}"
    event_response = requests.get(url)
    ev = event_response.json()

    # Variables for the card contents
    logo = f'logos/{ev['year']}_{ev['host']}.jpg'
    dates = f'{ev['start']} to {ev['end']}'
    host = f'{ev['host']} {ev['year']}'
    highlights = f'Highlights: {ev['highlights']}'
    participants = f'{ev['participants']} athletes'
    events = f'{ev['events']} events'
    countries = f'{ev['countries']} countries'

    card = dbc.Card([
        dbc.CardBody(
            [
                html.H4([html.Img(src=app.get_asset_url(logo), width=35, className="me-1"),
                         host]),
                html.Br(),
                html.H6(dates, className="card-subtitle"),
                html.P(highlights, className="card-text"),
                html.P(participants, className="card-text"),
                html.P(events, className="card-text"),
                html.P(countries, className="card-text"),
            ]
        ),
    ],
        style={"width": "18rem"},
    )
    return card


# Set to display event 12, this will be changed next week using a callback
card = create_card(12)
```

This [Charming Data video](https://www.youtube.com/watch?v=NEMDvIUaI6A) has more detail on getting data from an API.

This [Charming Data video](https://www.youtube.com/watch?v=THB9AEwdSXo) has more on the dbc Card.
