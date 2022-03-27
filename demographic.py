import pandas as pd
import numpy as np

df=pd.read_csv("artical.csv")

df=df.sort_values('score', ascending=False)
output=df[['total_events']].head(20).values.tolist()