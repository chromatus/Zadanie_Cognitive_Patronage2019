"""
Zadanie2_Cognitive_Patronage2019
made by Andrzej Klimko
"""

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

dataPath = 'salary.csv'
# location and of .csv file containing data

class Data:
    def dataLoading(self):
        # loads data from file replacing missing values with NaN
        frame = pd.read_csv(dataPath, na_values = ' ', header = 0)
        return frame
    
    
    def dataPreprocessing(self, frame):
        # separating complete and incomplete rows 
        # into separate frames and scaling them
        complData = frame.dropna()
        incomplData = frame[frame.isnull().any(axis=1)]
        #splitting complete and incomplete rows
        
        arr = np.array(complData, dtype = np.float)
        arr2 = np.array(incomplData, dtype = np.float)
        # convert values to floats
        arr = MinMaxScaler().fit_transform(arr)
        # scaling complete rows for further processing
        X, y = arr[:, :-1], arr[:, -1]
        toFillX = arr2[:, :-1]
        # splitting scaled data for further processing
        toFillX = MinMaxScaler().fit_transform(toFillX)
        # scaling incomplete rows
        return X, y, toFillX
    
    
    def dataPredicting(self, X, y, toFillX):
        # using sklearn to fill uncompleted rows    
        from sklearn.svm import SVR
        svr = SVR(kernel='linear')
        svr.fit(X, y)
        predy = svr.predict(toFillX)
        return predy
    
    
    def dataRescaling(self, X, y, toPred, estData):
        # scaling data to what it was before processing  
        X = MinMaxScaler(feature_range=(1, 12.7)).fit_transform(X)
        toPred = MinMaxScaler(feature_range=(2, 12)).fit_transform(toPred)
        
        combined = np.concatenate([y, estData])
        combined = np.array(combined, dtype = np.float)
        combined = MinMaxScaler(feature_range=(2750, 13000)).fit_transform(
            combined.reshape(-1, 1))
        # combining data to rescale it
        # done to use data from file for scaling predicted data
        y, estData = combined[:len(y)], combined[len(y):]
        #splitting data again, for further use
        return X, y, toPred, estData
    
    
#     def plot(self, X, y, toPred, estData):
#         # visualizing results
#         plt.scatter(X, y, label='inputed data')
#         plt.plot(toPred, estData, color = 'red')
#         plt.scatter(toPred, estData,
#             label = 'estimated values', color = 'red')
#         plt.legend()
#         plt.show()
#         return


# # Using created functions
# dataFrame = dataLoading()
# globalX, globaly, toPredictX = dataPreprocessing(dataFrame)
# estimatedData = dataPredicting(globalX, globaly, toPredictX)
# globalX, globaly, toPredictX, estimatedData = dataRescaling(
#         globalX, globaly, toPredictX, estimatedData)
# print("Years worked:  ")
# print(toPredictX)
# print("Estimated salary:   ")
# print(estimatedData)
# plot(globalX, globaly, toPredictX, estimatedData)