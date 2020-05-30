from FileLoader import FileLoader


class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        years = []
        for i in range(len(self.df)):
            if self.df.loc[i, "City"] == location:
                year = self.df.loc[i, "Year"]
                if year not in years:
                    years.append(year)
        return years

    def where(self, year):
        for i in range(len(self.df)):
            if self.df.loc[i, "Year"] == year:
                return self.df.loc[i, "City"]
        return None


fl = FileLoader()
std = SpatioTemporalData(fl.load("../athlete_events.csv"))
print(std.where(1896))
print(std.where(2016))
print(std.when("Athina"))
print(std.when("Paris"))
