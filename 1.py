import pandas as pd

# Nuetsros datos no son para relaizar aprendizaje automatico si no mas para clasificar por grupos las distintas

data = pd.read_csv("copilot\spoti.csv")

#miramos si existen valores nulos

top10 = data.head(10)
df10 = pd.DataFrame({"artist_name": top10["artist_name"], "track_name":top10["track_name"]})

df10.to_csv("top10.csv")

data.sort_values(by="popularity")
print(data)
# dsico una de triste y otra de contento, top 10 del año