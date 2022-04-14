# Prediccion de popularidad de una canción  
## Introducción
En este apartado hemos intentado diseñar un modelo con el cual nos permita predecir la poplaridad de una canción basada en distintos rasgos. cabe añadir antes de empezar que el archivo de los datos es de solo 50 filas por lo que no se esperan buenos resultados de ante mano.  
Para ello lo primero que hemos realizado es observar la relacion que existen entre las variables a traves de un mapa de correlaciones como el siguiente  
//Añadir iagen calor  
Como podemos observar si nos fijamos en la columna de de popularidad que es la que nos interesa veremos que hay poca relación entre cualquier variable y esta, lo que nos indica con antelación que la elaboración de un modelo para la predicción de este dato no arroja muy buen futuro, aun así seguiremos adelante ya que es interesante ver el proceso y la predicción de otro dato carece de mucho sentido.  

El siguiente paso ha sido realizar esta comparacion pero de manera gráfica para observar si existe alguna relación tanto lineal como inversa de alguno de los datos. Además, nos permite ver la distribución de cada una de las variables, nuestro objetivo será el de que se asemjen lo mas posible a una distribución normal.  
Las imágenes ya se han tomado con anterioridad y se encuentran en la carpeta de Analisis de Datos asi como en el texto adjuntado en dicha carpeta. Como podemos observar algunas distribuciones comparten semejanza con una distribución normal y otras con una logaritmica por lo que se procederá a corregir estos datos.

## Modelos
Hemos decidido usar dos modelos diferentes, regresión lineal y bosques aleatorios para disponer de dos modelos diferentes y ver cual de los dos trabaja mejor en esta situación. 
Antes de realizar ninguna operación ni trabajo hemos decidido eliminar las columnas de id, nombre de canción, y track id ya que no aportan valor y son irrelevantes a la hora de determinar si una canción es popular o no. Además hemos decidido añadir cada uno de los artistas como columna de nuestros datos ya que creemos que es relevante a la hora de la predicción.
Empezaremos por el modelo de regresión lineal.  

### Regresión Lineal
A la hora de trabajar con datos en un modelo cualquiera separaremos las variables dependientes frente a las independientes, así mismo separaremos los datos de entrenamiento y de test.  
A continuación, se aplica un ajuste a las variables independientes para dejar a estas con una distribución lo más parecida a una distribución normal, lo mismo con la variable dependiente.
Una vez ajustados todos los datos se procede al entrenamiento del modelo y la predicción de sus valores para su posterior análisis.

### Bosque Aleatorios
Al contrario que con el modelo de regresión lineal, en este modelo no haría falta la estandarización de sus variables por el mero funcionamiento de este algoritmo ya que se centra en la busqueda de patrones, en cierta manera, para la optención de una salida acorde a los datos. Se procede de la misma manera que antes y se entrena y se predicen los datos del modelo

## Errores e Interpreación
Una vez obenidos los datos de la predicción hemos calculado el error de estos con los valores que deberían haberse obtenido en realidad y hemos realizado tanto un histograma del error como el valor del r cuadrado de cada modelo
### Regresión Lineal 
//Foto erro regfresion
Como podemos observar la mayoria de los datos se encuentran respecto a la media pero es verdad que la dispersión de los valores es muy grande siendo la amplitud del erro de 30 puntos por arriba y por abajo. Además el r cuadrado arroja un valor negativo y no muy favorable pero no es del todo concluyente ya que en muchas ocasiones no hay que tomar el valor de este como validación de los datos.

### Bosque Aleatorio
//foot
Como se observa el gráfico es similar al anterior pero esta vez la amplitid de los fallos es mucho menor, arrojando un fallo de 7 por abajo y un error maximo por la derecha de 10, lo cual nos indica que este modelo se ajusta mucho mejor a estos datos


## Conclusión
Como se ha vsito, hemos procedido con la elaboración de dos modelos de regresión para la predicción de la popularidad de una canción cualquiera. Hemos visto que uno de los dos modelos se ajusta mucho mejor y que otro, el de regresión lineal, falla mucho más, esto es debido a que como se ha vsito al principio no existia apenas relación de ninguna vriable con la popularidad lo que hace que un modelo de este tipo carezca de mucho acierto. Por el contrario el modelo de bosque aleatorio arroja datos mas esperanzadores ya que apesar de no exisir mucha relación directa es el funcionamiento del modelo el que se encarga de encontrar estas.
Cabe destacar para finalizar que al tratarse de una muestra de datos tan pequeña cualquier eleboración de un modelo predictivo será siempre de menor precisión y de menor información.
