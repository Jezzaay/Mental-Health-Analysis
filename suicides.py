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
from plotly.tools import mpl_to_plotly

from app import  app
from gdhi_file import gdhi
from house_prices import  houseprices_suicides

#import csv
london = pd.read_csv('data/suicides/indicators-CountyUA.data london.csv')
east_mid = pd.read_csv("data/suicides/indicators-CountyUA.data east midlands.csv")
east_england = pd.read_csv("data/suicides/indicators-CountyUA.data east of england.csv")
north_east = pd.read_csv("data/suicides/indicators-CountyUA.data north east.csv")
north_west = pd.read_csv("data/suicides/indicators-CountyUA.data north west.csv")
south_west = pd.read_csv("data/suicides/indicators-CountyUA.data south west.csv")
south_east = pd.read_csv("data/suicides/indicators-CountyUA.data south east.csv")
west_midlands = pd.read_csv("data/suicides/indicators-CountyUA.data west midlands.csv")
yorkshire = pd.read_csv("data/suicides/indicators-CountyUA.data yorkshire.csv")


#drop Columns
tables_to_drop = ["IndicatorID",   "AreaCode",  "AreaType",
                      "Recent_Trend", "Category_Type", "Value_note",
                                                "Time_period_Sortable", "Category",   "Upper_CI_99.8_limit",
                      "Upper_CI_95.0_limit", "Lower_CI_99.8_limit",
                                                "New_data", "Compared_to_goal",
                  "Compared_to_England_value_or_percentiles","Compared_to_Region_value_or_percentiles"]




london = london.drop(tables_to_drop, axis = 1)
east_mid = east_mid.drop(tables_to_drop, axis = 1)
east_england = east_england.drop(tables_to_drop, axis = 1)
north_east = north_east.drop(tables_to_drop, axis = 1)
north_west = north_west.drop(tables_to_drop, axis = 1)
south_west = south_west.drop(tables_to_drop, axis = 1)
south_east = south_east.drop(tables_to_drop, axis = 1)
west_midlands = west_midlands.drop(tables_to_drop, axis = 1)
yorkshire = yorkshire.drop(tables_to_drop, axis = 1)

#Clearing data which is not cities
east_mid = east_mid[~east_mid.AreaName.str.contains("East") &
                            ~east_mid.AreaName.str.contains("shire")]

east_england = east_england[~east_england.AreaName.str.contains("East") &
                            ~east_england.AreaName.str.contains("shire")]

london = london[~london.AreaName.str.contains("East") &
                            ~london.AreaName.str.contains("shire") &
                            ~london.AreaName.str.contains("England")&
                            ~london.AreaName.str.contains("City")    ]

north_east = north_east[~north_east.AreaName.str.contains("North") &
                        ~north_east.AreaName.str.contains("South") &
                            ~north_east.AreaName.str.contains("shire")&
                        ~north_east.AreaName.str.contains("County") ]


north_west = north_west[~north_west.AreaName.str.contains("North") &
                        ~north_west.AreaName.str.contains("South") &
                            ~north_west.AreaName.str.contains("shire")&
                        ~north_west.AreaName.str.contains("East") ]


south_west = south_west[~south_west.AreaName.str.contains("North") &
                        ~south_west.AreaName.str.contains("South") &
                            ~south_west.AreaName.str.contains("shire")&
                        ~south_west.AreaName.str.contains("East") &
                        ~south_west.AreaName.str.contains("England") ]


south_east = south_east[~south_east.AreaName.str.contains("North") &
                        ~south_east.AreaName.str.contains("South") &
                            ~south_east.AreaName.str.contains("shire")&
                        ~south_east.AreaName.str.contains("East") &
                        ~south_east.AreaName.str.contains("England")&
                        ~south_east.AreaName.str.contains("West")]

west_midlands = west_midlands[~west_midlands.AreaName.str.contains("North") &
                        ~west_midlands.AreaName.str.contains("South") &
                            ~west_midlands.AreaName.str.contains("shire")&
                        ~west_midlands.AreaName.str.contains("East") &
                        ~west_midlands.AreaName.str.contains("England")&
                        ~west_midlands.AreaName.str.contains("West")]

yorkshire = yorkshire[~yorkshire.AreaName.str.contains("North") &
                        ~yorkshire.AreaName.str.contains("South") &
                            ~yorkshire.AreaName.str.contains("shire")&
                        ~yorkshire.AreaName.str.contains("East") &
                        ~yorkshire.AreaName.str.contains("England")&
                        ~yorkshire.AreaName.str.contains("West")]



#rename Persons to Unknown Sex

london["Sex"] = london["Sex"].replace({'Persons':'Unknown'})
east_mid["Sex"] = east_mid["Sex"].replace({'Persons':'Unknown'})
east_england["Sex"] = east_england["Sex"].replace({'Persons':'Unknown'})
north_east["Sex"] = north_east["Sex"].replace({'Persons':'Unknown'})
north_west["Sex"] = north_west["Sex"].replace({'Persons':'Unknown'})
south_west["Sex"] = south_west["Sex"].replace({'Persons':'Unknown'})
south_east["Sex"] = south_east["Sex"].replace({'Persons':'Unknown'})
south_east["Sex"] = south_east["Sex"].replace({'Persons':'Unknown'})
west_midlands["Sex"] = west_midlands["Sex"].replace({'Persons':'Unknown'})
yorkshire["Sex"] = yorkshire["Sex"].replace({'Persons':'Unknown'})



data_join = [london, east_mid, east_england, north_east, north_west,
             south_west, south_east, west_midlands, yorkshire]

all_data =  pd.concat(data_join)

#All of England
all_data =  pd.concat(data_join)
all_data = all_data[all_data.AreaName != "England"]
all_data = all_data[all_data.ParentName != "England"]



all_data = all_data[~all_data.AreaName.str.contains("Greater*")]
all_data = all_data[~all_data.AreaName.str.contains("West")]
all_data = all_data[~all_data.AreaName.str.contains("East")]
all_data = all_data[~all_data.AreaName.str.contains("North")]
all_data = all_data[~all_data.AreaName.str.contains("South")]
all_data = all_data[~all_data.AreaName.str.contains("Islands")]
all_data = all_data[~all_data.AreaName.str.contains("shire")]
all_data = all_data[~all_data.AreaName.str.contains("United Kingdom")]

all = all_data.groupby(["Timeperiod", "AreaName"]).size().reset_index()
all.columns = ["Year", "AreaName", "IndicatorFigures"]
all1517= all[all["Year"] == "2015 - 17"]
all1517 = all1517.groupby([ "AreaName", "IndicatorFigures"]).size().reset_index()
all1517.columns =  ["AreaName" ,"Figure_Amount", "IndicatorFigures"]

#England With London
england = all_data.groupby(["IndicatorName", "Age", "Timeperiod", "ParentName"]).size().reset_index()
england.columns = ["IndicatorName", "Age",  "Year", "Region", "IndicatorFigures"]

# Islington & Sunderland
islsund =  [london, north_east]
islsund = pd.concat(islsund)
islsund = islsund[islsund.AreaName.str.contains("Islington") | islsund.AreaName.str.contains("Sunderland")]
islsund = islsund.groupby(["IndicatorName", "Age",  "Sex", "AreaName" ]).size().reset_index()
islsund.columns = ["IndicatorName", "Age",  "Sex", "AreaName", "IndicatorFigures"]


#England WO London
eng_wo_london = [east_mid, east_england, north_east, north_west,
             south_west, south_east, west_midlands, yorkshire]
england_wo_london = pd.concat(eng_wo_london)
england_wo_london = england_wo_london[england_wo_london.AreaName != "England"]
england_wo_london = england_wo_london[england_wo_london.ParentName != "England"]
england_wo_london = england_wo_london.groupby(["IndicatorName", "Age",  "Timeperiod", "ParentName" ]).size().reset_index()
england_wo_london.columns = ["IndicatorName", "Age",  "Year", "Region", "IndicatorFigures"]

# England Region Count
england_reg = all_data.groupby(["ParentName", "Timeperiod"]).size().reset_index()
england_reg.columns = ["Region", "Year", "Figures"]


#London Data
london= london[london.AreaName  != "England"]

london_data = london.groupby(["IndicatorName", "Sex" ,"Age","AreaName"]).size().reset_index()
london_data.columns = ["IndicatorName", "Sex" ,"Age","AreaName", "IndicatorFigures"]

#East Mid
east_mid = east_mid[east_mid != "England"]
east_mid_data = east_mid.groupby(["IndicatorName","Sex" ,"Age","AreaName"]).size().reset_index()
east_mid_data.columns = ["IndicatorName", "Sex" ,"Age", "AreaName", "IndicatorFigures"]


#East England
east_england = east_england[east_england!= "England"]
east_england_data = east_england.groupby(["IndicatorName","Sex" ,"Age", "AreaName"]).size().reset_index()
east_england_data.columns =  ["IndicatorName", "Sex" ,"Age", "AreaName", "IndicatorFigures"]


#North East
north_east = north_east[north_east!= "England"]
ne_data = north_east.groupby(["IndicatorName", "Sex" ,"Age", "AreaName"]).size().reset_index()
ne_data.columns =  ["IndicatorName", "Sex" ,"Age", "AreaName", "IndicatorFigures"]




#North West
north_west = north_west[north_west!= "England"]
nw_data = north_west.groupby(["IndicatorName", "Sex" ,"Age","AreaName"]).size().reset_index()
nw_data.columns =  ["IndicatorName","Sex" ,"Age","AreaName", "IndicatorFigures"]

#South West
south_west = south_west[south_east!= "England"]
sw_data = south_west.groupby(["IndicatorName", "Sex" ,"Age", "AreaName"]).size().reset_index()
sw_data.columns =  ["IndicatorName", "Sex" ,"Age", "AreaName", "IndicatorFigures"]



#South East
south_east = south_east[south_east!= "England"]
se_data = south_east.groupby(["IndicatorName", "Sex" ,"Age", "AreaName"]).size().reset_index()
se_data.columns =  ["IndicatorName", "Sex" ,"Age","AreaName", "IndicatorFigures"]



#West Mid
west_midlands = west_midlands[west_midlands!= "England"]
west_mid_data = west_midlands.groupby(["IndicatorName", "Sex" ,"Age", "AreaName"]).size().reset_index()
west_mid_data.columns =  ["IndicatorName", "Sex" ,"Age","AreaName", "IndicatorFigures"]



#Yorkshire
yorkshire = yorkshire[yorkshire!= "England"]
yorkshire_data = yorkshire.groupby(["IndicatorName", "Sex" ,"Age", "AreaName"]).size().reset_index()
yorkshire_data.columns =  ["IndicatorName", "Sex", "Age", "AreaName", "IndicatorFigures"]

print(islsund)

#grouped islington sunderland
grpislsund = go.Figure()
Ages = ["10-34 yrs", "35-64 yrs", "65+ yrs", "10+ yrs", "15-74 yrs"]

grpislsund.layout.update(
    title="Islington x Sunderland Suicides"
)


grpislsund.add_trace(go.Bar(
    x = Ages,
    y = [1,1,1,1,1],
    name =  "Sunderland"
))

grpislsund.add_trace(go.Bar(
    x = Ages,
    y = [1,1,1,1,1],
    name =  "Islington"
))


#nested pie
islsundpie =[ go.Pie(values=islsund["IndicatorFigures"],
                    labels=islsund["Age"],
                    hole = 0.5,
                    direction = 'clockwise',
                    ),
            go.Pie(values=islsund["IndicatorFigures"],
                   labels=islsund["AreaName"],
                   hole=0.9,
                   direction = 'clockwise',
)
              ]



suicides_layout = html.Div([




    html.H1('Suicide Analysis', id="title"),
    html.P("Suicide analysise comparing different regions of England"),
    dcc.Graph(  # two csv files + bar charts
        id='all_graph_gdhi',
        figure={
            'data': [
                {'x': gdhi["region_name"],
                 'y': gdhi["2017"],
                 'type': 'bar',
                 'hovertext': gdhi["region_name"],
                 'name': "Gross disposable Household Income ",
                 },
                {
                  'x': houseprices_suicides["regionname"],
                  'y': houseprices_suicides["averageprice"],
                    'type':'bar',
                    'hovertext': houseprices_suicides["regionname"],
                    'name':"2017 House Prices for England"
                },
            ],
            'layout': dict(title='England in 2017 Gross Disposable HouseHold income  & House prices',
                           autosize=True,
                           xaxis={'title': "Cities"},
                           yaxis={'title': "Amount of £ "},
                           hovermode="compare",
                           height=1500,

                           )
        }
    ),

        html.Details([
            html.Summary("England Data"),

            html.Br(),

            # Dash datatable to display to users
            dash_table.DataTable(
                id="all_data",
                columns=[{'id': c, 'name': c} for c in england.columns],
                data=england.to_dict('records'),
                filtering=True,  # Allows users to filter
                sorting=True,
                sorting_type="single",  # Only one column can be sorted at a time
                pagination_settings={  # how many are shown at once
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

            html.P("Two Graphs showing Data for England. One displaying data including London and one without. "
                   "The reason for this is to show the data that London may contain majority of the data. Therefore,"
                   "the data being shown can be more accurate and can give the viewer a better outlook on the data. "),
            html.Br(),


            html.Details([
                html.Summary("Graphs Comparing suicide rates with and without london "),
            html.Div([

                html.P(
                    "Bar Plot for England Data without London. As London is massive it is important to show the England "
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
                        'layout': dict(title='England Suicide Data (Without London)', autosize=True,
                                       barmode="stack",
                                       xaxis={'title': "Years"},
                                       yaxis={'title': "Indicator Figures (Total Figures for Year)",
                                              'range': [0, 300]},
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
                        'layout': dict(title='England Suicide Data (Including London) ', autosize=True,
                                       barmode="stack",
                                       xaxis={'title': "Years"},
                                       yaxis={'title': "Indicator Figures (Total Figures for Year)",
                                              'range': [0, 400]},
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
                        'layout': dict(title='England Region Figures For Suicide Data', autosize=True,
                                       barmode="stack",
                                       xaxis={'title': "Years"},
                                       yaxis={'title': "Indicator Figures (Total Figures for Year)",
                                              'range': [0, 400]},
                                       height=2500,
                                       hovermode="closest"
                                       )
                    }
                ),

            ]),
            ]),
        ]),

    html.Details([
        html.Summary("Comparison of Islington and Sunderland"),
        html.H1("Islington & Sunderland"),
        html.Br(),
        dash_table.DataTable(
            id="islsund_table",
            columns=[{'id': c, 'name': c} for c in islsund.columns],
            data=islsund.to_dict('records'),
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
            figure=go.Figure(data=grpislsund)
        ),

        dcc.Graph(
            figure=go.Figure(data=islsundpie, layout={'title': 'Islington x Sunderland Suicides'})
        ),

    ]),


    html.Div([
    html.Details([
        html.Summary("East Midlands Details"),
        html.Br(),
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
            id='east_mid_graph',
            figure={
                'data': [
                    {'x': east_mid_data["Age"],
                     'y': east_mid_data["IndicatorFigures"], 'type': 'bar',
                     'text': east_mid_data["AreaName"],
                     'textposition': "inside",
                     'hovertext':"Indicator Name : "+ east_mid_data["IndicatorName"] +  "<br>" +  "Sex:" + east_mid_data["Sex"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"
                                    ),
                     }
                ],
                'layout': dict(title='East Midlands Suicide Data', autosize=True, barmode="stack",
                               xaxis={'title': "Ages"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=1200,
                               hovermode="closest"
                               )
            }
        ),

        dcc.Graph(id='east_mid_pie',
                  figure={
                      'data': [go.Pie(labels=east_mid_data["Age"],
                                      values=east_mid_data["IndicatorFigures"],
                                      marker=dict(line=dict(color='#fff', width=1)),
                                      hoverinfo='label+ value+percent', textinfo='value + percent',
                                      domain={'x': [0, .75], 'y': [0, 1]}
                                      )
                               ],
                      'layout': go.Layout(title='East Midlands Suicide Plot',
                                          autosize=True, height=500
                                          )
                  }),

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
                    {'x': east_england_data["Age"],
                     'y': east_england_data["IndicatorFigures"], 'type': 'bar',
                     'text': east_england_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': "Indicator Name : "+ east_england_data["IndicatorName"] +  "<br>" +  "Sex:" + east_england_data["Sex"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"),
                     }
                ],
                'layout': dict(title='East of England Suicide Data', autosize=True, barmode="group",
                               xaxis={'title': "Ages"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=1500,
                               hovermode="closest")
            }
        ),

        dcc.Graph(
            id='east_england_pie',
            figure={
                'data': [
                    {'x': east_england_data["Age"],
                     'y': east_england_data["IndicatorFigures"],
                     'text': east_england_data["AreaName"],
                     'textposition': "inside",
                     'type': 'pie',
                     'hovertext': "Indicator Name : " + east_england_data["IndicatorName"] + "<br>" + "Sex:" +
                                  east_england_data["Sex"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"),
                     }
                ],
                'layout': dict(title='East of England Suicide Data', autosize=True, barmode="group",
                               xaxis={'title': "Ages"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=1500,
                               hovermode="closest")
            }
        ),

        dcc.Graph(id='east_england_pie',
                  figure={
                      'data': [go.Pie(labels=east_england_data["Age"],
                                      values=east_england_data["IndicatorFigures"],
                                      marker=dict(line=dict(color='#fff', width=1)),
                                      hoverinfo='label+ value+percent', textinfo='value + percent',
                                      domain={'x': [0, .75], 'y': [0,1]}
                                      )
                               ],
                      'layout': go.Layout(title='East of England Suicide Data',
                                          autosize=True, height = 500
                                          )
                  }),

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
            id='london_graph',
            figure={
                'data': [
                    {'x': london_data["Age"],
                     'y': london_data["IndicatorFigures"], 'type': 'bar',
                     'text': london_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': "Indicator Name : "+ london_data["IndicatorName"] +  "<br>" +  "Sex:" + london_data["Sex"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"),
                     }
                ],
                'layout': dict(title='London Suicide Data', autosize=True,
                               xaxis={'title': "Ages"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                              # height=2500,
                               hovermode="closest")
            }
        ),

        dcc.Graph(id='london_pie',
                  figure={
                      'data': [go.Pie(labels=london_data["Age"],
                                      values=london_data["IndicatorFigures"],
                                      marker=dict(line=dict(color='#fff', width=1)),
                                      hoverinfo='label+ value+percent', textinfo='value + percent',
                                      domain={'x': [0, .75], 'y': [0, 1]}
                                      )
                               ],
                      'layout': go.Layout(title='London Suicide Plot',
                                          autosize=True, height=500
                                          )
                  }),



        html.Div(id="london_container")
    ]),



    html.Details([
        html.Summary("North East Details"),
        html.Br(),

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
                    {'x': ne_data["Age"],
                     'y': ne_data["IndicatorFigures"], 'type': 'bar',
                     'text': ne_data["AreaName"],
                     'textposition': "inside",
                     'hovertext':"Indicator Name : "+ ne_data["IndicatorName"] +  "<br>" +  "Sex:" + ne_data["Sex"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"),
                     }
                ],
                'layout': dict(title='North East England Suicide People Data', autosize=True,
                               xaxis={'title': "Ages"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               hovermode="closest",
                               height=1500
                               )
            }
        ),

        dcc.Graph(id='ne_pie',
                  figure={
                      'data': [go.Pie(labels=ne_data["Age"],
                                      values=ne_data["IndicatorFigures"],
                                      marker=dict(line=dict(color='#fff', width=1)),
                                      hoverinfo='label+ value+percent', textinfo='value + percent',
                                      domain={'x': [0, .75], 'y': [0, 1]}
                                      )
                               ],
                      'layout': go.Layout(title='North East Suicide Plot',
                                          autosize=True, height=500
                                          )
                  }),

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
                    {'x': nw_data["Age"],
                     'y': nw_data["IndicatorFigures"], 'type': 'bar',
                     'text': nw_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': "Indicator Name : "+ nw_data["IndicatorName"] +  "<br>" +  "Sex:" + nw_data["Sex"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"),
                     }
                ],
                'layout': dict(title='North West England Suicide Data', autosize=True,
                               xaxis={'title': "Ages"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=2500,
                               hovermode="closest")
            }
        ),

        dcc.Graph(id='nw_pie',
                  figure={
                      'data': [go.Pie(labels=nw_data["Age"],
                                      values=nw_data["IndicatorFigures"],
                                      marker=dict(line=dict(color='#fff', width=1)),
                                      hoverinfo='label+ value+percent', textinfo='value + percent',
                                      domain={'x': [0, .75], 'y': [0, 1]}
                                      )
                               ],
                      'layout': go.Layout(title='North West Suicide Plot',
                                          autosize=True, height=500
                                          )
                  }),
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
                    {'x': se_data["Age"],
                     'y': se_data["IndicatorFigures"], 'type': 'bar',
                     'text': se_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': "Indicator Name : "+ se_data["IndicatorName"] +  "<br>" +  "Sex:" + se_data["Sex"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"
                                    ),
                     }
                ],
                'layout': dict(title='South East Suicide Data', autosize=True,
                               xaxis={'title': "Ages"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=2500,
                               hovermode="closest")
            }
        ),

        dcc.Graph(id='se_pie',
                  figure={
                      'data': [go.Pie(labels=se_data["Age"],
                                      values=se_data["IndicatorFigures"],
                                      marker=dict(line=dict(color='#fff', width=1)),
                                      hoverinfo='label+ value+percent', textinfo='value + percent',
                                      domain={'x': [0, .75], 'y': [0, 1]}
                                      )
                               ],
                      'layout': go.Layout(title='South East Suicide Plot',
                                          autosize=True, height=500
                                          )
                  }),
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
                    {'x': sw_data["Age"],
                     'y': sw_data["IndicatorFigures"], 'type': 'bar',
                     'text': sw_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': "Indicator Name : "+ sw_data["IndicatorName"] +  "<br>" +  "Sex:" + sw_data["Sex"],
                     'opacity': 0.8,
                     'marker': dict(color="rgb(255,165,0)"),
                     }
                ],
                'layout': dict(title='South West Suicide Data', autosize=True,
                               xaxis={'title': "Ages"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=1500,
                               hovermode="closest")
            }
        ),

        dcc.Graph(id='sw_pie',
                  figure={
                      'data': [go.Pie(labels=sw_data["Age"],
                                      values=sw_data["IndicatorFigures"],
                                      marker=dict(line=dict(color='#fff', width=1)),
                                      hoverinfo='label+ value+percent', textinfo='value + percent',
                                      domain={'x': [0, .75], 'y': [0, 1]}
                                      )
                               ],
                      'layout': go.Layout(title='South West Suicide Plot',
                                          autosize=True, height=500
                                          )
                  }),


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
                        {'x': west_mid_data["Age"],
                         'y': west_mid_data["IndicatorFigures"], 'type': 'bar',
                         'text': west_mid_data["AreaName"],
                         'textposition': "inside",
                         'hovertext': "Indicator Name : "+ west_mid_data["IndicatorName"] +  "<br>" +  "Sex:" + west_mid_data["Sex"],
                         'opacity': 0.8,
                         'marker': dict(color="rgb(255,165,0)"),
                         }
                    ],
                    'layout': dict(title='West Midlands Suicide Data', autosize=True,
                                   xaxis={'title': "Ages"},
                                   yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                                   hovermode="closest",
                                   height=1500)
                }
            ),

            dcc.Graph(id='westmid_pie',
                      figure={
                          'data': [go.Pie(labels=west_mid_data["Age"],
                                          values=west_mid_data["IndicatorFigures"],
                                          marker=dict(line=dict(color='#fff', width=1)),
                                          hoverinfo='label+ value+percent', textinfo='value + percent',
                                          domain={'x': [0, .75], 'y': [0, 1]}
                                          )
                                   ],
                          'layout': go.Layout(title='West Midlands Suicide Plot',
                                              autosize=True, height=500
                                              )
                      }),

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
                    {'x': yorkshire_data["Age"],
                     'y': yorkshire_data["IndicatorFigures"], 'type': 'bar',
                     'text': yorkshire_data["AreaName"],
                     'textposition': "inside",
                     'hovertext': "Indicator Name : "+ yorkshire_data["IndicatorName"] +  "<br>" +  "Sex:" + yorkshire_data["Sex"],
                     'marker': dict(color="rgb(255,165,0)",
                                    width=2),
                     }
                ],
                'layout': dict(title='Yorkshire Suicide Data', autosize=True,
                               xaxis={'title': "Ages"},
                               yaxis={'title': "Indicator Figures (Total Figures for Year)"},
                               height=1500,
                               hovermode="closest")
            }
        ),

        dcc.Graph(id='york_pie',
                  figure={
                      'data': [go.Pie(labels=yorkshire_data["Age"],
                                      values=yorkshire_data["IndicatorFigures"],
                                      marker=dict(line=dict(color='#fff', width=1)),
                                      hoverinfo='label+ value+percent', textinfo='value + percent',
                                      domain={'x': [0, .75], 'y': [0, 1]}
                                      )
                               ],
                      'layout': go.Layout(title='South West Suicide Plot',
                                          autosize=True, height=500
                                          )
                  }),

    ]),
        html.Div(id='suicides-content'),

]),

])




def display_value(value):
    return 'You have selected "{}"'.format(value)
