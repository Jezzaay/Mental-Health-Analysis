import pandas as pd


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



# 2017 house prices data
# Gov.uk  to compare with GDHI
# https://www.gov.uk/government/statistical-data-sets/uk-house-price-index-data-downloads-august-2017

houseprices = pd.read_csv("data/UK-HPI-full-file-2017-08.csv", skipinitialspace=True)

houseprices = houseprices.drop(["AreaCode", "Index", "IndexSA","1m%Change","12m%Change","AveragePriceSA","SalesVolume","DetachedPrice","DetachedIndex","Detached1m%Change","Detached12m%Change",
                         "SemiDetachedPrice","SemiDetachedIndex","SemiDetached1m%Change","SemiDetached12m%Change","TerracedPrice","TerracedIndex","Terraced1m%Change",
                               "Terraced12m%Change","FlatPrice","FlatIndex","Flat1m%Change","Flat12m%Change","CashPrice","CashIndex","Cash1m%Change","Cash12m%Change","CashSalesVolume",
                        "MortgagePrice","MortgageIndex","Mortgage1m%Change","Mortgage12m%Change","MortgageSalesVolume","FTBPrice","FTBIndex","FTB1m%Change","FTB12m%Change","FOOPrice",
                          "FOOIndex","FOO1m%Change","FOO12m%Change","NewPrice","NewIndex","New1m%Change","New12m%Change","NewSalesVolume","OldPrice","OldIndex","Old1m%Change","Old12m%Change","OldSalesVolume"], axis=1)

houseprices.columns = houseprices.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

hp_date = houseprices[houseprices.date.str.contains("08/2017")]
houseprices["date"] = hp_date
houseprices = houseprices[houseprices["date"].notnull()]



houseprices = houseprices[~houseprices.regionname.str.contains("North") &
                       ~houseprices.regionname.str.contains("South") &
                       ~houseprices.regionname.str.contains("shire") &
                        ~houseprices.regionname.str.contains("County") ]




#houseprices["date"]  = houseprices[houseprices["date"].isin(pd.date_range(start_date,end_date))]


print(houseprices)
