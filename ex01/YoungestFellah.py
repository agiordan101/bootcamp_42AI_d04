from FileLoader import FileLoader


def youngestFellah(df, year):
    min = {'f': 100,
           'm': 100}
    for i in range(1, len(df)):
        if df.loc[i, "Year"] == year:
            if (df.loc[i, "Sex"] == "F" and df.loc[i, "Age"] < min['f']):
                min['f'] = df.loc[i, "Age"]
            if (df.loc[i, "Sex"] == "M" and df.loc[i, "Age"] < min['m']):
                min['m'] = df.loc[i, "Age"]
    return min


fl = FileLoader()
youngest_athlete = youngestFellah(fl.load("../athlete_events.csv"), 2004)
print(youngest_athlete)
