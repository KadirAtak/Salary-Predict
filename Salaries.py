# -*- coding: utf-8 -*-
"""developer_200205039_AbdulkadirAtak

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16HYhZWvWhzo_H64aPujF90uaaUZd_fO1
"""

from keras.layers import Dense
from keras.models import Sequential
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.optimizers import Adam
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
from sklearn.preprocessing import StandardScaler
from keras.optimizers import SGD

data=pd.read_csv('salaries.csv')
data.columns
data_encoded = pd.get_dummies(data, columns=['experience_level', 'employment_type', 'job_title','employee_residence', 'company_location', 'company_size','salary_currency'])
print(data_encoded.head())

x = data_encoded.drop(['salary','salary_in_usd'], axis=1)
y = data_encoded['salary']*32

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.10,random_state=58)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

mlp = Sequential()
mlp.add(Dense(128, activation='relu', input_dim=X_train.shape[1]))
mlp.add(Dense(64, activation='relu'))
mlp.add(Dense(64, activation='relu'))
mlp.add(Dense(64, activation='relu'))
mlp.add(Dense(16, activation='relu'))
mlp.add(Dense(1, activation='linear'))

opt=SGD(learning_rate=0.1)
mlp.compile(loss="mean_squared_error", optimizer='Adam', metrics=['mean_squared_error'])

mlp.fit(X_train_scaled, y_train, epochs=50, batch_size=128, validation_split=0.1)

pred = mlp.predict(X_test_scaled)
from sklearn.metrics import mean_absolute_error, r2_score
mae = mean_absolute_error(y_test, pred)
print("Test seti ortalama mutlak hata (MAE):", mae)
r2 = r2_score(y_test, pred)
print("Test seti R-kare (R^2):", r2)

"""## 2. yapay sinir ağı

"""

mlp_2 = Sequential()
mlp_2.add(Dense(128, activation='relu', input_dim=X_train.shape[1]))
mlp_2.add(Dense(64, activation='relu'))
mlp_2.add(Dense(64, activation='relu'))
mlp_2.add(Dense(64, activation='relu'))
mlp_2.add(Dense(32, activation='relu'))
mlp_2.add(Dense(1, activation='linear'))

from keras.optimizers import SGD
opts=Adam(learning_rate=0.01)
mlp_2.compile(loss="mean_squared_error", optimizer=opts, metrics=['mean_squared_error'])

mlp_2.fit(X_train_scaled, y_train, epochs=50, batch_size=128, validation_split=0.1)

preds = mlp_2.predict(X_test_scaled)
from sklearn.metrics import mean_absolute_error, r2_score
mae = mean_absolute_error(y_test, preds)
print("Test seti ortalama mutlak hata (MAE):", mae)
r2 = r2_score(y_test, preds)
print("Test seti R-kare (R^2):", r2)

"""# 3. yapay sinir ağı"""

mlp_3 = Sequential()
mlp_3.add(Dense(128, activation='relu', input_dim=X_train.shape[1]))
mlp_3.add(Dense(64, activation='relu'))
mlp_3.add(Dense(64, activation='relu'))
mlp_3.add(Dense(1, activation='linear'))

from keras.optimizers import SGD
optss=Adam(learning_rate=0.1)
mlp_3.compile(loss="mean_squared_error", optimizer=optss, metrics=['mean_squared_error'])

mlp_3.fit(X_train_scaled, y_train, epochs=50, batch_size=128, validation_split=0.1)

predss = mlp_3.predict(X_test_scaled)
from sklearn.metrics import mean_absolute_error, r2_score
mae = mean_absolute_error(y_test, predss)
print("Test seti ortalama mutlak hata (MAE):", mae)
r3 = r2_score(y_test, predss)
print("Test seti R-kare (R^2):", r3)