# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FWDDDgLSmPpPxr4daYXf0rCQu2s06d2J
"""

from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM , GRU ,SimpleRNN,RNN
from google.colab import drive
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import TimeseriesGenerator
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from tensorflow.keras.layers import LeakyReLU
from keras.layers import Dropout

drive.mount('/content/drive')

df=pd.read_csv('drive/My Drive/dataset/TripB01.csv',sep=';', encoding="ISO-8859-1")
df2=pd.read_csv('drive/My Drive/dataset/TripB02.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB03.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB04.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB05.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB06.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB07.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB08.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB09.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB10.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB11.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB12.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB13.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB14.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB15.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB16.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB17.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB18.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB19.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB20.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB21.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB22.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB23.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB24.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB25.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB26.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB27.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB28.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB29.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB30.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB31.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB32.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB33.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB34.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB35.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB36.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB37.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)
df2=pd.read_csv('drive/My Drive/dataset/TripB38.csv',sep=';', encoding="ISO-8859-1")
df= df.append(df2)

len(df)

#df["Velocity [km/h]]]"]=df["Velocity [km/h]]]"].fillna(0)
#df["Velocity [km/h]"]=df["Velocity [km/h]"].fillna(0)
df['Velocity [km/h]]]'] = df['Velocity [km/h]]]'].fillna(df['Velocity [km/h]]]'].mean()) 
df['Velocity [km/h]']=df['Velocity [km/h]'].fillna(df['Velocity [km/h]]]'].mean())

df=df.fillna(df.mean())

#df.drop(['Velocity [km/h]]]'], axis=1,inplace=True)
df.drop(['Temperature Vent right [°C] ','Ambient Temperature Sensor [°C]','Throttle [%]','Temperature Vent central left [°C]','Temperature Vent central right [°C]','max. Battery Temperature [°C]','SoC [%]','min. SoC [%]','Throttle [%]','Temperature Vent right [°C]','Regenerative Braking Signal ','max. Battery Temperature [°C]','max. SoC [%)','Heating Power LIN [W]','Requested Heating Power [W]','Heater Signal','Requested Coolant Temperature [°C]','Coolant Temperature Heatercore [°C]','Coolant Temperature Inlet [°C]','Temperature Coolant Heater Inlet [°C]','Temperature Coolant Heater Outlet [°C]','Temperature Heat Exchanger Outlet [°C]','Temperature Defrost lateral left [°C]','Temperature Defrost lateral right [°C]','Temperature Defrost central [°C]','Temperature Defrost central left [°C]','Temperature Defrost central right [°C]','Temperature Footweel Driver [°C]','Temperature Footweel Co-Driver [°C]','Temperature Feetvent Co-Driver [°C]','Temperature Feetvent Driver [°C]','Temperature Head Co-Driver [°C]','Temperature Head Driver [°C]'],axis=1,inplace=True)
df=df.dropna(how='any')

len(df)

df.index.is_unique

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(16,6))
cor = df.corr()
sns.heatmap(cor,annot=True, cmap='BrBG')
plt.show()

df

values = df.values
values = values.astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)


def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg

reframed = series_to_supervised(scaled, 2, 1)

reframed.drop(reframed.columns[[14,15,16,17,18,19,20]], axis=1, inplace=True)

reframed

#with lag 

n_train_hours=50000
values = reframed.values
train = values[:n_train_hours, :]
test = values[n_train_hours:, :]

train_X=train[:,:13]

train_X=np.delete(train_X, 12, 1)
train_y=train[:,12]

test_X=test[:,:13]
test_X=np.delete(test_X, 12, 1)
test_y=test[:,12]
#train_X, train_y = train[:, :-1], train[:, -1]
#test_X, test_y = test[:, :-1], test[:, -1]
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)

n_train_hours=50000
values = reframed.values
train = values[:n_train_hours, :]
test = values[n_train_hours:, :]

train_X=train

train_X=np.delete(train_X, 8, 1)
train_y=train[:,8]

test_X=test
test_X=np.delete(test_X, 8, 1)
test_y=test[:,8]
#train_X, train_y = train[:, :-1], train[:, -1]
#test_X, test_y = test[:, :-1], test[:, -1]
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)



test_y = test_y.reshape((len(test_y), 1))
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,0]

model = Sequential()
model.add(LSTM(units=100,return_sequences=True, input_shape=(train_X.shape[1], train_X.shape[2])))


model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
# fit network
history = model.fit(train_X, train_y, epochs=60, batch_size=80, validation_data=(test_X, test_y), verbose=1, shuffle=False)
# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()

yhat = model.predict(test_X)

# make a prediction
yhat = model.predict(test_X)

test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))

# invert scaling for forecast
inv_yhat = concatenate((yhat, test_X[:, 1:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:,41]
# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_X[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,41]
# calculate RMSE
rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
print('Test RMSE: %.3f' % rmse)

test_y*(100-9.5)+9.5

yhat*(100-9.5)+9.5

y=yhat*(100-9.5)+9.5
y=y.tolist()
max(y)

rmse = sqrt(mean_squared_error(y,yx))
print('Test RMSE: %.3f' % rmse)

y2=(test_y*(100-9.5))+9.5
y2=y2.tolist()
len(y2)
t1= pd.DataFrame(y)
t2=pd.DataFrame(y2)

t1.to_excel('predtemp.xlsx')

test=df.iloc[50000:,:]
test.to_excel('test.xlsx')

!pip install kora -q
from kora.selenium import wd
wd.get("https://google.com")

df.describe()