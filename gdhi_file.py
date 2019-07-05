import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# 1997 - 2017 gdhi data
# gross disposable household income from Office of National Statistics

gdhi = pd.read_csv("data/gdhireferencetables.csv", skipinitialspace=True)
gdhi.columns = gdhi.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

gdhi = gdhi.drop(["nuts_level", "nuts_code"], axis=1)

gdhi = gdhi.dropna(thresh=1) # if more than one NaN then delete




#Clearing data which is not cities
gdhi = gdhi[~gdhi.region_name.str.contains("Greater*")]
gdhi = gdhi[~gdhi.region_name.str.contains("West")]
gdhi = gdhi[~gdhi.region_name.str.contains("East")]
gdhi = gdhi[~gdhi.region_name.str.contains("North")]
gdhi = gdhi[~gdhi.region_name.str.contains("South")]
gdhi = gdhi[~gdhi.region_name.str.contains("Islands")]
gdhi = gdhi[~gdhi.region_name.str.contains("shire")]
gdhi = gdhi[~gdhi.region_name.str.contains("United Kingdom")]
gdhi = gdhi[~gdhi.region_name.str.contains("Isles")]
gdhi = gdhi[~gdhi.region_name.str.contains("City")]


#Clearing non England
gdhi = gdhi[~gdhi.region_name.str.contains("Swansea")]
gdhi = gdhi[~gdhi.region_name.str.contains("Cardiff")]
gdhi = gdhi[~gdhi.region_name.str.contains("Powys")]
gdhi = gdhi[~gdhi.region_name.str.contains("Scotland")]
gdhi = gdhi[~gdhi.region_name.str.contains("Caithness")]
gdhi = gdhi[~gdhi.region_name.str.contains("Inverness")]
gdhi = gdhi[~gdhi.region_name.str.contains("Siar")]
gdhi = gdhi[~gdhi.region_name.str.contains("Lochaber")]
gdhi = gdhi[~gdhi.region_name.str.contains("Edinburgh")]
gdhi = gdhi[~gdhi.region_name.str.contains("Falkirk")]
gdhi = gdhi[~gdhi.region_name.str.contains("Perth")]
gdhi = gdhi[~gdhi.region_name.str.contains("Glasgow")]
gdhi = gdhi[~gdhi.region_name.str.contains("Scottish")]
gdhi = gdhi[~gdhi.region_name.str.contains("Gwent")]
gdhi = gdhi[~gdhi.region_name.str.contains("Dumfries")]
gdhi = gdhi[~gdhi.region_name.str.contains("Belfast")]
gdhi = gdhi[~gdhi.region_name.str.contains("Banbridge")]
gdhi = gdhi[~gdhi.region_name.str.contains("Newry")]
gdhi = gdhi[~gdhi.region_name.str.contains("Mid")]
gdhi = gdhi[~gdhi.region_name.str.contains("Causeway")]
gdhi = gdhi[~gdhi.region_name.str.contains("Newtownabbey")]
gdhi = gdhi[~gdhi.region_name.str.contains("Fermanagh")]
gdhi = gdhi[~gdhi.region_name.str.contains("Antrim")]
gdhi = gdhi[~gdhi.region_name.str.contains("Lisburn")]
gdhi = gdhi[~gdhi.region_name.str.contains("Antrim")]
gdhi = gdhi[~gdhi.region_name.str.contains("Valleys")]
gdhi = gdhi[~gdhi.region_name.str.contains("CC")]
gdhi = gdhi[~gdhi.region_name.str.contains("Wales")]
gdhi = gdhi[~gdhi.region_name.str.contains("Gwynedd")]
gdhi = gdhi[~gdhi.region_name.str.contains("Bridgend")]
gdhi = gdhi[~gdhi.region_name.str.contains("Gateway")]
gdhi = gdhi[~gdhi.region_name.str.contains("Heart")]





