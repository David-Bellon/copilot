En este texto se detalla paso por paso el proceso que se ha seguido y que se debería seguir antes una situacion similar. Para apoyar las ideas se han ido adjuntando imágenes.

En la carpeta codigo hay dos archivos uno llamado "analisis" en el cual se recogen todas las funciones que habria que ir mirando una a una para tomar reflejo de como nos llegan los datos
y como habría que modificar estos. Y en el otro archivo "limpieza" se encuentra el código por el cual se ha pasado los datos antes de realizar cualquier tipo de acción con ellos.


-Primero obtenemos una descripción de como son los datos que se encuentran en nustro dataset

![1](https://user-images.githubusercontent.com/91338053/163276163-48fabbdc-8f9a-4ec1-8345-685e592450fc.PNG)

Como podemos observar los tipos de datos que tenemos son ints(numeros enteros), floats(Decimales) y objetos(En pandas se le llaman así a los strings), a su vez vemos que todos los tipos de
datos estan bien por lo que en este caso no habría que tocar nada.

-Con esta misma función podemos ver si existen valores nulos en alguna de nuestras filas. Y como podemos observar no hay ningún valor nulo por lo que tampoco haremos nada respecto
a esto. En la mayoria de casos habría que quitar las filas de valores nulos o añadir a dichos valores nulos algunos datos de los que podamos obtener informacion.


-Ahora vamos a ver si hay dupicados en columnas que no nos interesan. Si observamos el archivo de datos, las unicas columnas que nos interesan que no dispongan de valores duplicados son id, nombre de la cancion y track id. Para esto vamos a mirar si existe algun valor duplicado en estas columnas, de ser el caso eliminaríamos uno de los dos. Para ello miramos si la longitud de la lista de todos los datos de la columna es igual a la lista pero detro de un conjunto ya que se borran los duplicados. 
![2](https://user-images.githubusercontent.com/91338053/163281265-1f67e1d9-de6c-41a5-9e11-c30223c2755f.PNG)
Como podemos ver hay el mismo numero de datos por lo que no exisen valores duplicados y no debemos hacer nada.

-Vamos a ver si existiera algún dato en alguna de las columnas que resaltara del resto ya por ser muy elevado o muy bajo. Para ello miramos los datos estadisticos de cada columna
![3](https://user-images.githubusercontent.com/91338053/163281337-16544f0e-de6e-486f-a64b-0eb1c3538001.PNG)
Podemos ver si miramos detenidamente que no hay ningun valor muy disperso y que se salga mucho de lo corriente en ninguna columna, sobre todo fijandonos en valores maximos y minimos y sin tener en cuenta coumnas columnas que llevan numero concretos enteros.

-Para añadir mas peso a esto vamos a ver los histogramas de cada una de las columnas importantes y vemos como es su distribucion y que podemos sacar de cada una de ellas. Solo nos centraremos en las que tengan valores reseñables.

**Popularidad**

Como podemos observar en un principio podriamos decir que hay elementos dispersos por abajo pero teniendo en cuenta que los datos que tenemos son de las 50 canciones más escuchadas del año tiene sentido que haya pocas populares.

**Danzabilidad**
![danza](https://user-images.githubusercontent.com/91338053/163281460-db9ecb28-4843-4dd0-b83b-ac0e257bbb44.PNG)
Podemos observar que no hay mucha dispersion y es mas una distribucion normal

**Energia
![energia](https://user-images.githubusercontent.com/91338053/163281484-d3e972fc-8865-41b6-a8f2-d2e5ea72f949.PNG)
Mas de lo mismo con energía

**Key
![key](https://user-images.githubusercontent.com/91338053/163281497-b4b88ae8-7167-4013-a791-bf0f4545c5e3.PNG)

Mas elementos en los extremos pero tampoco excesivos como para considerarlos outsiders.

**Volumen
![volumen](https://user-images.githubusercontent.com/91338053/163281511-fc1c74a7-1785-4ef3-bfaa-fa13215390ad.PNG)

Se tiende a canciones más altas pero tambien este es un apartado que no representa mucho ya que al tratarse de canciones dependiendo del género son de un estio u otro. Lo que si se puede sacar de aqui es que las cancioones con mas decibelios son las que mas reproducciones tienen en general.

**Speechiness
![speech](https://user-images.githubusercontent.com/91338053/163281516-3cc42771-f55f-4a31-a2a1-e113d6d06daf.PNG)

Parecido a lo que ocurre con el tono, abundancia en un lado y pocos en el otro extremo sin ningun fuera de serie concreto.

**Acustico
![acustico](https://user-images.githubusercontent.com/91338053/163281537-9713b1b9-cd32-41b6-be6c-241e315e66ba.PNG)

Más de lo mismo que los dos anteriores.

**Liveness
![liveness](https://user-images.githubusercontent.com/91338053/163281545-e1c72a39-bfed-4be8-bd9f-8791d2a2a554.PNG)

Predominancia de un tipo muy clara lo que indica que las mas escuchadas son las que mayor alegria trasmiten pero ninguna cancion con la que se puede afirmar que hay un error o algo por el estilo.

**Valence
![valence](https://user-images.githubusercontent.com/91338053/163281556-857179a9-9a7e-4415-92bc-aec5ebf90c17.PNG)

Distribucion normal casi perfecta.

**Tempo
![tempo](https://user-images.githubusercontent.com/91338053/163281568-9c297a86-5971-421f-bd15-576f965e082f.PNG)

Mas de lo mismo, muy distribuida.

**Duracion
![duracion](https://user-images.githubusercontent.com/91338053/163281577-78aa9655-be0d-4d36-a09b-857cf6404812.PNG)

Distribucion normal similar a las anteriores
