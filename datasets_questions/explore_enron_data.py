#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import pandas

# solution one: work with dictionary functions

def get_dataset_information_dict(enron_data):
    people = len(list(enron_data.keys()))
    print ('There are %d people in the sampled dataset.' %people)

    features = len(list(enron_data.values())[0].values())
    print('There are %d features for each person in the sampled datasets.' %features)

    counter = 0
    for key, value in enron_data.items():
        if value['poi'] == True:
            counter += 1

    print('There are %d poi persons in this sampled dataset.' %counter)

# solution two: work with pandas dataframe functions
def get_dataset_information_df(enron_data):
    df = pandas.DataFrame.from_dict(enron_data, orient = 'index')
    row, col = df.shape
    print('There are %d people in the sampled datasets.' %row)
    print('There area %d features for each person in the sampled datasets.' %col)

    counter = len(df[df.poi==True])
    print('There are %d poi persons in this sampled dataset.' %counter)

    salary_num = len(data[data.salary!='NaN'])
    address_mail_num = len(data[data.email_address!='NaN'])
    print('Qualitifed salary %d' %salary_num)
    print('Qualitifed address mail %d' %address_mail_num)

    non_payment_num = len(data[data.total_payments=='NaN'])
    print('People do not have total payments record %d' %non_payment_num)



if __name__ == '__main__':
    enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
    print('There are', len(enron_data), 'people in the enron dataset.')
    get_dataset_information_df(enron_data)
