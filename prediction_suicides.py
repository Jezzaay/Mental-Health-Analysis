import  suicides
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import sklearn
import pandas as pd

# Coding Phases
# younger people (yp) + initials of city
# e.g. ld for london or ne for north east
# suicides (sds)


drop = ["AreaName", "IndicatorName", "Sex"]


# As I have been encountering a RMSE and R2 score of 0.0 and 1.0 for all the training/test apart from the England W.o London


# ------- LONDON --------


lnd = suicides.london_data
lnd = lnd.drop(drop, axis=1)
lnd["Age"] = lnd['Age'].str.replace(r"-","")
lnd["Age"] = lnd['Age'].str.replace(r"+","")
lnd["Age"] = lnd['Age'].str.replace(r" yrs","")
lnd["Age"] = lnd["Age"].astype(float) # pd.to_numeric(lnd["Age"], errors="ignore")

x_ld = lnd["Age"]
y_ld = lnd["IndicatorFigures"]


#turn 1D array into 2D array
# call preprocessor for StandardScaler to reshape a Series Object
scaler = preprocessing.StandardScaler()
x_ld = scaler.fit_transform(x_ld.values.reshape(-1,1))
y_ld = scaler.fit_transform(y_ld.values.reshape(-1,1))


lnd_X_train, lnd_X_test, lnd_Y_train, lnd_Y_test = train_test_split(x_ld, y_ld, test_size=.2, random_state=2)


linear_model = LinearRegression()
linear_model.fit(lnd_X_train, lnd_Y_train)

lnd_y_train_pred = linear_model.predict(lnd_X_train)
rmse = (np.sqrt(mean_squared_error(lnd_Y_train, lnd_y_train_pred)))
r2 = r2_score(lnd_Y_train, lnd_y_train_pred)


#print("The model performance for training Set - Suicides - London ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")


lnd_Y_test_pred = linear_model.predict(lnd_X_test)
rmse = (np.sqrt(mean_squared_error(lnd_Y_test, lnd_Y_test_pred))) # Root mean squared Error
r2 = r2_score(lnd_Y_test, lnd_Y_test_pred)  #  R squared explained variation / total variation

#print(lnd_Y_test)
#print(lnd_Y_test_pred)

#print("The model performance for testing Set - Suicides - London ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")

# ------- England With LND --------

eng = suicides.england
#eng = eng.drop(drop, axis=1)
eng["Age"] = eng['Age'].str.replace(r"-","")
eng["Age"] = eng['Age'].str.replace(r"+","")
eng["Age"] = eng['Age'].str.replace(r" yrs","")
eng["Age"] = eng["Age"].astype(float) # pd.to_numeric(lnd["Age"], errors="ignore")
x_eng= eng["Age"]
y_eng = eng["IndicatorFigures"]


#turn 1D array into 2D array
# call preprocessor for StandardScaler to reshape a Series Object
scaler = preprocessing.StandardScaler()
x_eng = scaler.fit_transform(x_eng.values.reshape(-1,1))
y_eng = scaler.fit_transform(y_eng.values.reshape(-1,1))


eng_X_train, eng_X_test, eng_Y_train, eng_Y_test = train_test_split(x_eng, y_eng, test_size=.2, random_state=3)


linear_model = LinearRegression()
linear_model.fit(eng_X_train, eng_Y_train)

se_y_train_pred = linear_model.predict(eng_X_train)
rmse = (np.sqrt(mean_squared_error(eng_Y_train, se_y_train_pred)))
r2 = r2_score(eng_Y_train, se_y_train_pred)


#print("The model performance for training Set - Suicides -  England With London  ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")


eng_Y_test_pred = linear_model.predict(eng_X_test)
rmse = (np.sqrt(mean_squared_error(eng_Y_test, eng_Y_test_pred))) # Root mean squared Error
r2 = r2_score(eng_Y_test, eng_Y_test_pred)  #  R squared explained variation / total variation

#print(eng_Y_test)
#print(lnd_Y_test_pred)

print("The model performance for testing Set - Suicides - England With London ")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")

# ------- England W.O LND --------

engwolnd = suicides.england_wo_london
#engwolnd = engwolnd.drop(drop, axis=1)
engwolnd["Age"] = engwolnd['Age'].str.replace(r"-","")
engwolnd["Age"] = engwolnd['Age'].str.replace(r"+","")
engwolnd["Age"] = engwolnd['Age'].str.replace(r" yrs","")
engwolnd["Age"] = engwolnd["Age"].astype(float) # pd.to_numeric(lnd["Age"], errors="ignore")
x_engwolnd= engwolnd["Age"]
y_engwolnd = engwolnd["IndicatorFigures"]


#turn 1D array into 2D array
# call preprocessor for StandardScaler to reshape a Series Object
scaler = preprocessing.StandardScaler()
x_engwolnd = scaler.fit_transform(x_engwolnd.values.reshape(-1,1))
y_engwolnd = scaler.fit_transform(y_engwolnd.values.reshape(-1,1))


engwolnd_X_train, engwolnd_X_test, engwolnd_Y_train, engwolnd_Y_test = train_test_split(x_engwolnd, y_engwolnd, test_size=.2, random_state=3)


linear_model = LinearRegression()
linear_model.fit(engwolnd_X_train, engwolnd_Y_train)

se_y_train_pred = linear_model.predict(engwolnd_X_train)
rmse = (np.sqrt(mean_squared_error(engwolnd_Y_train, se_y_train_pred)))
r2 = r2_score(engwolnd_Y_train, se_y_train_pred)


#print("The model performance for training Set - Suicides -  engwolndland Without London  ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")


engwolnd_Y_test_pred = linear_model.predict(engwolnd_X_test)
rmse = (np.sqrt(mean_squared_error(engwolnd_Y_test, engwolnd_Y_test_pred))) # Root mean squared Error
r2 = r2_score(engwolnd_Y_test, engwolnd_Y_test_pred)  #  R squared explained variation / total variation

#print(engwolnd_Y_test)
#print(lnd_Y_test_pred)

print("The model performance for testing Set - Suicides - England Without London ")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")



# ------- SOUTH EAST --------

se = suicides.se_data
se = se.drop(drop, axis=1)
se["Age"] = se['Age'].str.replace(r"-","")
se["Age"] = se['Age'].str.replace(r"+","")
se["Age"] = se['Age'].str.replace(r" yrs","")
se["Age"] = se["Age"].astype(float) # pd.to_numeric(lnd["Age"], errors="ignore")
#print(se)
x_se = se["Age"]
y_se = se["IndicatorFigures"]


#turn 1D array into 2D array
# call preprocessor for StandardScaler to reshape a Series Object
scaler = preprocessing.StandardScaler()
x_se = scaler.fit_transform(x_se.values.reshape(-1,1))
y_se = scaler.fit_transform(y_se.values.reshape(-1,1))


se_X_train, se_X_test, se_Y_train, se_Y_test = train_test_split(x_se, y_se, test_size=.2, random_state=6)


linear_model = LinearRegression()
linear_model.fit(se_X_train, se_Y_train)

se_y_train_pred = linear_model.predict(se_X_train)
rmse = (np.sqrt(mean_squared_error(se_Y_train, se_y_train_pred)))
r2 = r2_score(se_Y_train, se_y_train_pred)


#print("The model performance for training Set - Suicides -  South East ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")


se_Y_test_pred = linear_model.predict(se_X_test)
rmse = (np.sqrt(mean_squared_error(se_Y_test, se_Y_test_pred))) # Root mean squared Error
r2 = r2_score(se_Y_test, se_Y_test_pred)  #  R squared explained variation / total variation

#'print(se_Y_test)
#print(lnd_Y_test_pred)

#print("The model performance for testing Set - Suicides - South East ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")

# ------- SOUTH WEST   --------

sw = suicides.sw_data
sw = sw.drop(drop, axis=1)
sw["Age"] = sw['Age'].str.replace(r"-","")
sw["Age"] = sw['Age'].str.replace(r"+","")
sw["Age"] = sw['Age'].str.replace(r" yrs","")
sw["Age"] = sw["Age"].astype(float) # pd.to_numeric(lnd["Age"], errors="ignore")
#print(se)
x_sw = sw["Age"]
y_sw = sw["IndicatorFigures"]


#turn 1D array into 2D array
# call preprocessor for StandardScaler to reshape a Series Object
scaler = preprocessing.StandardScaler()
x_sw = scaler.fit_transform(x_sw.values.reshape(-1,1))
y_sw = scaler.fit_transform(y_sw.values.reshape(-1,1))


sw_X_train, sw_X_test, sw_Y_train, sw_Y_test = train_test_split(x_sw, y_sw, test_size=.2, random_state=6)


linear_model = LinearRegression()
linear_model.fit(sw_X_train, sw_Y_train)

sw_y_train_pred = linear_model.predict(sw_X_train)
rmse = (np.sqrt(mean_squared_error(sw_Y_train, sw_y_train_pred)))
r2 = r2_score(sw_Y_train, sw_y_train_pred)


#print("The model performance for training Set - Suicides -  South West ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")


sw_Y_test_pred = linear_model.predict(sw_X_test)
rmse = (np.sqrt(mean_squared_error(sw_Y_test, sw_Y_test_pred))) # Root mean squared Error
r2 = r2_score(sw_Y_test, sw_Y_test_pred)  #  R squared explained variation / total variation

#'print(se_Y_test)
#print(lnd_Y_test_pred)

#print("The model performance for testing Set - Suicides - South West ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")

# ------- NORTH WEST   --------

nw = suicides.nw_data
nw = nw.drop(drop, axis=1)
nw["Age"] = nw['Age'].str.replace(r"-","")
nw["Age"] = nw['Age'].str.replace(r"+","")
nw["Age"] = nw['Age'].str.replace(r" yrs","")
nw["Age"] = nw["Age"].astype(float) # pd.to_numeric(lnd["Age"], errors="ignore")
#print(se)
x_nw = nw["Age"]
y_nw = nw["IndicatorFigures"]


#turn 1D array into 2D array
# call preprocessor for StandardScaler to reshape a Series Object
scaler = preprocessing.StandardScaler()
x_nw = scaler.fit_transform(x_nw.values.reshape(-1,1))
y_nw = scaler.fit_transform(y_nw.values.reshape(-1,1))


nw_X_train, nw_X_test, nw_Y_train, nw_Y_test = train_test_split(x_nw, y_nw, test_size=.2, random_state=6)


linear_model = LinearRegression()
linear_model.fit(nw_X_train, nw_Y_train)

nw_y_train_pred = linear_model.predict(nw_X_train)
rmse = (np.sqrt(mean_squared_error(nw_Y_train, nw_y_train_pred)))
r2 = r2_score(nw_Y_train, nw_y_train_pred)


#print("The model performance for training Set - Suicides -  North West ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")


nw_Y_test_pred = linear_model.predict(nw_X_test)
rmse = (np.sqrt(mean_squared_error(nw_Y_test, nw_Y_test_pred))) # Root mean squared Error
r2 = r2_score(nw_Y_test, nw_Y_test_pred)  #  R squared explained variation / total variation

#'print(se_Y_test)
#print(lnd_Y_test_pred)

#print("The model performance for testing Set - Suicides - North West ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")

# ------- NORTH EAST   --------

ne = suicides.ne_data
ne = ne.drop(drop, axis=1)
ne["Age"] = ne['Age'].str.replace(r"-","")
ne["Age"] = ne['Age'].str.replace(r"+","")
ne["Age"] = ne['Age'].str.replace(r" yrs","")
ne["Age"] = ne["Age"].astype(float) # pd.to_numeric(lnd["Age"], errors="ignore")
#print(se)
x_ne = ne["Age"]
y_ne = ne["IndicatorFigures"]


#turn 1D array into 2D array
# call preprocessor for StandardScaler to reshape a Series Object
scaler = preprocessing.StandardScaler()
x_ne = scaler.fit_transform(x_ne.values.reshape(-1,1))
y_ne = scaler.fit_transform(y_ne.values.reshape(-1,1))


ne_X_train, ne_X_test, ne_Y_train, ne_Y_test = train_test_split(x_ne, y_ne, test_size=.2, random_state=6)


linear_model = LinearRegression()
linear_model.fit(ne_X_train, ne_Y_train)

ne_y_train_pred = linear_model.predict(ne_X_train)
rmse = (np.sqrt(mean_squared_error(ne_Y_train, ne_y_train_pred)))
r2 = r2_score(ne_Y_train, ne_y_train_pred)


#print("The model performance for training Set - Suicides -  North East ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")


ne_Y_test_pred = linear_model.predict(ne_X_test)
rmse = (np.sqrt(mean_squared_error(ne_Y_test, ne_Y_test_pred))) # Root mean squared Error
r2 = r2_score(ne_Y_test, ne_Y_test_pred)  #  R squared explained variation / total variation

#'print(se_Y_test)
#print(lnd_Y_test_pred)

#print("The model performance for testing Set - Suicides - North East ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")



# -------  EAST  OF ENGLAND  --------

ee = suicides.east_england_data
ee = ee.drop(drop, axis=1)
ee["Age"] = ee['Age'].str.replace(r"-","")
ee["Age"] = ee['Age'].str.replace(r"+","")
ee["Age"] = ee['Age'].str.replace(r" yrs","")
ee["Age"] = ee["Age"].astype(float) # pd.to_numeric(lnd["Age"], errors="ignore")
#print(se)
x_ee = ee["Age"]
y_ee = ee["IndicatorFigures"]


#turn 1D array into 2D array
# call preprocessor for StandardScaler to reshape a Series Object
scaler = preprocessing.StandardScaler()
x_ee = scaler.fit_transform(x_ee.values.reshape(-1,1))
y_ee = scaler.fit_transform(y_ee.values.reshape(-1,1))


ee_X_train, ee_X_test, ee_Y_train, ee_Y_test = train_test_split(x_ee, y_ee, test_size=.2, random_state=5)


linear_model = LinearRegression()
linear_model.fit(ee_X_train, ee_Y_train)

ee_y_train_pred = linear_model.predict(ee_X_train)
rmse = (np.sqrt(mean_squared_error(ee_Y_train, ee_y_train_pred)))
r2 = r2_score(ee_Y_train, ee_y_train_pred)


#print("The model performance for training Set - Suicides -   East of England ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")


ee_Y_test_pred = linear_model.predict(ee_X_test)
rmse = (np.sqrt(mean_squared_error(ee_Y_test, ee_Y_test_pred))) # Root mean squared Error
r2 = r2_score(ee_Y_test, ee_Y_test_pred)  #  R squared explained variation / total variation

#'print(se_Y_test)
#print(lnd_Y_test_pred)

#print("The model performance for testing Set - Suicides -  East  of England ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")


# -------  EAST  OF ENGLAND  --------

emid = suicides.east_mid_data
emid = emid.drop(drop, axis=1)
emid["Age"] = emid['Age'].str.replace(r"-","")
emid["Age"] = emid['Age'].str.replace(r"+","")
emid["Age"] = emid['Age'].str.replace(r" yrs","")
emid["Age"] = emid["Age"].astype(float) # pd.to_numeric(lnd["Age"], errors="ignore")
#print(se)
x_emid = emid["Age"]
y_emid = emid["IndicatorFigures"]


#turn 1D array into 2D array
# call preprocessor for StandardScaler to reshape a Series Object
scaler = preprocessing.StandardScaler()
x_emid= scaler.fit_transform(x_emid.values.reshape(-1,1))
y_emid = scaler.fit_transform(y_emid.values.reshape(-1,1))


emid_X_train, emid_X_test, emid_Y_train, emid_Y_test = train_test_split(x_emid, y_emid, test_size=.2, random_state=5)


linear_model = LinearRegression()
linear_model.fit(emid_X_train, emid_Y_train)

emid_y_train_pred = linear_model.predict(emid_X_train)
rmse = (np.sqrt(mean_squared_error(emid_Y_train, emid_y_train_pred)))
r2 = r2_score(emid_Y_train, emid_y_train_pred)


#print("The model performance for training Set - Suicides -   East Midlands ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")


emid_Y_test_pred = linear_model.predict(emid_X_test)
rmse = (np.sqrt(mean_squared_error(emid_Y_test, emid_Y_test_pred))) # Root mean squared Error
r2 = r2_score(emid_Y_test, emid_Y_test_pred)  #  R squared explained variation / total variation

#'print(se_Y_test)
#print(lnd_Y_test_pred)

#print("The model performance for testing Set - Suicides -  East Midlands ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")

# -------  YORKSHIRE  --------

york = suicides.yorkshire_data
york = york.drop(drop, axis=1)
york["Age"] = york['Age'].str.replace(r"-","")
york["Age"] = york['Age'].str.replace(r"+","")
york["Age"] = york['Age'].str.replace(r" yrs","")
york["Age"] = york["Age"].astype(float) # pd.to_numeric(lnd["Age"], errors="ignore")
#print(se)
x_york= york["Age"]
y_york= york["IndicatorFigures"]


#turn 1D array into 2D array
# call preprocessor for StandardScaler to reshape a Series Object
scaler = preprocessing.StandardScaler()
x_york= scaler.fit_transform(x_york.values.reshape(-1,1))
y_york= scaler.fit_transform(y_york.values.reshape(-1,1))


york_X_train, york_X_test, york_Y_train, york_Y_test = train_test_split(x_york, y_york, test_size=.2, random_state=5)


linear_model = LinearRegression()
linear_model.fit(york_X_train, york_Y_train)

york_y_train_pred = linear_model.predict(york_X_train)
rmse = (np.sqrt(mean_squared_error(york_Y_train, york_y_train_pred)))
r2 = r2_score(york_Y_train, york_y_train_pred)


#print("The model performance for training Set - Suicides -   Yorkshire ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")


york_Y_test_pred = linear_model.predict(york_X_test)
rmse = (np.sqrt(mean_squared_error(york_Y_test,york_Y_test_pred))) # Root mean squared Error
r2 = r2_score(york_Y_test, york_Y_test_pred)  #  R squared explained variation / total variation

#'print(se_Y_test)
#print(lnd_Y_test_pred)

#print("The model performance for testing Set - Suicides -  Yorkshire ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")