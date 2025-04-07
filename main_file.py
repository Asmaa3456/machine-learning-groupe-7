import numpy as np
import pandas as pd
import chardet
import matplotlib.pyplot as plt

# Détection de l'encodage
with open("machine-learning-groupe-7/Domain1_csv/Subject7-8-6.csv", 'rb') as f:
    result = chardet.detect(f.read())
    print(result)

# Lecture du fichier CSV avec le bon encodage
df = pd.read_csv("machine-learning-groupe-7/Domain1_csv/Subject7-8-6.csv", encoding=result['encoding'])

# Garde uniquement les colonnes x et y
df = df.iloc[:, :2]
df.columns = ['x', 'y']

# Tracé 2D
plt.figure(figsize=(10, 6))
plt.plot(df['x'], df['y'], marker='o')
plt.title("Trajectoire du geste en 2D")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')  # Pour garder les proportions X/Y
plt.show()
