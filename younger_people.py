
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
from gdhi_file import gdhi

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
                  "Lower_CI_95.0_limit", "Value", "Count", "Denominator"]



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

# Removing England from AreaName and ParentName as unsure where these figures are actually from

# .size().reset_index() allows to count the number of same in the first column e.g. IndicatorName, counts these figures.

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

print(all_data)


all = all_data.groupby(["Timeperiod", "AreaName"]).size().reset_index()
all.columns = ["Year", "AreaName", "IndicatorFigures"]

all1718= all[all["Year"] == "2017/18"]
all1718 = all1718.groupby([ "AreaName", "IndicatorFigures"]).size().reset_index()
all1718.columns =  ["AreaName" ,"Figure_Amount", "IndicatorFigures"]


#England With London
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


# GDHI
fig, ax = plt.subplots()
london_brent = gdhi[(gdhi.region_name == "Brent")]
london_Enfield = gdhi[(gdhi.region_name == "Enfield")]
london_Westminster = gdhi[(gdhi.region_name == "Westminster")]
london_Lambeth = gdhi[(gdhi.region_name == "Lambeth")]
london_figures = london.groupby(["Timeperiod", "AreaName"]).size().reset_index()
london_figures.columns =  ["Year", "AreaName", "IndicatorFigures"]
brent_figures = london_figures[(london_figures.AreaName == "Brent")]
Enfield_figures = london_figures[(london_figures.AreaName == "Enfield")]
Westminster_figures = london_figures[(london_figures.AreaName == "Westminster")]
Lambeth_figures = london_figures[(london_figures.AreaName == "Lambeth")]



ax.bar(london_brent["region_name"], london_brent["2015"], label="GDHI")
ax.bar(london_Enfield["region_name"], london_Enfield["2015"], label="GDHI" )
ax.bar(london_Westminster["region_name"], london_Westminster["2015"], label="GDHI" )
ax.bar(london_Lambeth["region_name"], london_Lambeth["2015"], label="GDHI" )
ax.plot(brent_figures["AreaName"],  brent_figures["IndicatorFigures"], 'bs' )
ax.plot(Enfield_figures["AreaName"],  Enfield_figures["IndicatorFigures"], 'bs'  )
ax.plot(Westminster_figures["AreaName"],  Westminster_figures["IndicatorFigures"], 'bs'  )
ax.plot(Lambeth_figures["AreaName"],  Lambeth_figures["IndicatorFigures"], 'bs'  )

plt.ylabel("Amount of £ GDHI and amount of mental health reports in blue")
plt.xlabel("Cities")
plt.title("London in 2015 with GDHI and Amount of Mental Health In Younger People")


total_london = london_figures.groupby(["Year", "IndicatorFigures"]).size().reset_index()
total_london.columns =  ["Year", "Figure_Amount", "IndicatorFigures"]
plt.scatter(total_london["Year"], total_london["Figure_Amount"])
plt.title("The amount of mental health indicator figures per year In London")
plt.xlabel("Year")
plt.ylabel("Figure Amount")

#East Mid
east_mid = east_mid[east_mid != "England"]
east_mid_data = east_mid.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
east_mid_data.columns = ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]

#GHDI
fig, ax = plt.subplots()

eastmid_figures = east_mid.groupby(["Timeperiod", "AreaName"]).size().reset_index()
eastmid_figures.columns =  ["Year", "AreaName", "IndicatorFigures"]

eastmid_Derby = gdhi[(gdhi.region_name == "Derby")]
Derby_figures = eastmid_figures[(eastmid_figures.AreaName == "Derby")]
eastmid_Nottingham = gdhi[(gdhi.region_name == "Nottingham")]
Nottingham_figures = eastmid_figures[(eastmid_figures.AreaName == "Nottingham")]
eastmid_Leicester = gdhi[(gdhi.region_name == "Leicester")]
Leicester_figures = eastmid_figures[(eastmid_figures.AreaName == "Leicester")]

ax.bar(eastmid_Derby["region_name"], eastmid_Derby["2015"], label="GDHI")
ax.plot(Derby_figures["AreaName"],  Derby_figures["IndicatorFigures"], 'bs'  )
ax.bar(eastmid_Nottingham["region_name"], eastmid_Nottingham["2015"], label="GDHI")
ax.plot(Nottingham_figures["AreaName"],  Nottingham_figures["IndicatorFigures"], 'bs'  )
ax.bar(eastmid_Leicester["region_name"], eastmid_Leicester["2015"], label="GDHI")
ax.plot(Leicester_figures["AreaName"],  Leicester_figures["IndicatorFigures"], 'bs'  )

plt.ylabel("Amount of £ GDHI and amount of mental health reports in blue")
plt.xlabel("Cities")
plt.title("East Midlands in 2015 with GDHI and Amount of Mental Health In Younger People")
#East England
east_england = east_england[east_england!= "England"]
east_england_data = east_england.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
east_england_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]

#GHDI
fig, ax = plt.subplots()

eastengland_figures = east_england.groupby(["Timeperiod", "AreaName"]).size().reset_index()
eastengland_figures.columns =  ["Year", "AreaName", "IndicatorFigures"]

east_Luton = gdhi[(gdhi.region_name == "Luton")]
Luton_figures = eastengland_figures[(eastengland_figures.AreaName == "Luton")]
east_Bedford = gdhi[(gdhi.region_name == "Bedford")]
Bedford_figures = eastengland_figures[(eastengland_figures.AreaName == "Bedford")]
east_Peterborough = gdhi[(gdhi.region_name == "Peterborough")]
Peterborough_figures = eastengland_figures[(eastengland_figures.AreaName == "Peterborough")]

ax.bar(east_Luton["region_name"], east_Luton["2015"], label="GDHI")
ax.plot(Luton_figures["AreaName"],  Luton_figures["IndicatorFigures"], 'bs'  )
ax.bar(east_Bedford["region_name"], east_Bedford["2015"], label="GDHI")
ax.plot(Bedford_figures["AreaName"],  Bedford_figures["IndicatorFigures"], 'bs'  )
ax.bar(east_Peterborough["region_name"], east_Peterborough["2015"], label="GDHI")
ax.plot(Peterborough_figures["AreaName"],  Peterborough_figures["IndicatorFigures"], 'bs'  )

plt.ylabel("Amount of £ GDHI and amount of mental health reports in blue")
plt.xlabel("Cities")
plt.title("East of England in 2015 with GDHI and Amount of Mental Health In Younger People")

#North East
north_east = north_east[north_east!= "England"]
ne_data = north_east.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
ne_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]


#GDHI
fig, ax = plt.subplots()
north_east_figures = north_east.groupby(["Timeperiod", "AreaName"]).size().reset_index()
north_east_figures.columns =  ["Year", "AreaName", "IndicatorFigures"]
ne_sunderland = gdhi[(gdhi.region_name == "Sunderland")]
sunderland_figures = north_east_figures[(north_east_figures.AreaName == "Sunderland")]
ne_darlington = gdhi[(gdhi.region_name  == "Darlington")]
darlington_figures = north_east_figures[(north_east_figures.AreaName == "Darlington")]
ax.bar(ne_sunderland["region_name"], ne_sunderland["2015"], label="GDHI")
ax.bar(ne_darlington["region_name"], ne_darlington["2015"], label="GDHI" )
ax.plot(sunderland_figures["AreaName"],  sunderland_figures["IndicatorFigures"], 'bs' )
ax.plot(darlington_figures["AreaName"],  darlington_figures["IndicatorFigures"], 'bs'  )


plt.ylabel("Amount of £ GDHI and amount of mental health reports in blue")
plt.xlabel("Cities")
plt.title("North East in 2015 with GDHI and Amount of Mental Health In Younger People")
#ax.legend(loc="best", numpoints = 1)


total_ne = north_east_figures.groupby(["Year", "IndicatorFigures"]).size().reset_index()
total_ne.columns =  ["Year", "Figure_Amount", "IndicatorFigures"]
plt.scatter(total_ne["Year"], total_ne["Figure_Amount"])
plt.title("The amount of mental health indicator figures per year in North East")
plt.xlabel("Year")
plt.ylabel("Figure Amount")


#North West
north_west = north_west[north_west!= "England"]
nw_data = north_west.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
nw_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]

#GDHI
fig, ax = plt.subplots()
north_west_figures = north_west.groupby(["Timeperiod", "AreaName"]).size().reset_index()
north_west_figures.columns =  ["Year", "AreaName", "IndicatorFigures"]
nw_Manchester = gdhi[(gdhi.region_name == "Manchester")]
Manchester_figures = north_west_figures[(north_west_figures.AreaName == "Manchester")]
nw_Liverpool = gdhi[(gdhi.region_name  == "Liverpool")]
Liverpool_figures = north_west_figures[(north_west_figures.AreaName == "Liverpool")]
nw_Blackpool = gdhi[(gdhi.region_name == "Blackpool")]
Blackpool_figures = north_east_figures[(north_east_figures.AreaName == "Blackpool")]
ax.bar(nw_Manchester["region_name"], nw_Manchester["2015"], label="GDHI")
ax.bar(nw_Liverpool["region_name"], nw_Liverpool["2015"], label="GDHI" )
ax.bar(nw_Blackpool["region_name"], nw_Blackpool["2015"], label="GDHI" )
ax.plot(Manchester_figures["AreaName"],  Manchester_figures["IndicatorFigures"], 'bs' )
ax.plot(Liverpool_figures["AreaName"],  Liverpool_figures["IndicatorFigures"], 'bs'  )
ax.plot(Blackpool_figures["AreaName"],  Blackpool_figures["IndicatorFigures"], 'bs'  )


plt.ylabel("Amount of £ GDHI and amount of mental health reports in blue")
plt.xlabel("Cities")
plt.title("North West in 2015 with GDHI and Amount of Mental Health In Younger People")


#South West
south_west = south_west[south_east!= "England"]
sw_data = south_west.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
sw_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]

#GDHI
fig, ax = plt.subplots()
sw_figures = south_west.groupby(["Timeperiod", "AreaName"]).size().reset_index()
sw_figures.columns =  ["Year", "AreaName", "IndicatorFigures"]
sw_Swindon = gdhi[(gdhi.region_name == "Swindon")]
Swindon_figures = sw_figures[(sw_figures.AreaName == "Swindon")]
sw_Plymouth = gdhi[(gdhi.region_name  == "Plymouth")]
Plymouth_figures = sw_figures[(sw_figures.AreaName == "Plymouth")]
sw_Torbay = gdhi[(gdhi.region_name == "Torbay")]
Torbay_figures = sw_figures[(sw_figures.AreaName == "Torbay")]
ax.bar(sw_Swindon["region_name"], sw_Swindon["2015"], label="GDHI")
ax.bar(sw_Plymouth["region_name"], sw_Plymouth["2015"], label="GDHI" )
ax.bar(sw_Torbay["region_name"], sw_Torbay["2015"], label="GDHI" )
ax.plot(Swindon_figures["AreaName"],  Swindon_figures["IndicatorFigures"], 'bs' )
ax.plot(Plymouth_figures["AreaName"],  Plymouth_figures["IndicatorFigures"], 'bs'  )
ax.plot(Torbay_figures["AreaName"],  Torbay_figures["IndicatorFigures"], 'bs'  )

plt.ylabel("Amount of £ GDHI and amount of mental health reports in blue")
plt.xlabel("Cities")
plt.title("South West in 2015 with GDHI and Amount of Mental Health In Younger People")


#South East
south_east = south_east[south_east!= "England"]
se_data = south_east.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
se_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]

#GDHI
fig, ax = plt.subplots()
se_figures = south_east.groupby(["Timeperiod", "AreaName"]).size().reset_index()
se_figures.columns =  ["Year", "AreaName", "IndicatorFigures"]
se_MiltonKeynes = gdhi[(gdhi.region_name == "Milton Keynes")]
MiltonKeynes_figures = se_figures[(se_figures.AreaName == "Milton Keynes")]
se_Portsmouth = gdhi[(gdhi.region_name  == "Portsmouth")]
Portsmouth_figures = se_figures[(se_figures.AreaName == "Portsmouth")]
se_Berkshire = gdhi[(gdhi.region_name == "Berkshire")]
Berkshire_figures = se_figures[(se_figures.AreaName == "Berkshire")]
ax.bar(se_MiltonKeynes["region_name"], se_MiltonKeynes["2015"], label="GDHI")
ax.bar(se_Portsmouth["region_name"], se_Portsmouth["2015"], label="GDHI" )
ax.bar(se_Berkshire["region_name"], se_Berkshire["2015"], label="GDHI" )
ax.plot(MiltonKeynes_figures["AreaName"],  MiltonKeynes_figures["IndicatorFigures"], 'bs' )
ax.plot(Portsmouth_figures["AreaName"],  Portsmouth_figures["IndicatorFigures"], 'bs'  )
ax.plot(Berkshire_figures["AreaName"],  Berkshire_figures["IndicatorFigures"], 'bs'  )

plt.ylabel("Amount of £ GDHI and amount of mental health reports in blue")
plt.xlabel("Cities")
plt.title("South East in 2015 with GDHI and Amount of Mental Health In Younger People")



#West Mid
west_midlands = west_midlands[west_midlands!= "England"]
west_mid_data = west_midlands.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
west_mid_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]


#GDHI
fig, ax = plt.subplots()
westmid = west_midlands.groupby(["Timeperiod", "AreaName"]).size().reset_index()
westmid.columns =  ["Year", "AreaName", "IndicatorFigures"]
wmBirmingham = gdhi[(gdhi.region_name == "Birmingham")]
Birmingham_figures = westmid[(westmid.AreaName == "Birmingham")]
wmCoventry = gdhi[(gdhi.region_name  == "Coventry")]
Coventry_figures = westmid[(westmid.AreaName == "Coventry")]
wmStokeonTrent = gdhi[(gdhi.region_name == "Stoke-on-Trent")]
StokeonTrent_figures = westmid[(westmid.AreaName == "Stoke-on-Trent")]
ax.bar(wmBirmingham["region_name"], wmBirmingham["2015"], label="GDHI")
ax.bar(wmCoventry["region_name"], wmCoventry["2015"], label="GDHI" )
ax.bar(wmStokeonTrent["region_name"], wmStokeonTrent["2015"], label="GDHI" )
ax.plot(Birmingham_figures["AreaName"],  Birmingham_figures["IndicatorFigures"], 'bs' )
ax.plot(Coventry_figures["AreaName"],  Coventry_figures["IndicatorFigures"], 'bs'  )
ax.plot(StokeonTrent_figures["AreaName"],  StokeonTrent_figures["IndicatorFigures"], 'bs'  )

plt.ylabel("Amount of £ GDHI and amount of mental health reports in blue")
plt.xlabel("Cities")
plt.title("West Midlands in 2015 with GDHI and Amount of Mental Health In Younger People")



#Yorkshire
yorkshire = yorkshire[yorkshire!= "England"]
yorkshire_data = yorkshire.groupby(["IndicatorName", "Timeperiod", "AreaName"]).size().reset_index()
yorkshire_data.columns =  ["IndicatorName", "Year", "AreaName", "IndicatorFigures"]


#GDHI
fig, ax = plt.subplots()
yorkshire_figures = yorkshire.groupby(["Timeperiod", "AreaName"]).size().reset_index()
yorkshire_figures.columns =  ["Year", "AreaName", "IndicatorFigures"]
yorkYork = gdhi[(gdhi.region_name == "York")]
York_figures = yorkshire_figures[(yorkshire_figures.AreaName == "York")]
yorkSheffield = gdhi[(gdhi.region_name  == "Sheffield")]
Sheffield_figures = yorkshire_figures[(yorkshire_figures.AreaName == "Sheffield")]
yorkLeeds = gdhi[(gdhi.region_name == "Leeds")]
Leeds_figures = yorkshire_figures[(yorkshire_figures.AreaName == "Leeds")]
ax.bar(yorkYork["region_name"], yorkYork["2015"], label="GDHI")
ax.bar(yorkSheffield["region_name"], yorkSheffield["2015"], label="GDHI" )
ax.bar(yorkLeeds["region_name"], yorkLeeds["2015"], label="GDHI" )
ax.plot(York_figures["AreaName"],  York_figures["IndicatorFigures"], 'bs' )
ax.plot(Sheffield_figures["AreaName"],  Sheffield_figures["IndicatorFigures"], 'bs'  )
ax.plot(Leeds_figures["AreaName"],  Leeds_figures["IndicatorFigures"], 'bs'  )

plt.ylabel("Amount of £ GDHI and amount of mental health reports in blue")
plt.xlabel("Cities")
plt.title("Yorkshire in 2015 with GDHI and Amount of Mental Health In Younger People")



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
                    'x': all1718["AreaName"],
                    'y': all1718["Figure_Amount"],
                    'type': 'bar',
                    'name': "Mental Health Figures",

                },
            ],
            'layout': dict(title='England in 2017/2018 with GDHI and Amount of Mental Health In Younger People',
                           autosize=True,
                           xaxis={'title': "Cities"},
                           yaxis={'title': "Amount of £ GDHI and amount of mental health reports in orange)"},
                           hovermode="compare",
                           height=1500,

                           )
        }
    ),


    html.Details([ # Details allows to hide sections in the page until clicked.
        html.Summary("England Data"),



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

        html.P("Two Graphs showing Data for England. One displaying data including London and one without. "
               "The reason for this is to show the data that London may contain majority of the data. Therefore,"
               "the data being shown can be more accurate and can give the viewer a better outlook on the data. "),
        html.Br(),

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

