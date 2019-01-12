"""
Zadanie2_Cognitive_Patronage2019
made by Andrzej Klimko
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

dataPath = 'salary.csv'
# location and of .csv file containing data

class Cognitive:
    """
    """
    
    frame = []
    complete_data = []
    partial_data = []
    X = []
    y = []
    to_fill_X = []
    predicted = []
    
    
    def data_loading(self):
        """Loads data from file replacing missing values with NaN."""
        self.frame = pd.read_csv(dataPath, na_values = ' ', header = 0)
        return
    
    
    def data_preprocessing(self):
        """Separates complete and incomplete rows into separate frames
        and scales them.
        """
        self.complete_data = self.frame.dropna()
        self.partial_data = self.frame[self.frame.isnull().any(axis=1)]
        #splitting complete and incomplete rows
        
        arr = np.array(self.complete_data, dtype = np.float)
        arr2 = np.array(self.partial_data, dtype = np.float)
        # convert values to floats
        arr = MinMaxScaler().fit_transform(arr)
        # scaling complete rows for further processing
        self.X, self.y = arr[:, :-1], arr[:, -1]
        self.to_fill_X = arr2[:, :-1]
        # splitting scaled data for further processing
        self.to_fill_X = MinMaxScaler().fit_transform(self.to_fill_X)
        # scaling incomplete rows
        return
    
    
    def data_predicting(self):
        """Uses sklearn to fill uncompleted rows."""
        from sklearn.svm import SVR
        svr = SVR(kernel='linear')
        svr.fit(self.X, self.y)
        self.predicted = svr.predict(self.to_fill_X)
        return
    
    
    def data_rescaling(self):
        """Scales the data to what it was before processing."""
        self.X = MinMaxScaler(feature_range=(1, 12.7)).fit_transform(self.X)
        self.to_fill_X = MinMaxScaler(feature_range=(
            2, 12)).fit_transform(self.to_fill_X)
        combined = np.concatenate([self.y, self.predicted])
        combined = np.array(combined, dtype = np.float)
        combined = MinMaxScaler(feature_range=(2750, 13000)).fit_transform(
            combined.reshape(-1, 1))
        # combining data to rescale it
        # done to use data from file for scaling predicted data
        self.y, self.predicted = combined[:len(self.y)], combined[len(self.y):]
        #splitting data again, for further use
        return
    
    
    def plot(self):
        """Makes data visualization."""
        plt.scatter(self.X, self.y, label='inputed data')
        plt.plot(self.to_fill_X, self.predicted, color = 'red')
        plt.scatter(self.to_fill_X, self.predicted,
            label = 'estimated values', color = 'red')
        plt.legend()
        plt.show()
        return


# Creating class instance and calling created methods.
cognitive = Cognitive()
cognitive.data_loading()
cognitive.data_preprocessing()
cognitive.data_predicting()
cognitive.data_rescaling()
cognitive.plot()

