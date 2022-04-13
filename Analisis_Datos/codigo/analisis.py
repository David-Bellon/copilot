import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def descripcion(data):
    print(data.info())

def unicos(data):
    print("id")
    print(len(data["id"]) == len(set(data["id"])))

    print("track_name")
    print(len(data["track_name"]) == len(set(data["track_name"])))

    print("track_id")
    print(len(data["track_id"]) == len(set(data["track_id"])))

def estadistica_columna(data):
    print(data.describe())

def graficar(data):
    for column in data:
        sns.histplot(x=data[column])
        plt.show()


data = pd.read_csv("copilot\spoti.csv")
graficar(data)