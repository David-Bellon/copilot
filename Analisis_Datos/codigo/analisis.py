import pandas as pd


def descripcion(data):
    print(data.info())

def unicos(data):
    print("id")
    print(len(data["id"]) == len(set(data["id"])))

    print("track_name")
    print(len(data["track_name"]) == len(set(data["track_name"])))

    print("track_id")
    print(len(data["track_id"]) == len(set(data["track_id"])))

data = pd.read_csv("copilot\spoti.csv")
unicos(data)