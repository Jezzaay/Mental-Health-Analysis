import  younger_people
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


# ------- LONDON --------


lnd = younger_people.london_data
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


lnd_X_train, lnd_X_test, lnd_Y_train, lnd_Y_test = train_test_split(x_ld, y_ld, test_size=.2, random_state=6)


linear_model = LinearRegression()
linear_model.fit(lnd_X_train, lnd_Y_train)

lnd_y_train_pred = linear_model.predict(lnd_X_train)
rmse = (np.sqrt(mean_squared_error(lnd_Y_train, lnd_y_train_pred)))
r2 = r2_score(lnd_Y_train, lnd_y_train_pred)


#print("The model performance for training set - London ")
#print("--------------------------------------")
#print('RMSE is {}'.format(rmse))
#print('R2 score is {}'.format(r2))
#print("\n")


lnd_Y_test_pred = linear_model.predict(lnd_X_test)
rmse = (np.sqrt(mean_squared_error(lnd_Y_test, lnd_Y_test_pred))) # Root mean squared Error
r2 = r2_score(lnd_Y_test, lnd_Y_test_pred)  #  R squared explained variation / total variation

#print(lnd_Y_test)
#print(lnd_Y_test_pred)

print("The model performance for testing set - London ")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")

# ------- England W.O LND --------

eng = younger_people.england_wo_london

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


eng_X_train, eng_X_test, eng_Y_train, eng_Y_test = train_test_split(x_eng, y_eng, test_size=.2, random_state=5)


linear_model = LinearRegression()
linear_model.fit(eng_X_train, eng_Y_train)

se_y_train_pred = linear_model.predict(eng_X_train)
rmse = (np.sqrt(mean_squared_error(eng_Y_train, se_y_train_pred)))
r2 = r2_score(eng_Y_train, se_y_train_pred)


print("The model performance for training set -  England Without London  ")
#print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")


eng_Y_test_pred = linear_model.predict(eng_X_test)
rmse = (np.sqrt(mean_squared_error(eng_Y_test, eng_Y_test_pred))) # Root mean squared Error
r2 = r2_score(eng_Y_test, eng_Y_test_pred)  #  R squared explained variation / total variation

#print(eng_Y_test)
#print(lnd_Y_test_pred)

print("The model performance for testing set - England Without London ")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")



# ------- SOUTH EAST --------

se = younger_people.se_data
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


print("The model performance for training set -  South East ")
#print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")


se_Y_test_pred = linear_model.predict(se_X_test)
rmse = (np.sqrt(mean_squared_error(se_Y_test, se_Y_test_pred))) # Root mean squared Error
r2 = r2_score(se_Y_test, se_Y_test_pred)  #  R squared explained variation / total variation

#'print(se_Y_test)
#print(lnd_Y_test_pred)

print("The model performance for testing set - South East ")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")

# ------- SOUTH WEST   --------

sw = younger_people.sw_data
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


print("The model performance for training set -  South West ")
#print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")


sw_Y_test_pred = linear_model.predict(sw_X_test)
rmse = (np.sqrt(mean_squared_error(sw_Y_test, sw_Y_test_pred))) # Root mean squared Error
r2 = r2_score(sw_Y_test, sw_Y_test_pred)  #  R squared explained variation / total variation

#'print(se_Y_test)
#print(lnd_Y_test_pred)

print("The model performance for testing set - South West ")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")

# ------- NORTH WEST   --------

nw = younger_people.nw_data
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


print("The model performance for training set -  North West ")
#print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")


nw_Y_test_pred = linear_model.predict(nw_X_test)
rmse = (np.sqrt(mean_squared_error(nw_Y_test, nw_Y_test_pred))) # Root mean squared Error
r2 = r2_score(nw_Y_test, nw_Y_test_pred)  #  R squared explained variation / total variation

#'print(se_Y_test)
#print(lnd_Y_test_pred)

print("The model performance for testing set - North West ")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")