# Import the necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics



# For text feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer
# For creating a pipeline
from sklearn.pipeline import Pipeline
# Classifier Model (Logistic Regression)
from sklearn.linear_model import LogisticRegression

def pwd_analyseir(num_num_data):
    # Read the File
    data = pd.read_csv('static/training.csv')
    features = data.values[:, 1].astype('str')
    labels = data.values[:, -1].astype('int')
    classifier_model = Pipeline([
                    ('tfidf', TfidfVectorizer(analyzer='char')),
                    ('logisticRegression',LogisticRegression(multi_class='multinomial', solver='sag')),
    ])
    # Fit the Model
    classifier_model.fit(features, labels)
    # Instead of splitting dataset into training and testing, we keep test dataset as seprate .csv file 
    df= pd.read_csv('static/cleanpasswordlist.csv')
    X = df.values[:, 1].astype('str')
    y = df.values[:, -1].astype('int')
    predictions = classifier_model.predict(X)
    # Report the confusion matrix
    from sklearn import metrics
    # my code
    a = []
    a.append(num_num_data) 
    var = a[:1]
    predict=classifier_model.predict(var)
    # print(predict)
    return predict
    



# var = pre_pwd('tioijoifo')
# print(var[0])

