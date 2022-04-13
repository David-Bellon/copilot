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

Popularidad

Como podemos observar en un principio podriamos decir que hay elementos dispersos por abajo pero teniendo en cuenta que los datos que tenemos son de las 50 canciones más escuchadas del año tiene sentido que haya pocas populares.

Danzabilidad
//Danzabilidad
Podemos observar que no hay mucha dispersion y es mas una distribucion normal

Energia
//Energia
Mas de lo mismo con energía

Key
//Key
Mas elementos en los extremos pero tampoco excesivos como para considerarlos outsiders.

Volumen
//voulumen
Se tiende a canciones más altas pero tambien este es un apartado que no representa mucho ya que al tratarse de canciones dependiendo del género son de un estio u otro. Lo que si se puede sacar de aqui es que las cancioones con mas decibelios son las que mas reproducciones tienen en general.

Speechiness
//speech
Parecido a lo que ocurre con el tono, abundancia en un lado y pocos en el otro extremo sin ningun fuera de serie concreto.

Acustico
//acustico
Más de lo mismo que los dos anteriores.

Liveness
//ivenes
Predominancia de un tipo muy clara lo que indica que las mas escuchadas son las que mayor alegria trasmiten pero ninguna cancion con la que se puede afirmar que hay un error o algo por el estilo.

Valence
//Vaence
Distribucion normal casi perfecta.

Tempo
//Tempo
Mas de lo mismo, muy distribuida.

Duracion
//Duracion
Distribucion normal similar a las anteriores
