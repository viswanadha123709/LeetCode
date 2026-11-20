import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"]=students["grade"].map(int)
    return students