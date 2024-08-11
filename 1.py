import numpy as np
import pandas as pd
df = pd.read_csv("D:/Tutedude/fruits.csv")
print(df)
print(df.describe())
headers = ["Products","S1","S2","S3","S4","S5"]
df.columns = headers
df = df.drop(['S4','S5'],axis=1)
df = df.dropna(subset=['S1','S2','S3'],axis=0)
df = df.replace(np.nan,22)
df["S3"]+=1000
df=df.rename(columns={"S3":"S3+1000"})
print(df)
