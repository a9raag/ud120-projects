from prep_terrain_data import makeTerrainData
from sklearn.naive_bayes import  GaussianNB


features_train, labels_train, features_test, labels_test = makeTerrainData()
clf=GaussianNB()
clf.fit(features_train,labels_train)
clf.predict(features_test)
print clf.score(features_test,labels_test)