import pandas as pd


def descripcion(data):
    print(data.info())

def unicos(data):
    for columna in data:
        print("Columna:" + columna)
        print(len(data[columna]) == len(set(data[columna])))

data = pd.read_csv("copilot\spoti.csv")
unicos(data)