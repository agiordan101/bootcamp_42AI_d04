import pandas as pd


class FileLoader:

    def __init__(self):
        pass
    
    def load(self, path):
        df = pd.read_csv(path)
        print("Dimensions row/col : {} / {}".format(len(df), len(df.columns)))
        return df

    def display(df, n):
        

fl = FileLoader()
fl.load("../athlete_events.csv")
