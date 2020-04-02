#!/usr/bin/env python
from collections import defaultdict
import pandas as pd

d = pd.read_csv("summarized.csv")

nyears = len(set(d["year"]))

variables = defaultdict(list)
for c in set(d["country_id"]):
    variables["year"] += set(d["year"])
    variables["country_id"] += [c for i in range(nyears)]
    for v in ("low","best","high"):
        variables[v] += [0 for i in range(nyears)]

empty = pd.DataFrame(data = variables)

zeropadded = pd.concat((empty,d)).groupby(["country_id","year"]).sum()
zeropadded.to_csv("zeropadded.csv")

