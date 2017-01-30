#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
from sklearn import cross_validation
from sklearn.metrics import classification_report,confusion_matrix,precision_score,recall_score
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list,sort_keys="../tools/python2_lesson14_keys.pkl")
labels, features = targetFeatureSplit(data)
features_training, features_test, labels_training, labels_test = cross_validation.train_test_split(features,labels,random_state=42,test_size=0.3)
clf = DecisionTreeClassifier()
clf.fit(features_training, labels_training)
predict = clf.predict(features_test)
print clf.score(features_test, labels_test)
print classification_report(labels_test, predict)
print confusion_matrix(labels_test,predict)
print precision_score()
### it's all yours from here forward!  


