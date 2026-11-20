import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(
        department.rename(columns={"id": "departmentId", "name": "Department"}),
        on="departmentId"
    )

    max_salary = employee.groupby("Department")["salary"].max().reset_index()

    result = employee.merge(
        max_salary,
        on=["Department", "salary"]
    )

    return result[["Department", "name", "salary"]].rename(
        columns={"name": "Employee", "salary": "Salary"}
    )