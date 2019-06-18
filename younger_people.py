
import dash
import dash_core_components as dcc
import dash_html_components as html
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

#drop Columns as not using these in the analysis
tables_to_drop = ["IndicatorID", "ParentCode",  "AreaCode",  "AreaType",
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

#joining the columns together for the all data section
data_join = [london, east_mid, east_england, north_east, north_west,
             south_west, south_east, west_midlands, yorkshire]


#All of England
all_data =  pd.concat(data_join)
all_data = all_data[all_data.AreaName != "England"]
all_data = all_data[all_data.ParentName != "England"]
england = all_data.groupby(["IndicatorName", "Timeperiod", "ParentName"]).size().reset_index()
england.columns = ["IndicatorName", "Year", "Region", "IndicatorFigures"]

#England WO London
eng_wo_london = [east_mid, east_england, north_east, north_west,
             south_west, south_east, west_midlands, yorkshire]
england_wo_london = pd.concat(eng_wo_london)
england_wo_london = england_wo_london[england_wo_london.AreaName != "England"]
england_wo_london = england_wo_london[england_wo_london.ParentName != "England"]
england_wo_london = england_wo_london.groupby(["IndicatorName", "Timeperiod", "ParentName"]).size().reset_index()
england_wo_london.columns = ["IndicatorName", "Year", "Region", "IndicatorFigures"]

# England Region Count
england_reg = all_data.groupby(["ParentName", "Timeperiod"]).size().reset_index()
england_reg.columns = ["Region", "Year", "Figures"]


#London Data
london= london[london.AreaName  != "England"]

london_data = london.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
london_data.columns = ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]
#East Mid
east_mid = east_mid[east_mid != "England"]
east_mid_data = east_mid.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
east_mid_data.columns = ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]
#East England
east_england = east_england[east_england!= "England"]
east_england_data = east_england.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
east_england_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]
#North East
north_east = north_east[north_east!= "England"]
ne_data = north_east.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
ne_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]
#North West
north_west = north_west[north_west!= "England"]
nw_data = north_west.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
nw_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]
#South West
south_west = south_west[south_east!= "England"]
sw_data = south_west.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
sw_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]
#South East
south_east = south_east[south_east!= "England"]
se_data = south_east.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
se_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]
#West Mid
west_midlands = west_midlands[west_midlands!= "England"]
west_mid_data = west_midlands.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
west_mid_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]
#Yorkshire
yorkshire = yorkshire[yorkshire!= "England"]
yorkshire_data = yorkshire.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
yorkshire_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]

# Page Layout
younger_people_layout = html.Div([
    html.H1('Children & Younger People Analysis', id="title"),
    html.P("Hover over the area names for the cells indicator name, as many places in the dataset have 1's for each "
           "indicator it may have repetitions for the area name in the cells but they are for different indicators. "
           "Hovering also displays the indicator value. "
           "The graphs are Year and Indicator Figures in a bar chart. Although the bar may seem to be high but that is "
           "every reported case for that year within the dataset"),
    html.P("London has the largest of this data. To read London area names zooming in is required."
           "Each graph is scaled so the text is clearly visible. However, there are tools, to zoom in or out.   "),

    html.Details([ # Details allows to hide sections in the page until clicked.
        html.Summary("England Data"),
        html.P("Two Graphs showing Data for England. One displaying data including London and one without. "
               "The reason for this is to show the data that London may contain majority of the data. Therefore,"
               "the data being shown can be more accurate and can give the viewer a better outlook on the data. "),
        html.Br(),


        html.Br(),


        #Dash datatable to display to users
        dash_table.DataTable(
            id="all_data",
            columns=[{'id': c, 'name': c} for c in england.columns],
            data=england.to_dict('records'),
            filtering=True, # Allows users to filter
            sorting=True,
            sorting_type="single", # Only one column can be sorted at a time
            pagination_settings={ # how many are shown at once
                "current_page": 0,
                "page_size": 5,
            },
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

        html.Div([

            html.P("Bar Plot for England Data without London. As London is massive it is important to show the England "
                   "data without London including, whereas another will also show London to compare. "),
            dcc.Graph(
                id='all_wo_lon_graph',
                figure={
                    'data': [
                        {'x': england_wo_london["Year"],
                         'y': england_wo_london["IndicatorFigures"],
                         'type': 'bar',  # bar
                         'text': england_wo_london["Region"],
                         'textposition': "inside",  # Showing the Text inside each block per year
                         'hovertext': england_wo_london["IndicatorName"],
                         'opacity': 0.8,
                         'marker': dict(color="rgb(255,165,0)"
                                        ),
                         }
                    ],
                    # setting the layout, title, axes
                    'layout': dict(title='England Younger People Data (Without London)', autosize=True, barmode="stack",
                                   xaxis={'title': "Years"},
                                   yaxis={'title': "Indicator Figures (Total Figures for Year)",
                                          'range': [0, 500]},
                                   height=2500,
                                   hovermode="closest"
                                   )
                }
            ),
                html.P("Bar Plot for England Data with London. As it is seen in the plot, "
                       "london takes up majority of the space. "),
            dcc.Graph(
                id='england_graph_w_london',
                figure={
                    'data': [
                        {'x': england["Year"],
                         'y': england["IndicatorFigures"],
                         'type': 'bar',  # bar
                         'text': england["Region"],
                         'textposition': "inside",  # Showing the Text inside each block per year
                         'hovertext': england["IndicatorName"],
                         'opacity': 0.8,
                         'marker': dict(color="rgb(255,165,0)"
                                        ),
                         }
                    ],
                    # setting the layout, title, axes
                    'layout': dict(title='England Younger People Data (Including London) ', autosize=True, barmode="stack",
                                   xaxis={'title': "Years"},
                                   yaxis={'title': "Indicator Figures (Total Figures for Year)",
                                          'range': [0, 1000]},
                                   height=2500,
                                   hovermode="closest"
                                   )
                }
            ),
            html.P("England just split into regions for their figures on younger people mental health "
                   "data not showing each indicator/illness. This then shows which "
                   "regions have the highest amount of figures"),
            dcc.Graph(
                id='england_regions',
                figure={
                    'data': [
                        {'x': england_reg["Year"],
                         'y': england_reg["Figures"],
                         'type': 'bar',  # bar
                         'text': england_reg["Region"],
                         'textposition': "inside",  # Showing the Text inside each block per year
                         'hovertext': england_reg["Region"],
                         'opacity': 0.8,
                         'marker': dict(color="rgb(255,165,0)"
                                        ),
                         }
                    ],
                    # setting the layout, title, axes
                    'layout': dict(title='England Region Figures For Younger People Data', autosize=True, barmode="stack",
                                   xaxis={'title': "Years"},
                                   yaxis={'title': "Indicator Figures (Total Figures for Year)",
                                          'range': [0, 1000]},
                                   height=2500,
                                   hovermode="closest"
                                   )
                }
            ),


        ]),



    ]),

    html.Details([
        html.Summary("East Midlands Details"),
        html.Br(),

html.Div([ ]),
        html.H1("East Midlands Data"),
        html.P("This includes areas such as Derby, Nottingham, Rutland"),
        html.Br(),


        dash_table.DataTable(
            id="east_midlands_table",
            columns=[{'id': c, 'name': c} for c in east_mid_data.columns],
            data=east_mid_data.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="single",
            pagination_settings={
                "current_page":0,
                "page_size": 5,
            },
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

        dcc.Graph(
            id='east_mid_graph',
            figure={
                'data': [
                    {'x': east_mid_data["Year"],
                     'y': east_mid_data["IndicatorFigures"], 'type': 'bar',
                     'text': east_mid_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': east_mid_data["IndicatorName"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"
                                              ),
                     }
                ],
                'layout': dict(title='East Midlands Younger People Data', autosize=True, barmode="stack",
                               xaxis={'title': "Years"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=1200,
                               hovermode="closest"
                               )
            }
        ),

        html.Br(),

    ]),

    html.Details([
        html.Summary("East of England Details"),
        html.H1("East of England Data"),
         html.P("This includes areas such as Luton, Bedford, Essex, Cambridgeshire"),


        html.Br(),
        dash_table.DataTable(
            id="east_england_table",
            columns=[{'id': c, 'name': c} for c in east_england_data.columns],
            data=east_england_data.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="single",
            pagination_settings={
                "current_page": 0,
                "page_size": 5,
            },
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
        dcc.Graph(
            id='east_england_graph',
            figure={
                'data': [
                    {'x': east_england_data["Year"],
                     'y': east_england_data["IndicatorFigures"], 'type': 'bar',
                     'text': east_england_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': east_england_data["IndicatorName"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"),
                     }
                ],
                'layout': dict(title='East of England Younger People Data', autosize=True, barmode="group",
                               xaxis={'title': "Years"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=1500,
                               hovermode="closest")
            }
        ),

    ]),

    html.Details([
        html.Summary("London Details"),
        html.H1("London Data"),
                html.P("This includes areas such as Brent, Camden, Enfield"),



        html.Br(),



        dash_table.DataTable(
            id="london_table",

            columns=[{'id': c, 'name': c} for c in london_data.columns],
            data=london_data.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="single",
            pagination_mode="fe",
            pagination_settings={
                "current_page":0,
                "page_size": 5,
            },
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

        dcc.Graph(
            id='london_graph',
            figure={
                'data': [
                    {'x': london_data["Year"],
                     'y': london_data["IndicatorFigures"], 'type': 'bar',
                     'text': london_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': london_data["IndicatorName"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"),
                     }
                ],
                'layout': dict(title='London Younger People Data', autosize=True,
                               xaxis={'title': "Years"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)",
                                      'dtick': 100}, #  how many ticks per axis in this case Y.
                               height=2500,
                               hovermode="closest")
            }
        ),

        html.Div(id="london_container")
    ]),

    html.Details([
        html.Summary("North East Details"),
        html.H1("North East Data"),
                html.P("This includes areas such as Sunderland, Gateshead, Middlesbrough"),

        html.Br(),

        dash_table.DataTable(
            id="north_east_table",

            columns=[{'id': c, 'name': c} for c in ne_data.columns],
            data=ne_data.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="single",
            pagination_settings={
                "current_page": 0,
                "page_size": 5,
            },
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
        dcc.Graph(
            id='ne_graph',
            figure={
                'data': [
                    {'x': ne_data["Year"],
                     'y': ne_data["IndicatorFigures"], 'type': 'bar',
                     'text': ne_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': ne_data["IndicatorName"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"),
                     }
                ],
                'layout': dict(title='North East England Younger People Data', autosize=True,
                               xaxis={'title': "Years"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               hovermode="closest",
                               height=1500
                               )
            }
        ),

    ]),

    html.Details([
        html.Summary("North West Details"),
        html.H1("North West Data"),
                html.P("This includes areas such as Blackpool, Liverpool, Manchester"),

        html.Br(),
        dash_table.DataTable(
            id="north_west_table",

            columns=[{'id': c, 'name': c} for c in nw_data.columns],
            data=nw_data.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="single",
            pagination_settings={
                "current_page": 0,
                "page_size": 5,
            },
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
        dcc.Graph(
            id='nw_graph',
            figure={
                'data': [
                    {'x': nw_data["Year"],
                     'y': nw_data["IndicatorFigures"], 'type': 'bar',
                     'text': nw_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': nw_data["IndicatorName"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"),
                     }
                ],
                'layout': dict(title='North West England Younger People Data',autosize=True,
                               xaxis={'title': "Years"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=2500,
                               hovermode="closest")
            }
        ),

    ]),

    html.Details([
        html.Summary("South East Details"),
        html.H1("South East Data"),
                html.P("This includes areas such as Kent, Milton Keynes, Reading"),

        html.Br(),
        dash_table.DataTable(
            id="south_east_table",
            columns=[{'id': c, 'name': c} for c in se_data.columns],
            data=se_data.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="single",
            pagination_settings={
                "current_page": 0,
                "page_size": 5,
            },
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
        dcc.Graph(
            id='se_graph',
            figure={
                'data': [
                    {'x': se_data["Year"],
                     'y': se_data["IndicatorFigures"], 'type': 'bar',
                     'text': se_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': se_data["IndicatorName"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"
                                              ),
                     }
                ],
                'layout': dict(title='South East Younger People Data', autosize=True,
                               xaxis={'title': "Years"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=2500,
                               hovermode="closest")
            }
        ),

    ]),

    html.Details([
        html.Summary("South West Details"),
        html.H1("South West Data"),
                html.P("This includes areas such as Bournemouth, Swindon, Torbay"),

        html.Br(),
        dash_table.DataTable(
            id="south_west_table",
            columns=[{'id': c, 'name': c} for c in sw_data.columns],
            data=sw_data.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="single",
            pagination_settings={
                "current_page": 0,
                "page_size": 5,
            },
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
        dcc.Graph(
            id='south_west_graph',
            figure={
                'data': [
                    {'x': sw_data["Year"],
                     'y': sw_data["IndicatorFigures"], 'type': 'bar',
                     'text': sw_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': sw_data["IndicatorName"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"),
                     }
                ],
                'layout': dict(title='South West Younger People Data', autosize=True,
                               xaxis={'title': "Years"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=1500,
                               hovermode="closest")
            }
        ),

    ]),

    html.Details([
        html.Summary("West Midlands Details"),
        html.H1("West Midlands Data"),
                html.P("This includes areas such as Coventry, Solihull, Wolverhamton"),

        html.Br(),
        dash_table.DataTable(
            id="west_midlands_table",
            columns=[{'id': c, 'name': c} for c in west_mid_data.columns],
            data=west_mid_data.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="single",
            pagination_settings={
                "current_page": 0,
                "page_size": 5,
            },
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

        dcc.Graph(
            id='west_mid_graph',
            figure={
                'data': [
                    {'x': west_mid_data["Year"],
                     'y': west_mid_data["IndicatorFigures"], 'type': 'bar',
                     'text': west_mid_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': west_mid_data["IndicatorName"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"),
                     }
                ],
                'layout': dict(title='West Midlands Younger People Data', autosize=True,
                               xaxis={'title': "Years"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               hovermode="closest",
                               height=1500)
            }
        ),

    ]),

    html.Details([
        html.Summary("Yorkshire & The Humber Details"),
        html.H1("Yorkshire & The Humber Data"),
        html.Br(),
        dash_table.DataTable(
            id="yorkshire_table",
            columns=[{'id': c, 'name': c} for c in yorkshire_data.columns],
            data=yorkshire_data.to_dict('records'),
            filtering=True,
            sorting=True,
            sorting_type="single",
            pagination_settings={
                "current_page": 0,
                "page_size": 5,
            },
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

        dcc.Graph(
            id='yorkshire_graph',
            figure={
                'data': [
                    {'x': yorkshire_data["Year"],
                     'y': yorkshire_data["IndicatorFigures"], 'type': 'bar',
                     'text': yorkshire_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': yorkshire_data["IndicatorName"],
                     'marker': dict(color="rgb(255,165,0)",
                                              width=2),
                     }
                ],
                'layout': dict(title='Yorkshire Younger People Data', autosize=True,
                               xaxis={'title': "Years"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=1500,
                               hovermode="closest")
            }
        ),

    ]),

    html.Div(id='younger_content'),

])

