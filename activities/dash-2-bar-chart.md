# 2. Bar chart

| Activity                          | Chart type | Data access method | Chart library  |
|:----------------------------------|:-----------|:-------------------|:---------------|
| [Activity 2](dash-2-bar-chart.md) | Bar chart  | pandas / .csv      | Plotly Express |

## Create the bar chart

Create a stacked bar chart that shows the ratio of female:male competitors for either winter or summer events.

This requires further manipulation of the DataFrame before the chart can be created. See the comments in the code below.

Add the code to `figures.py`:

```python
def bar_gender(event_type):
    """
    Creates a stacked bar chart showing change in the number of sports in the summer and winter paralympics
    over time
    An example for exercise 2.

    :param event_type: str Winter or Summer
    :return: Plotly Express bar chart
    """
    cols = ['type', 'year', 'host', 'participants_m', 'participants_f', 'participants']
    df_events = pd.read_csv(event_data, usecols=cols)
    # Drop Rome as there is no male/female data
    df_events.drop([0], inplace=True, )
    df_events.reset_index(drop=True)
    # Add new columns that each contain the result of calculating the % of male and female participants
    df_events['M%'] = df_events['participants_m'] / df_events['participants']
    df_events['F%'] = df_events['participants_f'] / df_events['participants']
    # Sort the values by Type and Year
    df_events.sort_values(['type', 'year'], ascending=(True, True), inplace=True)
    # Create a new column that combines Location and Year to use as the x-axis
    df_events['xlabel'] = df_events['host'] + ' ' + df_events['year'].astype(str)
    # Create the stacked bar plot of the % for male and female
    df_events = df_events.loc[df_events['type'] == event_type]
    fig = px.bar(df_events,
                 x='xlabel',
                 y=['M%', 'F%'],
                 title='How has the ratio of female:male participants changed?',
                 labels={'xlabel': '', 'value': '', 'variable': ''},
                 color_discrete_map={'M%': 'blue', 'F%': 'green'},
                 template="simple_white"
                 )
    fig.update_xaxes(ticklen=0)
    return fig
```

## Add styling

Have a look at styling options and try and change some of
the [styling options](https://plotly.com/python/styling-plotly-express/) of the bar chart e.g. add a title, change the
colour of the bars.