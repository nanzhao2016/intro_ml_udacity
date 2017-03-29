#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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




#########################################################
### your code goes here ###

#########################################################

from sklearn import svm
from sklearn.metrics import accuracy_score
import pprint

results = {}
#sample = round(len(features_train)/100)
sample = len(features_train)
features_train = features_train[: sample]
labels_train = labels_train[: sample]

"""
svc = svm.SVC(kernel = "linear")
t0 = time()
svc.fit(features_train, labels_train)
print("training time is: ", time()-t0, "s")
pred = svc.predict(features_test)

accuracy = accuracy_score(pred, labels_test)
results["linear"] = accuracy

svc = svm.SVC(kernel = "rbf")
t0 = time()
svc.fit(features_train, labels_train)
print("training time is: ", time()-t0, "s")
pred = svc.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
results["rbf"] = accuracy

pprint.pprint(results)
"""
"""
c = [1, 10, 100, 1000, 10000]
for i in c:
    svc = svm.SVC(kernel = "rbf", C=i)
    svc.fit(features_train, labels_train)
    pred = svc.predict(features_test)
    accuracy = accuracy_score(pred, labels_test)
    results[str(i)] = accuracy	

pprint.pprint(results)
"""
svc = svm.SVC(kernel = "rbf", C=10000)
svc.fit(features_train, labels_train)
pred = svc.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
print(accuracy)	

print(sum(pred))



