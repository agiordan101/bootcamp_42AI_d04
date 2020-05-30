import pandas as pd


class FileLoader:

    def __init__(self):
        pass

    def load(self, path):
        df = pd.read_csv(path)
        print("Load \"{}\" / Dimensions row/col : {} / {}"
              .format(path, len(df), len(df.columns)))
        return df

    def display(self, df, n):
        if n < 0:
            print(df[n:])
        else:
            print(df[:n])
