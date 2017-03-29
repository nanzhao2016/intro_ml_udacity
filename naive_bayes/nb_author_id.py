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


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score
comp = {}

"""
gnb = GaussianNB()
t0 = time()
gnb.fit(features_train, labels_train)
print("training time: ", round(time()-t0, 3), "s")

t1 = time()
pred = gnb.predict(features_test)
print("predicting time: ", round(time()-t1, 3), "s")

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(pred, labels_test)

print(accuracy)
"""
gnb = GaussianNB()
gnb.fit(features_train, labels_train)
pred = gnb.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
comp['gnb'] = accuracy

mnb = MultinomialNB()
mnb.fit(features_train, labels_train)
pred = mnb.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
comp['mnb'] = accuracy

bnb = BernoulliNB()
bnb.fit(features_train, labels_train)
pred = bnb.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
comp['bnb'] = accuracy

import pprint

pprint.pprint(comp)




#########################################################





