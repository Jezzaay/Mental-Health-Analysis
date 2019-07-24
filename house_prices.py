import pandas as pd


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:.2f}'.format)


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

houseprices_younger = houseprices
houseprices_suicides = houseprices

# have to remove all of these so the plot matches up with the GDHI files.
houseprices_younger = houseprices[~houseprices.regionname.str.contains("North") &
                       ~houseprices.regionname.str.contains("South") &
                       ~houseprices.regionname.str.contains("shire") &
                       ~houseprices.regionname.str.contains("mid") &
                        ~houseprices.regionname.str.contains("County") &
                        ~houseprices.regionname.str.contains("Greater*") &
                         ~houseprices.regionname.str.contains("West") &
                       ~houseprices.regionname.str.contains("Mid") &
                       ~houseprices.regionname.str.contains("East") &
                       ~houseprices.regionname.str.contains("Swansea") &
                       ~houseprices.regionname.str.contains("Islands") &
                       ~houseprices.regionname.str.contains("United Kingdom") &
                          ~houseprices.regionname.str.contains("Great Britain") &
                          ~houseprices.regionname.str.contains("City") &
                       ~houseprices.regionname.str.contains("Isles") &
                       ~houseprices.regionname.str.contains("Swansea") &
                       ~houseprices.regionname.str.contains("Cardiff") &
                       ~houseprices.regionname.str.contains("Powys") &
                       ~houseprices.regionname.str.contains("Scotland") &
                       ~houseprices.regionname.str.contains("Inverness") &
                       ~houseprices.regionname.str.contains("Caithness") &
                       ~houseprices.regionname.str.contains("Siar") &
                       ~houseprices.regionname.str.contains("Edinburgh") &
                       ~houseprices.regionname.str.contains("Lochaber") &
                       ~houseprices.regionname.str.contains("Falkirk") &
                       ~houseprices.regionname.str.contains("Perth") &
                       ~houseprices.regionname.str.contains("Glasgow") &
                       ~houseprices.regionname.str.contains("Scottish") &
                       ~houseprices.regionname.str.contains("Gwent") &
                       ~houseprices.regionname.str.contains("Dumfries") &
                       ~houseprices.regionname.str.contains("Belfast") &
                       ~houseprices.regionname.str.contains("Banbridge") &
                       ~houseprices.regionname.str.contains("Newry") &
                       ~houseprices.regionname.str.contains("Fermanagh") &
                       ~houseprices.regionname.str.contains("Causeway") &
                       ~houseprices.regionname.str.contains("Newtownabbey") &
                       ~houseprices.regionname.str.contains("Antrim") &
                       ~houseprices.regionname.str.contains("Lisburn") &
                       ~houseprices.regionname.str.contains("CC") &
                       ~houseprices.regionname.str.contains("Valleys") &
                       ~houseprices.regionname.str.contains("Wales") &
                       ~houseprices.regionname.str.contains("Gwynedd") &
                       ~houseprices.regionname.str.contains("Bridgend") &
                       ~houseprices.regionname.str.contains("Gateway") &
                       ~houseprices.regionname.str.contains("Heart") &
                       ~houseprices.regionname.str.contains("Ashfield") &
                       ~houseprices.regionname.str.contains("Basingstoke") &
                       ~houseprices.regionname.str.contains("Brentwood") &
                       ~houseprices.regionname.str.contains("Burnley") &
                       ~houseprices.regionname.str.contains("Cambridge") &
                       ~houseprices.regionname.str.contains("Cae") &
                       ~houseprices.regionname.str.contains("-") &
                       ~houseprices.regionname.str.contains("St") &
                       ~houseprices.regionname.str.contains("High")&
                       ~houseprices.regionname.str.contains("Fife") &
                       ~houseprices.regionname.str.contains("Forest") &
                       ~houseprices.regionname.str.contains("Exeter") &
                       ~houseprices.regionname.str.contains("Fareham") &
                       ~houseprices.regionname.str.contains("Ere") &
                       ~houseprices.regionname.str.contains("Hyndburn") &
                       ~houseprices.regionname.str.contains("Inner") &
                       ~houseprices.regionname.str.contains("Newark") &
                       ~houseprices.regionname.str.contains("New")&
                       ~houseprices.regionname.str.contains("Ashfield") &
                       ~houseprices.regionname.str.contains("Rush") &
                       ~houseprices.regionname.str.contains("Valley") &
                       ~houseprices.regionname.str.contains("Rhondda") &
                       ~houseprices.regionname.str.contains("Redcar") &
                       ~houseprices.regionname.str.contains("Pur") &
                       ~houseprices.regionname.str.contains("Inv") &
                       ~houseprices.regionname.str.contains("Boston") &
                       ~houseprices.regionname.str.contains("Epping")&
                       ~houseprices.regionname.str.contains("Fy") &
                       ~houseprices.regionname.str.contains("church") &
                       ~houseprices.regionname.str.contains("Gates") &
                       ~houseprices.regionname.str.contains("Great") &
                       ~houseprices.regionname.str.contains("Herts") &
                       ~houseprices.regionname.str.contains("Hinckley")&
                       ~houseprices.regionname.str.contains("Tend") &
                       ~houseprices.regionname.str.contains("Suffolk Coastal") &
                       ~houseprices.regionname.str.contains("Twek") &
                       ~houseprices.regionname.str.contains("Tonbridge") &
                       ~houseprices.regionname.str.contains("River") &
                       ~houseprices.regionname.str.contains("Vale")&
                       ~houseprices.regionname.str.contains("Har") &
                       ~houseprices.regionname.str.contains("Dart") &
                       ~houseprices.regionname.str.contains("Glou") &
                       ~houseprices.regionname.str.contains("Lin") &
                       ~houseprices.regionname.str.contains("Outer") &
                       ~houseprices.regionname.str.contains("Preston")&
                       ~houseprices.regionname.str.contains("Wind") &
                       ~houseprices.regionname.str.contains("Cope") &
                       ~houseprices.regionname.str.contains("Con") &
                       ~houseprices.regionname.str.contains("Brox") &
                       ~houseprices.regionname.str.contains("Bo") &
                       ~houseprices.regionname.str.contains("Bab") &
                       ~houseprices.regionname.str.contains("Lew") &
                       ~houseprices.regionname.str.contains("Gos") &
                       ~houseprices.regionname.str.contains("Fen") &
                       ~houseprices.regionname.str.contains("Elm") &
                       ~houseprices.regionname.str.contains("Kett") &
                          ~houseprices.regionname.str.contains("Read") &
                          ~houseprices.regionname.str.contains("Rei") &
                          ~houseprices.regionname.str.contains("Maid") &
                          ~houseprices.regionname.str.contains("Gild") &
                          ~houseprices.regionname.str.contains("Ham") &
                       ~houseprices.regionname.str.contains("Al") &
                       ~houseprices.regionname.str.contains("Bas") &
                          ~houseprices.regionname.str.contains("Co") &
                          ~houseprices.regionname.str.contains("Ch") &
                          ~houseprices.regionname.str.contains("Ca") &
                          ~houseprices.regionname.str.contains("Ash") &
                          ~houseprices.regionname.str.contains("Ips")&
                          ~houseprices.regionname.str.contains("Me") &
                          ~houseprices.regionname.str.contains("Nune") &
                          ~houseprices.regionname.str.contains("Sal") &
                          ~houseprices.regionname.str.contains("Se") &
                          ~houseprices.regionname.str.contains("Swa") &
                          ~houseprices.regionname.str.contains("Tew") &
                          ~houseprices.regionname.str.contains("Wat")&
                          ~houseprices.regionname.str.contains("Wea") &
                          ~houseprices.regionname.str.contains("Wo") &
                          ~houseprices.regionname.str.contains("Wy") &
                          ~houseprices.regionname.str.contains("Wr") &
                          ~houseprices.regionname.str.contains("Wi") &
                          ~houseprices.regionname.str.contains("Wey") &
                          ~houseprices.regionname.str.contains("Wel")&
                          ~houseprices.regionname.str.contains("Utt") &
                          ~houseprices.regionname.str.contains("Tor")  &
                          ~houseprices.regionname.str.contains("Sheo") &
                          ~houseprices.regionname.str.contains("Scar") &
                          ~houseprices.regionname.str.contains("Pen") &
                          ~houseprices.regionname.str.contains("Dover") &
                          ~houseprices.regionname.str.contains("Guildford")&
                          ~houseprices.regionname.str.contains("Norwich") &
                          ~houseprices.regionname.str.contains("Oadby") &
                          ~houseprices.regionname.str.contains("Craven") &
                          ~houseprices.regionname.str.contains("Brain") &
                          ~houseprices.regionname.str.contains("Arg") &
                          ~houseprices.regionname.str.contains("Angus") &
                          ~houseprices.regionname.str.contains("Arun")&
                          ~houseprices.regionname.str.contains("Bla") &
                          ~houseprices.regionname.str.contains("Broadland") &
                          ~houseprices.regionname.str.contains("Daco") &
                          ~houseprices.regionname.str.contains("Ged") &
                          ~houseprices.regionname.str.contains("Hal") &
                          ~houseprices.regionname.str.contains("Hast") &
                          ~houseprices.regionname.str.contains("Graves")&
                          ~houseprices.regionname.str.contains("Know") &
                          ~houseprices.regionname.str.contains("Moray") &
                          ~houseprices.regionname.str.contains("Redd") &
                          ~houseprices.regionname.str.contains("Roch") &
                          ~houseprices.regionname.str.contains("Rother") &
                          ~houseprices.regionname.str.contains("Rugby") &
                          ~houseprices.regionname.str.contains("Runnymede")&
                          ~houseprices.regionname.str.contains("Spel") &
                          ~houseprices.regionname.str.contains("Slou") &
                          ~houseprices.regionname.str.contains("Oldham") &
                          ~houseprices.regionname.str.contains("Epsom") &
                          ~houseprices.regionname.str.contains("Eden") &
                          ~houseprices.regionname.str.contains("Horsham") &
                          ~houseprices.regionname.str.contains("Hav")&
                          ~houseprices.regionname.str.contains("Tam") &
                          ~houseprices.regionname.str.contains("Surrey") &
                          ~houseprices.regionname.str.contains("Bromsgrove") &
                          ~houseprices.regionname.str.contains("Breck") &
                          ~houseprices.regionname.str.contains("Daventry") &
                          ~houseprices.regionname.str.contains("Bury") &
                          ~houseprices.regionname.str.contains("Lichfield")&
                          ~houseprices.regionname.str.contains("Mans") &
                          ~houseprices.regionname.str.contains("Malvern") &
                          ~houseprices.regionname.str.contains("Neath") &
                          ~houseprices.regionname.str.contains("Oxford") &
                          ~houseprices.regionname.str.contains("Adur") &
                          ~houseprices.regionname.str.contains("Maldon") &
                          ~houseprices.regionname.str.contains("Poole")&
                          ~houseprices.regionname.str.contains("Ryedale") &
                          ~houseprices.regionname.str.contains("Rossendale") &
                          ~houseprices.regionname.str.contains("Waverley") &
                          ~houseprices.regionname.str.contains("Waveney") &
                          ~houseprices.regionname.str.contains("Trafford") &
                          ~houseprices.regionname.str.contains("Taunton") &
                          ~houseprices.regionname.str.contains("Thanet")&
                          ~houseprices.regionname.str.contains("Teignbridge") &
                          ~houseprices.regionname.str.contains("Shepway") &
                          ~houseprices.regionname.str.contains("Tandridge") &
                          ~houseprices.regionname.str.contains("Ceredigion") &
                          ~houseprices.regionname.str.contains("Crawley") &
                          ~houseprices.regionname.str.contains("Warwick") &
                          ~houseprices.regionname.str.contains("England")




]



houseprices_suicides = houseprices[~houseprices.regionname.str.contains("North") &
            ~houseprices.regionname.str.contains("South") &
                       ~houseprices.regionname.str.contains("shire") &
                       ~houseprices.regionname.str.contains("mid") &
                        ~houseprices.regionname.str.contains("County") &
                        ~houseprices.regionname.str.contains("Greater*") &
                         ~houseprices.regionname.str.contains("West") &
                       ~houseprices.regionname.str.contains("Mid") &
                       ~houseprices.regionname.str.contains("East") &
                       ~houseprices.regionname.str.contains("Swansea") &
                       ~houseprices.regionname.str.contains("Islands") &
                       ~houseprices.regionname.str.contains("United Kingdom") &
                      ~houseprices.regionname.str.contains("Great Britain") &
                          ~houseprices.regionname.str.contains("City") &
                       ~houseprices.regionname.str.contains("Isles") &
                       ~houseprices.regionname.str.contains("Swansea") &
                       ~houseprices.regionname.str.contains("Cardiff") &
                       ~houseprices.regionname.str.contains("Powys") &
                       ~houseprices.regionname.str.contains("Scotland") &
                       ~houseprices.regionname.str.contains("Inverness") &
                       ~houseprices.regionname.str.contains("Caithness") &
                       ~houseprices.regionname.str.contains("Siar") &
                       ~houseprices.regionname.str.contains("Edinburgh") &
                       ~houseprices.regionname.str.contains("Lochaber") &
                       ~houseprices.regionname.str.contains("Falkirk") &
                       ~houseprices.regionname.str.contains("Perth") &
                       ~houseprices.regionname.str.contains("Glasgow") &
                       ~houseprices.regionname.str.contains("Scottish") &
                       ~houseprices.regionname.str.contains("Gwent") &
                       ~houseprices.regionname.str.contains("Dumfries") &
                       ~houseprices.regionname.str.contains("Belfast") &
                       ~houseprices.regionname.str.contains("Banbridge") &
                       ~houseprices.regionname.str.contains("Newry") &
                       ~houseprices.regionname.str.contains("Fermanagh") &
                       ~houseprices.regionname.str.contains("Causeway") &
                       ~houseprices.regionname.str.contains("Newtownabbey") &
                       ~houseprices.regionname.str.contains("Antrim") &
                       ~houseprices.regionname.str.contains("Lisburn") &
                       ~houseprices.regionname.str.contains("CC") &
                       ~houseprices.regionname.str.contains("Valleys") &
                       ~houseprices.regionname.str.contains("Wales") &
                       ~houseprices.regionname.str.contains("Gwynedd") &
                       ~houseprices.regionname.str.contains("Bridgend")  &
                       ~houseprices.regionname.str.contains("Adur") &
                       ~houseprices.regionname.str.contains("Amber") &
                       ~houseprices.regionname.str.contains("Anug") &
                       ~houseprices.regionname.str.contains("Argyll") &
                       ~houseprices.regionname.str.contains("Arun") &
                       ~houseprices.regionname.str.contains("Ash") &
                       ~houseprices.regionname.str.contains("Aylesbury") &
                       ~houseprices.regionname.str.contains("Babergh") &
                       ~houseprices.regionname.str.contains("-") &
                       ~houseprices.regionname.str.contains("Basildon") &
                       ~houseprices.regionname.str.contains("Basingstoke") &
                       ~houseprices.regionname.str.contains("Bassetlaw") &
                       ~houseprices.regionname.str.contains("Blaby") &
                       ~houseprices.regionname.str.contains("Bolsover") &
                       ~houseprices.regionname.str.contains("Bolton") &
                       ~houseprices.regionname.str.contains("Boston") &
                       ~houseprices.regionname.str.contains("Forest") &
                       ~houseprices.regionname.str.contains("Braintree") &
                       ~houseprices.regionname.str.contains("Breckland") &
                       ~houseprices.regionname.str.contains("Brentwood") &
                       ~houseprices.regionname.str.contains("Broadland")  &
                       ~houseprices.regionname.str.contains("Broxtowe") &
                       ~houseprices.regionname.str.contains("Bury") &
                       ~houseprices.regionname.str.contains("Burnley") &
                       ~houseprices.regionname.str.contains("Caephily") &
                       ~houseprices.regionname.str.contains("Chase") &
                       ~houseprices.regionname.str.contains("Cambridge") &
                       ~houseprices.regionname.str.contains("Canterbury")  &
                       ~houseprices.regionname.str.contains("Carlisle") &
                       ~houseprices.regionname.str.contains("Castle") &
                       ~houseprices.regionname.str.contains("Ceredigion") &
                       ~houseprices.regionname.str.contains("Charnwood") &
                       ~houseprices.regionname.str.contains("Chermsford") &
                       ~houseprices.regionname.str.contains("Cheltenham") &
                       ~houseprices.regionname.str.contains("Cherwell")  &
                       ~houseprices.regionname.str.contains("Chesterfield") &
                       ~houseprices.regionname.str.contains("Chichester") &
                       ~houseprices.regionname.str.contains("Chiltern") &
                       ~houseprices.regionname.str.contains("Chorley") &
                       ~houseprices.regionname.str.contains("Christchurch") &
                       ~houseprices.regionname.str.contains("Colchester") &
                       ~houseprices.regionname.str.contains("Conwry")  &
                       ~houseprices.regionname.str.contains("Copeland") &
                       ~houseprices.regionname.str.contains("Corby") &
                       ~houseprices.regionname.str.contains("Cotswold") &
                       ~houseprices.regionname.str.contains("Craven") &
                       ~houseprices.regionname.str.contains("Crawley") &
                       ~houseprices.regionname.str.contains("Dacorum") &
                       ~houseprices.regionname.str.contains("Dartford")  &
                       ~houseprices.regionname.str.contains("Daventry") &
                       ~houseprices.regionname.str.contains("Eden") &
                       ~houseprices.regionname.str.contains("Elmbridge") &
                       ~houseprices.regionname.str.contains("Epsom") &
                       ~houseprices.regionname.str.contains("Erewash") &
                       ~houseprices.regionname.str.contains("Exeter") &
                       ~houseprices.regionname.str.contains("Fareham")  &
                       ~houseprices.regionname.str.contains("Fenland") &
                       ~houseprices.regionname.str.contains("Fife") &
                       ~houseprices.regionname.str.contains("Fylde") &
                       ~houseprices.regionname.str.contains("Gateshead") &
                       ~houseprices.regionname.str.contains("Gedling") &
                       ~houseprices.regionname.str.contains("Gloucester") &
                       ~houseprices.regionname.str.contains("Gosport")  &
                       ~houseprices.regionname.str.contains("Gravesham") &
                       ~houseprices.regionname.str.contains("Great") &
                       ~houseprices.regionname.str.contains("Guildford") &
                       ~houseprices.regionname.str.contains("Halton") &
                       ~houseprices.regionname.str.contains("Hambleton") &
                       ~houseprices.regionname.str.contains("Harlow") &
                       ~houseprices.regionname.str.contains("Harrogate")  &
                       ~houseprices.regionname.str.contains("Hart") &
                       ~houseprices.regionname.str.contains("Hast") &
                       ~houseprices.regionname.str.contains("Hertsmere") &
                       ~houseprices.regionname.str.contains("Highland") &
                       ~houseprices.regionname.str.contains("Ipswich") &
                       ~houseprices.regionname.str.contains("Kettering") &
                       ~houseprices.regionname.str.contains("Hinckley")  &
                       ~houseprices.regionname.str.contains("Angus") &
                       ~houseprices.regionname.str.contains("Bromsgrove") &
                       ~houseprices.regionname.str.contains("Broxbourne") &
                       ~houseprices.regionname.str.contains("Caerphilly") &
                       ~houseprices.regionname.str.contains("Chelmsford") &
                       ~houseprices.regionname.str.contains("Conwy") &
                       ~houseprices.regionname.str.contains("Dover") &
                       ~houseprices.regionname.str.contains("Harborough") &
                       ~houseprices.regionname.str.contains("Havant") &
                       ~houseprices.regionname.str.contains("High") &
                       ~houseprices.regionname.str.contains("Horsham") &
                       ~houseprices.regionname.str.contains("Hyndburn") &
                       ~houseprices.regionname.str.contains("Inner") &
                       ~houseprices.regionname.str.contains("Inverclyde") &
                       ~houseprices.regionname.str.contains("Maldon") &
                       ~houseprices.regionname.str.contains("Lincoln") &
                       ~houseprices.regionname.str.contains("Maidstone") &
                       ~houseprices.regionname.str.contains("Lichfield") &
                       ~houseprices.regionname.str.contains("Lewes") &
                       ~houseprices.regionname.str.contains("Knowsley") &
                       ~houseprices.regionname.str.contains("Kensington")  &
                       ~houseprices.regionname.str.contains("Hills") &
                       ~houseprices.regionname.str.contains("Mansfield") &
                       ~houseprices.regionname.str.contains("Mendip") &
                       ~houseprices.regionname.str.contains("Merthyr") &
                       ~houseprices.regionname.str.contains("Moray") &
                       ~houseprices.regionname.str.contains("Neath") &
                       ~houseprices.regionname.str.contains("Newark")  &
                       ~houseprices.regionname.str.contains("Newport") &
                       ~houseprices.regionname.str.contains("Newcastle") &
                       ~houseprices.regionname.str.contains("Norwich") &
                       ~houseprices.regionname.str.contains("Nuneaton") &
                       ~houseprices.regionname.str.contains("Oadby") &
                       ~houseprices.regionname.str.contains("Oldham") &
                       ~houseprices.regionname.str.contains("Oxford")  &
                       ~houseprices.regionname.str.contains("Poole") &
                       ~houseprices.regionname.str.contains("Preston") &
                       ~houseprices.regionname.str.contains("Purbeck") &
                       ~houseprices.regionname.str.contains("Reading") &
                       ~houseprices.regionname.str.contains("Recar") &
                       ~houseprices.regionname.str.contains("Redd") &
                       ~houseprices.regionname.str.contains("Rhondda")  &
                       ~houseprices.regionname.str.contains("Ribble") &
                       ~houseprices.regionname.str.contains("Rochdale") &
                       ~houseprices.regionname.str.contains("Rochford") &
                       ~houseprices.regionname.str.contains("Rossendale") &
                       ~houseprices.regionname.str.contains("Rother") &
                       ~houseprices.regionname.str.contains("Runnymede") &
                       ~houseprices.regionname.str.contains("Rugby")  &
                       ~houseprices.regionname.str.contains("Allerdale") &
                       ~houseprices.regionname.str.contains("Melton") &
                       ~houseprices.regionname.str.contains("Valley") &
                       ~houseprices.regionname.str.contains("Outer") &
                       ~houseprices.regionname.str.contains("Pendle") &
                       ~houseprices.regionname.str.contains("Redcar") &
                       ~houseprices.regionname.str.contains("Reigate")  &
                       ~houseprices.regionname.str.contains("Rushcliffe") &
                       ~houseprices.regionname.str.contains("Rushmoor") &
                       ~houseprices.regionname.str.contains("Ryedale") &
                       ~houseprices.regionname.str.contains("Salford") &
                       ~houseprices.regionname.str.contains("Scarborough") &
                       ~houseprices.regionname.str.contains("Sedgemoor") &
                       ~houseprices.regionname.str.contains("Selby")  &
                       ~houseprices.regionname.str.contains("Sevenoaks") &
                       ~houseprices.regionname.str.contains("Shepway") &
                       ~houseprices.regionname.str.contains("Slough") &
                       ~houseprices.regionname.str.contains("Spelthorne") &
                       ~houseprices.regionname.str.contains("St") &
                       ~houseprices.regionname.str.contains("Stafford") &
                       ~houseprices.regionname.str.contains("Stevenage")  &
                       ~houseprices.regionname.str.contains("Sitrling") &
                       ~houseprices.regionname.str.contains("Stockport") &
                       ~houseprices.regionname.str.contains("Stroud") &
                       ~houseprices.regionname.str.contains("Swale") &
                       ~houseprices.regionname.str.contains("Surrey") &
                       ~houseprices.regionname.str.contains("Suffolk")   &
                       ~houseprices.regionname.str.contains("Tam") &
                       ~houseprices.regionname.str.contains("Tonridge") &
                       ~houseprices.regionname.str.contains("Taunton") &
                       ~houseprices.regionname.str.contains("Three") &
                       ~houseprices.regionname.str.contains("Vale") &
                       ~houseprices.regionname.str.contains("Watford") &
                       ~houseprices.regionname.str.contains("Warwick")  &
                       ~houseprices.regionname.str.contains("Waveney") &
                       ~houseprices.regionname.str.contains("Waverley") &
                       ~houseprices.regionname.str.contains("Wealden") &
                       ~houseprices.regionname.str.contains("Wigan") &
                       ~houseprices.regionname.str.contains("Winchester") &
                       ~houseprices.regionname.str.contains("Weymouth") &
                       ~houseprices.regionname.str.contains("Welwyn")  &
                       ~houseprices.regionname.str.contains("Wellingborough") &
                       ~houseprices.regionname.str.contains("Thanet") &
                       ~houseprices.regionname.str.contains("Teignbridge") &
                       ~houseprices.regionname.str.contains("Tendring") &
                       ~houseprices.regionname.str.contains("Tyne") &
                       ~houseprices.regionname.str.contains("Uttlesford") &
                       ~houseprices.regionname.str.contains("Tan")  &
                       ~houseprices.regionname.str.contains("Tewk") &
                       ~houseprices.regionname.str.contains("Tonbridge") &
                       ~houseprices.regionname.str.contains("Tunbridge") &
                       ~houseprices.regionname.str.contains("Woking") &
                       ~houseprices.regionname.str.contains("Wor") &
                       ~houseprices.regionname.str.contains("Wrexham") &
                       ~houseprices.regionname.str.contains("Wyc")  &
                       ~houseprices.regionname.str.contains("Torfaen") &
                       ~houseprices.regionname.str.contains("Windsor") &
                       ~houseprices.regionname.str.contains("Trafford")  &
                       ~houseprices.regionname.str.contains("Torridge")




]







