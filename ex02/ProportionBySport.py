from FileLoader import FileLoader


def proportionBySport(df, year, sport, gender):
    n_ahtlete = 0
    n_ahtlete_sport = 0
    last_ahtlete = None
    for i in range(len(df)):
        if (df.loc[i, "Year"] == year
           and df.loc[i, "Sex"] == gender
           and df.loc[i, "Name"] != last_ahtlete):
            n_ahtlete += 1
            if df.loc[i, "Sport"] == sport:
                n_ahtlete_sport += 1
            last_ahtlete = df.loc[i, "Name"]
    return n_ahtlete_sport / n_ahtlete


fl = FileLoader()
print(proportionBySport(fl.load("../athlete_events.csv"),
                        2004, "Tennis", "F"))
