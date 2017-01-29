#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
a = preprocess()
##a = map(lambda x: x.reshape(-1, 1) if type(x) != list else x, a)
features_train, features_test, labels_train, labels_test = a

#########################################################
### your code goes here ###

clf = GaussianNB()
t = time()
clf.fit(features_train, labels_train)
print( "training time:", round(time()-t, 3), "s")
t=time()
predict = clf.predict(features_test)
print (type(predict),type(features_test))
print "prediction time:", round(time()-t, 3), "s"
accuracy = clf.score(features_test, labels_test)
form
print (accuracy)

#########################################################
