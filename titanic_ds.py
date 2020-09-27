import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)
print("*******TRAIN DATASET********")
#print(train.describe())
print(train.columns.values)
print(train.isna().sum())
train.fillna(train.mean(), inplace=True)
print(train.isna().sum())
#test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
#print("*******TEST DATASET********")
#print(pd.read_csv(test_url))
