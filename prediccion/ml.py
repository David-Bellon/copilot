import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt



# Visualizamo la correlacion entre los datos y la relacion en gráficos de todos ellos
def visualizar(data):
    plt.figure(figsize=(10,10))
    sns.heatmap(data.corr(), annot=True)
    plt.show()

    sns.pairplot(data)
    plt.show()



# Primero vamos a preparar los datos sobre los cuales vamos a trabajar, para ello vamos a quitar las columnas de id, track_name y track_id ya que no son relevantes para la 
# prediccion de la popularidad de esta
def preparar(data):
    data = data.drop(columns=["id", "track_id", "track_name"])
    aux = pd.get_dummies(data["artist_name"])
    data = pd.concat([data, aux], axis=1)
    data = data.drop(columns=["artist_name"])

    return data

# Vamos a realizar dos modelos diferentes y a probar estos y ver la diferencias de ambos y cual resulta en mayor precision
def modelos(data):
    data = preparar(data)
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.preprocessing import PowerTransformer
    from sklearn.metrics import r2_score

    X = data.drop(columns=["popularity"])
    y = data["popularity"]


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


    rf = RandomForestRegressor(n_estimators=1000, random_state=42)
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    print("R2 score con RandomForestRegressor: ", r2_score(y_test, rf_pred))
    print(rf.feature_importances_)

    
    rf_pred = rf.predict(X_test)
    error = y_test - rf_pred
    plt.figure(figsize=(10,10))
    sns.histplot(x=error)
    plt.show()

    pt = PowerTransformer()
    X_train = pt.fit_transform(X_train)
    X_test = pt.transform(X_test)
    y_train = np.log(y_train)
    y_test = np.log(y_test)
    
    reg = LinearRegression()
    reg.fit(X_train, y_train)
    reg_pred = reg.predict(X_test)
    print("R2 lineal: ", r2_score(y_test, reg_pred))

    reg_pred = reg.predict(X_test)
    error = np.exp(y_test) - np.exp(reg_pred)
    plt.figure(figsize=(10,10))
    sns.histplot(x=error)
    plt.show()



data = pd.read_csv("copilot\spoti.csv")
visualizar(data)
modelos(data)