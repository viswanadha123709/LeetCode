import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows=len(players.index)
    columns=len(players.columns)
    return list(players.shape)