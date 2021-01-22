import pandas as pd

"""
    Plan:
        1) Text vectorization
"""


"""
    Machine learning text classification algorithms:
        1) Naive Bayes (especially Multinomial Naive Bayes)
        2) SVM
"""


def data_prep():
    data = pd.read_csv(r'data/train.csv')
    print(data.head())


if __name__ == '__main__':
    data_prep()
