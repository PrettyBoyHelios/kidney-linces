import pandas as pd
import numpy as np


def classify_bp(bp):
    if 40 < bp <= 60:
        return 0
    if 60 < bp <= 80:
        return 1
    if 80 < bp <= 90:
        return 2
    if 90 < bp <= 100:
        return 3


# Cleans blood pressure
def clean_bp(d):
    sum = 0
    cont = 0
    for i, row in data.iterrows():
        try:
            x = int(row['bp'])
            row['bp'] = classify_bp(x)
            sum += x
            cont += 1
        except:
            row['bp'] = -1
            continue

    avg = sum/cont
    for i, row in data.iterrows():
        if row['bp'] == -1:
            #  TODO Update to use KNN assignation
            row['bp'] = classify_bp(avg)
    return data


def clean_columns(d, interest):
    remove_columns = []
    for column in d:
        print("column: ", column)
        if column not in interest:
            d = d.drop(column, axis=1)
            remove_columns.append(column)
    d = d.drop(remove_columns, axis=1)
    return d



def clean_data(d, interest):
    d = clean_columns(d, interest)
    d = clean_bp(d)
    return d


interest_columns = {"bp", "rbc", "pc", "pcc", "hemo", "pcv", "wc", "rc"}
data = pd.read_csv("renal.csv")
data = clean_data(data, interest_columns)
data.to_csv("hematomic.csv")
print(data)

