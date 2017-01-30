#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
from sklearn import tree

# clf = tree.DecisionTreeClassifier(min_samples_split=40)
# clf.fit(features_train, labels_train)
# predict = clf.predict(features_test)


def classify(features, labels, samples):
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(min_samples_split=samples, random_state=42)
    clf = clf.fit(features, labels)
    return clf


acc_min_samples_split_2 =classify(features_train, labels_train, 2).score(features_test, labels_test)
print (acc_min_samples_split_2)
# clf50 = classify(features_train, labels_train, 50)
# acc_min_samples_split_50 = clf50.score(features_test, labels_test)
# print acc_min_samples_split_50
#########################################################
### your code goes here ###


#########################################################
