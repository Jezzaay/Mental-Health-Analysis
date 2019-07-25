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

ypld = younger_people.london_data
ypld = ypld.drop(drop, axis=1)
ypld["Age"] = ypld['Age'].str.replace(r"-","")
ypld["Age"] = ypld['Age'].str.replace(r"+","")
ypld["Age"] = ypld['Age'].str.replace(r" yrs","")
ypld["Age"] = ypld["Age"].astype(float) # pd.to_numeric(ypld["Age"], errors="ignore")

X_ypld = ypld["Age"]
Y_ypld = ypld["IndicatorFigures"]


#turn 1D array into 2D array
# call preprocessor for StandardScaler to reshape a Series Object
scaler = preprocessing.StandardScaler()
X_ypld = scaler.fit_transform(X_ypld.values.reshape(-1,1))
Y_ypld = scaler.fit_transform(Y_ypld.values.reshape(-1,1))


ypld_X_train, ypld_X_test, ypld_Y_train, ypld_Y_test = train_test_split(X_ypld, Y_ypld, test_size=.2, random_state=5)
#ypld_X_train = ypld_X_train.reshape(-1,1)
#ypld_X_test = ypld_X_test.reshape(-1,1)
#ypld_Y_train = ypld_Y_train.reshape(-1,1)

print(ypld_X_train.shape)
print(ypld_X_test.shape)
print(ypld_Y_train.shape)
print(ypld_Y_test.shape)

linear_model = LinearRegression()
linear_model.fit(ypld_X_train, ypld_Y_train)

ypld_y_train_pred = linear_model.predict(ypld_X_train)
rmse = (np.sqrt(mean_squared_error(ypld_Y_train, ypld_y_train_pred)))
r2 = r2_score(ypld_Y_train, ypld_y_train_pred)


print("The model performance for training set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")


ypld_Y_test_pred = linear_model.predict(ypld_X_test)
rmse = (np.sqrt(mean_squared_error(ypld_Y_test, ypld_Y_test_pred)))
r2 = r2_score(ypld_Y_test, ypld_Y_test_pred)

print(ypld_Y_test)
print(ypld_Y_test_pred)

print("The model performance for testing set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))

print(type(ypld_Y_test))