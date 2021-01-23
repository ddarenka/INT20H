import pandas as pd
import numpy as np

"""
    Plan:
        1) Stop-words removal
        2) Lemmatization (several different forms of the same word are mapped to one single form)
        3) Tokenization
        4) Text vectorization
"""


"""
    Machine learning text classification algorithms:
        1) Naive Bayes (especially Multinomial Naive Bayes)
        2) SVM
"""

"""
    Evaluate model using:
        1) Precision (Accuracy) -> how often a sentiment rating was correct
        2) Recall               -> how many documents with sentiment were rated as sentimenta
        3) F1 Score             -> it gives us a single metric that rates a system by both precision and recall
"""

def data_prep():
    data = pd.read_csv(r'data/train.csv')
    print(data.head())


if __name__ == '__main__':
    train = pd.read_csv(r'data/train.csv', index_col='id')
    test = pd.read_csv(r'data/test.csv', index_col='id')
    submission = pd.read_csv(r'data/submission.csv')

    train['sentiment'].value_counts()
    submission.head()
    train.head(7)