import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers["status"] = ~customers["id"].isin(orders["customerId"])
    return customers[customers["status"]][["name"]].rename(
        columns={"name": "Customers"}
    )