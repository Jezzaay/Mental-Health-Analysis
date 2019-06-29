import pandas as pd

# 1997 - 2017 gdhi data
# gross disposable household income from Office of National Statistics

gdhi = pd.read_csv("data/gdhireferencetables.csv", skipinitialspace=True)
gdhi.columns = gdhi.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

gdhi = gdhi.drop(["nuts_level", "nuts_code"], axis=1)

gdhi = gdhi.dropna(thresh=1) # if more than one NaN then delete
