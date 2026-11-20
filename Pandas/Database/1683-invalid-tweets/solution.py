import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    temp=tweets[tweets["content"].str.len()>15]
    return temp[["tweet_id"]]