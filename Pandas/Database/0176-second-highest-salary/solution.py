import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset="salary")
    employee = employee.sort_values(by="salary", ascending=False)
    employee.reset_index(inplace=True, drop=True)

    if len(employee) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})

    return employee.rename(
        columns={"salary": "SecondHighestSalary"}
    ).iloc[[1]][["SecondHighestSalary"]]