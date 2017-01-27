#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)
d=sorted(data, key=lambda x: x[1])
print d[-2]
outliers=[]
for key in data_dict.keys():

    if data_dict[key]['salary'] >= 1e6 and data_dict[key]['bonus']>=5e6:
        outliers.append((key, data_dict[key]['salary'], data_dict[key]['bonus']))
        print key
print filter(lambda x:x[1]!="NaN",outliers)
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

### your code below



