import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    temp = employee.sort_values(by="salary", ascending=False)
    temp = temp.drop_duplicates(subset="salary")

    if len(temp) < N or N<1:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})

    salary = temp.iloc[N - 1]["salary"]
    return pd.DataFrame({f"getNthHighestSalary({N})": [salary]})