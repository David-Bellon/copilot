En este texto se detalla paso por paso el proceso que se ha seguido y que se debería seguir antes una situacion similar. Para apoyar las ideas se han ido adjuntando imágenes.

En la carpeta codigo hay dos archivos uno llamado "analisis" en el cual se recogen todas las funciones que habria que ir mirando una a una para tomar reflejo de como nos llegan los datos
y como habría que modificar estos. Y en el otro archivo "limpieza" se encuentra el código por el cual se ha pasado los datos antes de realizar cualquier tipo de acción con ellos.


-Primero obtenemos una descripción de como son los datos que se encuentran en nustro dataset
![image info](copilot\Analisis_Datos\imagenes\1.png)
Como podemos observar los tipos de datos que tenemos son ints(numeros enteros), floats(Decimales) y objetos(En pandas se le llaman así a los strings), a su vez vemos que todos los tipos de
datos estan bien por lo que en este caso no habría que tocar nada.

-Con esta misma función podemos ver si existen valores nulos en alguna de nuestras filas. Y como podemos observar no hay ningún valor nulo por lo que tampoco haremos nada respecto
a esto. En la mayoria de casos habría que quitar las filas de valores nulos o añadir a dichos valores nulos algunos datos de los que podamos obtener informacion.


-Ahora vamos a ver si hay dupicados en columnas que no nos interesan. Si observamos el archivo de datos, las unicas columnas que nos interesan que no dispongan de valores duplicados son id, nombre de la cancion y track id. Para esto vamos a mirar si existe algun valor duplicado en estas columnas, de ser el caso eliminaríamos uno de los dos. Para ello miramos si la longitud de la lista de todos los datos de la columna es igual a la lista pero detro de un conjunto ya que se borran los duplicados. 
![image info](copilot\Analisis_Datos\imagenes\2.png)
Como podemos ver hay el mismo numero de datos por lo que no exisen valores duplicados.

