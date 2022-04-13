import pandas as pd


# cada una de estas funciones lo que hace es ordenar el dataframe según lo que nos interese en cada uno de ellos
# y luego coger los primeros resultados y guardarlos en su propio fichero ya que mas adelante nos sera de utilidad 
# para poder reooger estos datos de manera sencilla y rápida

def get_populares(data):
    aux = data.sort_values(by=["popularity"])
    aux = aux.head(15)
    populares = pd.DataFrame({"artist": aux["artist_name"], "cancion" : aux["track_name"]})
    populares.to_csv(r"copilot\top_Populares.csv", index=False)

def get_bailables(data):
    aux = data.sort_values(by=["danceability"])
    aux = aux.head(15)
    bailables = pd.DataFrame({"artist": aux["artist_name"], "cancion" : aux["track_name"]})
    bailables.to_csv(r"copilot\top_Bailables.csv", index=False)
    
def get_topTen(data):
    top10 = data.head(10)
    df10 = pd.DataFrame({"artist": top10["artist_name"], "cancion" : top10["track_name"]})
    df10.to_csv(r"copilot\top10.csv", index=False)


data = pd.read_csv("copilot\spoti.csv")

get_topTen(data)
get_populares(data)
get_bailables(data)