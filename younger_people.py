import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn
import plotly
from dash.dependencies import Input, Output
from collections import Counter
import plotly.graph_objs as go

from app import  app
#import csv
london = pd.read_csv('data/children & Younger people/indicators-CountyUA.data london young people.csv')
east_mid = pd.read_csv("data/children & Younger people/indicators-CountyUA.data east mid.csv")
east_england = pd.read_csv("data/children & Younger people/indicators-CountyUA.data east of england.csv")
north_east = pd.read_csv("data/children & Younger people/indicators-CountyUA.data north east young people.csv")
north_west = pd.read_csv("data/children & Younger people/indicators-CountyUA.data north west.csv")
south_west = pd.read_csv("data/children & Younger people/indicators-CountyUA.data south west.csv")
south_east = pd.read_csv("data/children & Younger people/indicators-CountyUA.data southeast.csv")
west_midlands = pd.read_csv("data/children & Younger people/indicators-CountyUA.data west midlands.csv")
yorkshire = pd.read_csv("data/children & Younger people/indicators-CountyUA.data yorkshire &.csv")

#For Console to show all columns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#drop Columns
tables_to_drop = ["IndicatorID", "ParentCode", "ParentName", "AreaCode",  "AreaType",
                      "Recent_Trend", "Category_Type", "Value_note",
                                                "Time_period_Sortable", "Category",   "Upper_CI_99.8_limit",
                      "Upper_CI_95.0_limit", "Lower_CI_99.8_limit",
                                                "New_data", "Compared_to_goal",
                  "Compared_to_England_value_or_percentiles","Compared_to_Region_value_or_percentiles",
                  "Lower_CI_95.0_limit"]




london = london.drop(tables_to_drop, axis = 1)
east_mid = east_mid.drop(tables_to_drop, axis = 1)
east_england = east_england.drop(tables_to_drop, axis = 1)
north_east = north_east.drop(tables_to_drop, axis = 1)
north_west = north_west.drop(tables_to_drop, axis = 1)
south_west = south_west.drop(tables_to_drop, axis = 1)
south_east = south_east.drop(tables_to_drop, axis = 1)
west_midlands = west_midlands.drop(tables_to_drop, axis = 1)
yorkshire = yorkshire.drop(tables_to_drop, axis = 1)

data_join = [london, east_mid, east_england, north_east, north_west,
             south_west, south_east, west_midlands, yorkshire]

all_data =  pd.concat(data_join)
all_data = all_data[all_data.AreaName != "England"]



# get rid of test name.
test = all_data.groupby(["IndicatorName", "AreaName"]).size().reset_index()


type(test)
test.columns = ["IndicatorName", "AreaName","IndicatorPerArea"]

print(test)



younger_people_layout = html.Div([
    html.H1('Children & Younger People Analysis', id="title"),


#make this stacled
     dcc.Graph(
            figure = go.Figure(
                data=[
                    go.Bar(
                        x=test["IndicatorName"],
                        y=test["IndicatorPerArea"],
                text = test.IndicatorPerArea,
                textposition='auto'
                        #name=test["AreaName"]
                    )

                ],
                layout=go.Layout(
                 title="test",
                )
            )
        ),

    html.Details([
        html.Summary("United Kingdom Data"),

        html.Br(),

        html.Div([

            dcc.Graph(
                id="all_data_graph",
                figure={
                    'data': [

                        go.Scatter(
                            x=all_data[all_data["AreaName"] == i]['Timeperiod'],
                            y=all_data[all_data["AreaName"] == i ]['IndicatorName'],
                            #text=all_data[all_data["AreaName"] == i ]["Amount"],
                            mode='markers',
                            opacity=0.6,
                            marker={
                              'size':10,
                                'line': {'width' : 0.5, 'color' :'white'},

                            },
                           name=i,
                        )
                        for i in all_data.AreaName.unique()
                    ],
                    'layout': go.Layout(
                        xaxis={'title': "Time Period", 'autorange':True},
                        yaxis={'title': "Age", 'autorange':True},
                        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                         #legend={'x': 0, 'y': 1},
                           hovermode='closest',
                        autosize = True,

                    )
                }
            )

        ]),
        html.Br(),



        dash_table.DataTable(
            id="all_data",

            columns=[{'id': c, 'name': c} for c in all_data.columns],
            data=all_data.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="multi",
            style_table={'overflowX': 'scroll'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
        ),




    ]),

    html.Details([
        html.Summary("East Midlands Details"),
        html.Br(),

html.Div([


        ]),
        html.Br(),

        dash_table.DataTable(
            id="east_midlands_table",
            columns=[{'id': c, 'name': c} for c in east_mid.columns],
            data=east_mid.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="multi",
            style_table={'overflowX': 'scroll'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
        ),
    ]),

    html.Details([
        html.Summary("East of England Details"),
        html.Br(),
        dash_table.DataTable(
            id="east_england_table",
            columns=[{'id': c, 'name': c} for c in east_england.columns],
            data=east_england.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="multi",
            style_table={'overflowX': 'scroll'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
        ),
    ]),

    html.Details([
        html.Summary("London Details"),
        html.Br(),
        dash_table.DataTable(
            id="london_table",

            columns=[{'id': c, 'name': c} for c in london.columns],
            data=london.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="multi",
            style_table={'overflowX': 'scroll'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
        ),
    ]),

    html.Details([
        html.Summary("North East Details"),
        html.Br(),

        dash_table.DataTable(
            id="north_east_table",

            columns=[{'id': c, 'name': c} for c in north_east.columns],
            data=north_east.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="multi",
            style_table={'overflowX': 'scroll'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
        ),
    ]),

    html.Details([
        html.Summary("North West Details"),
        html.Br(),
        dash_table.DataTable(
            id="north_west_table",

            columns=[{'id': c, 'name': c} for c in north_west.columns],
            data=north_west.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="multi",
            style_table={'overflowX': 'scroll'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
        ),
    ]),

    html.Details([
        html.Summary("South East Details"),
        html.Br(),
        dash_table.DataTable(
            id="south_east_table",
            columns=[{'id': c, 'name': c} for c in south_east.columns],
            data=south_east.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="multi",
            style_table={'overflowX': 'scroll'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],

        ),
    ]),

    html.Details([
        html.Summary("South West Details"),
        html.Br(),
        dash_table.DataTable(
            id="south_west_table",
            columns=[{'id': c, 'name': c} for c in south_west.columns],
            data=south_west.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="multi",
            style_table={'overflowX': 'scroll'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
        ),
    ]),

    html.Details([
        html.Summary("West Midlands Details"),
        html.Br(),
        dash_table.DataTable(
            id="west_midlands_table",
            columns=[{'id': c, 'name': c} for c in west_midlands.columns],
            data=west_midlands.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="multi",
            style_table={'overflowX': 'scroll'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
        ),
    ]),

        html.Div(id='younger_content'),

])




@app.callback(Output('younger_content', 'children'),
        [Input('young', 'value')])

def display_value(value):
        return 'You have selected "{}"'.format(value)