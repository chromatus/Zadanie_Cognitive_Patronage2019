"""
Zadanie2_Cognitive_Patronage2019
made by Andrzej Klimko
"""

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

from .models import Salary

data_path = 'salary.csv'
# Location and of .csv file containing input data.
    

class Cognitive:
    """Class for handling data."""
    frame = []
    complete_data = []
    partial_data = []
    X = []
    y = []
    to_fill_X = []
    predicted = []
    
    
    def data_import_from_file(self):
        """Loads data from file replacing missing values with NaN."""
        self.frame = pd.read_csv(data_path, na_values = ' ', header = 0)
        return
    
    
    def data_preprocessing(self):
        """Separates complete and incomplete rows into separate frames
        and scales them.
        """
        self.complete_data = self.frame.dropna()
        self.partial_data = self.frame[self.frame.isnull().any(axis=1)]
        # Splitting complete and incomplete rows.
        
        arr = np.array(self.complete_data, dtype = np.float)
        arr2 = np.array(self.partial_data, dtype = np.float)
        # Converting values to floats.
        arr = MinMaxScaler().fit_transform(arr)
        # Scaling complete rows for further processing.
        self.X, self.y = arr[:, :-1], arr[:, -1]
        self.to_fill_X = arr2[:, :-1]
        # Splitting scaled data for further processing.
        self.to_fill_X = MinMaxScaler().fit_transform(self.to_fill_X)
        # Scaling incomplete rows.
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
        # Combining data to rescale it,
        # done to use data from file for scaling predicted data.
        self.y, self.predicted = combined[:len(self.y)], combined[len(self.y):]
        # Splitting data again, for further use.
        return
    
    
#     def plot(self):
#         """Makes data visualization."""
#         plt.scatter(self.X, self.y, label='inputed data')
#         plt.plot(self.to_fill_X, self.predicted, color = 'red')
#         plt.scatter(self.to_fill_X, self.predicted,
#             label = 'estimated values', color = 'red')
#         plt.legend()
#         plt.show()
#         return
    
    
    def data_export(self):
        """Exports data to the database."""
        try:
            for i in range(0, len(self.X)):
                temp = Salary(years_worked=float(self.X[i]), salary=float(self.y[i]))
                temp.save()
            for i in range(0, len(self.to_fill_X)):
                temp = Salary(years_worked=float(self.to_fill_X[i]), salary=float(self.predicted[i]))
                temp.save()
        except:
            # Rolls back changes if something goes wrong.
            pass
        return


# Creating class instance and calling created methods.
# cognitive = Cognitive()
# cognitive.data_import_from_file()
# cognitive.data_preprocessing()
# cognitive.data_predicting()
# cognitive.data_rescaling()
# cognitive.plot()
# cognitive.data_export()
# database_print()