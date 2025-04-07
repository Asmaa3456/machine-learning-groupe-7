import numpy
import pandas as pd
import chardet
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

with open("machine-learning-groupe-7/Domain1_csv/Subject7-8-6.csv", 'rb') as f:
    result = chardet.detect(f.read())
    print(result)
    print(f.readline())

df = pd.read_csv("machine-learning-groupe-7/Domain1_csv/Subject7-8-6.csv", encoding=result['encoding'])

df = df.iloc[:, :2]  # on garde seulement les 3 premières colonnes
df.columns = ['x', 'y']  # renomme les colonnes si nécessaire


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='2d')

ax.plot(df['x'], df['y'], df['z'], marker='o')

ax.set_title("Trajectoire du geste en 2D")
ax.set_xlabel("X")
ax.set_ylabel("Y")

plt.show()
