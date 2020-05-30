from FileLoader import FileLoader


def howManyMedals(df, name):
    dic = {}
    for i in range(len(df)):
        if df.loc[i, "Name"] == name:
            year = df.loc[i, "Year"]
            if not year in dic:
                dic[year] = {
                    "G": 0,
                    "S": 0,
                    "B": 0
                }
            palmares = dic[year]
            if df.loc[i, "Medal"] == "Gold":
                palmares["G"] += 1
            elif df.loc[i, "Medal"] == "Silver":
                palmares["S"] += 1
            elif df.loc[i, "Medal"] == "Bronze":
                palmares["B"] += 1
    return dic


fl = FileLoader()
print(howManyMedals(fl.load("../athlete_events.csv"),
                    "Kjetil Andr Aamodt"))
