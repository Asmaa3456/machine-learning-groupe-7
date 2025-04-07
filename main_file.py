import numpy
import pandas as pd

df = pd.read_csv("data/Domain1_csv/Subject1-0-1.csv")
df.columns = ['x', 'y', 'z']  # renomme les colonnes si nécessaire


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(df['x'], df['y'], df['z'], marker='o')

ax.set_title("Trajectoire du geste en 3D")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
