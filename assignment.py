import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

df=pd.read_csv("random_walk.csv")
df["distance"]=np.linalg.norm(df[["x", "y"]], axis=1)

average=df["distance"].mean()
mx=df["distance"].max()
mn=df["distance"].min()

print(f"average={average}, max={mx}, min={mn}")
distmore=df[df['distance']>average]
print(f"Distance more than average:\n {distmore[['step','distance']]}")

# with open('filtered_walk.json', 'w') as f_w:
distmore.to_json("filtered_walk.json", orient="records", indent=3)

plt.plot(df["x"], df["y"], color="blue", label="y(x)")
first_last=df[(df["step"]==1) | (df["step"]==300)]
plt.plot(first_last['x'],first_last['y'], color="red", marker="o", linestyle="none",label="first/last step")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
