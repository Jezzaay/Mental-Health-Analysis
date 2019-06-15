import pprint
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
from dash.dependencies import Input, Output
from collections import Counter
import plotly.graph_objs as go
import plotly.tools as tls

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

#London Data

london= london[london.AreaName  != "England"]

london_data = london.groupby(["IndicatorName", "Timeperiod"]).size().reset_index()
london_data.columns = ["IndicatorName", "Year", "IndicatorFigures"]
#East Mid
east_mid = east_mid[east_mid != "England"]
east_mid_data = east_mid.groupby(["IndicatorName", "Timeperiod"]).size().reset_index()
east_mid_data.columns = ["IndicatorName", "Year", "IndicatorFigures"]
#East England
east_england = east_england[east_england!= "England"]
east_england_data = east_england.groupby(["IndicatorName", "Timeperiod"]).size().reset_index()
east_england_data.columns = ["IndicatorName", "Year", "IndicatorFigures"]
#North East
north_east = north_east[north_east!= "England"]
ne_data = north_east.groupby(["IndicatorName", "Timeperiod"]).size().reset_index()
ne_data.columns = ["IndicatorName", "Year", "IndicatorFigures"]
#North West
north_west = north_west[north_west!= "England"]
nw_data = north_west.groupby(["IndicatorName", "Timeperiod"]).size().reset_index()
nw_data.columns = ["IndicatorName", "Year", "IndicatorFigures"]
#South West
south_west = south_west[south_east!= "England"]
sw_data = south_west.groupby(["IndicatorName", "Timeperiod"]).size().reset_index()
sw_data.columns = ["IndicatorName", "Year", "IndicatorFigures"]
#South East
south_east = south_east[south_east!= "England"]
se_data = south_east.groupby(["IndicatorName", "Timeperiod"]).size().reset_index()
se_data.columns = ["IndicatorName", "Year", "IndicatorFigures"]
#West Mid
west_midlands = west_midlands[west_midlands!= "England"]
west_mid_data = west_midlands.groupby(["IndicatorName", "Timeperiod"]).size().reset_index()
west_mid_data.columns = ["IndicatorName", "Year", "IndicatorFigures"]
#Yorkshire
yorkshire = yorkshire[yorkshire!= "England"]
yorkshire_data = yorkshire.groupby(["IndicatorName", "Timeperiod"]).size().reset_index()
yorkshire_data.columns = ["IndicatorName", "Year", "IndicatorFigures"]



younger_people_layout = html.Div([
    html.H1('Children & Younger People Analysis', id="title"),





    html.Details([
        html.Summary("United Kingdom Data"),

        html.Br(),

        html.Div([

            dcc.Graph( id="all_data_graph",figure={
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

html.Div([ ]),
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


                  dcc.Graph(
            id='london_graph',
            figure={
                'data': [
                    {'x': london_data["Year"],
                     'y': london_data["IndicatorFigures"], 'type': 'bar',
                     'text':  london_data["IndicatorName"]}
                ],
                'layout': dict(title='London Younger People Data', showLegend=True, barmode="stack")
            }
        ),


        html.Br(),



        dash_table.DataTable(
            id="london_table",

            columns=[{'id': c, 'name': c} for c in london_data.columns],
            data=london_data.to_dict('records'),
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

            columns=[{'id': c, 'name': c} for c in ne_data.columns],
            data=ne_data.to_dict('records'),
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

            columns=[{'id': c, 'name': c} for c in nw_data.columns],
            data=nw_data.to_dict('records'),
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
            columns=[{'id': c, 'name': c} for c in se_data.columns],
            data=se_data.to_dict('records'),
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
            columns=[{'id': c, 'name': c} for c in sw_data.columns],
            data=sw_data.to_dict('records'),
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
            columns=[{'id': c, 'name': c} for c in west_mid_data.columns],
            data=west_mid_data.to_dict('records'),
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
        html.Summary("Yorkshire Details"),
        html.Br(),
        dash_table.DataTable(
            id="west_midlands_table",
            columns=[{'id': c, 'name': c} for c in yorkshire_data.columns],
            data=yorkshire_data.to_dict('records'),
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
