import pandas as pd
def double(val):
    return val["salary"]*2
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
     employees["bonus"]=employees.apply(double,axis=1)
     return employees