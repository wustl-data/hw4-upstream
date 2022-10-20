import pandas as pd


def median_by_undergrad(survey: pd.DataFrame) -> pd.Series:
    return pd.Series(name="Median Salary", index=pd.Index([], name="Undergraduate Major"))
