import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

df=pd.read_csv("random_walk.csv")
df["distance"]=np.linalg.norm(df[["x", "y"]], axis=1)

average=df["distance"].mean()
mx=df["distance"].max()
mn=df["distance"].min()
