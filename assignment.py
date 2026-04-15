import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

df=pd.read_csv("random_walk.csv")
df["distance"]=sqrt(df["x"]**2+df["y"]**2)
