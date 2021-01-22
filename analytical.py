import pandas as pd


def data_prep():
    data = pd.read_csv(r'data/data_analytics.csv')
    print(data.head())


if __name__ == '__main__':
    data_prep()

