import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    temp=weather.pivot(index="month",columns="city",values="temperature")
    return temp