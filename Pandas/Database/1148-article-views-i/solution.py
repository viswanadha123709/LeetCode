import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    temp=views[(views["author_id"]==views["viewer_id"])]
    return temp.sort_values("author_id").drop_duplicates(subset="author_id")[["author_id"]].rename(columns={"author_id":"id"})
    