#!/usr/bin/env python
import pandas as pd

data = pd.read_csv("data/ged191.csv")
data = data[["country_id","year","low","best","high"]]
data = data.groupby(["country_id","year"]).sum()
data.to_csv("summarized.csv")
