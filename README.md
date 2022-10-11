# Docker Flask Api con Firebase y JWT
## Uso
1. Hacemos un fork del repositorio o lo descargamos
2. Ya dentro del repositorio creamos el contenedor docker con el siguiente comando
`sudo docker-compose up`
3. Abrimos un programa con el cual podamos hacer peticiones, este puede ser curl, wget, postman, insomnia, o un explorador, yo utilizare insomnia.
4. Vamos a ver el entry point "/" o el de por defecto, para ello vamos a "http://127.0.0.1:5000".
[![Imsomnia1](https://i.ibb.co/Zfn0Y0m/Imsonia1.png "Imsomnia1")](https://i.ibb.co/Zfn0Y0m/Imsonia1.png "Imsomnia1")
5. Para crear un usuario vamos a "http://127.0.0.1:5000/signup" con el metodo GET ponemos Multipart Form, seguido de esto creamos dos campos uno para el email y otro para el password, los rellenamos tal que asi.
[![Insomnia2](https://i.ibb.co/hKgCcxL/Imsomnia2.png "Insomnia2")](https://i.ibb.co/hKgCcxL/Imsomnia2.png "Insomnia2")
Al lado derecho podemos ver que se creo el usuario satisfactoriamente
6. Ahora necesitamos un token para ello vamos a "http://127.0.0.1:5000/token" con  el metodo GET ponemos Multipart Form, creamos el campo email y password, los digitamos, despues le damos enviar.[![Insomnia3](https://i.ibb.co/T4xcSvx/Insomnia3.png "Insomnia3")](https://i.ibb.co/T4xcSvx/Insomnia3.png "Insomnia3")
Esto nos dara un token, lo copiamos.
7. Para ver el palindromo dentro del texto vamos a "http://127.0.0.1:5000/palindromo", ponemos metodo POST, mandamos formato JSON, con una unica propiedad llamada "text" con el contenido del texto el cual queremos buscar el palindromo en este caso "abccc"[![Insomnia4](https://i.ibb.co/7Nyx7df/Insomnia4.png "Insomnia4")](https://i.ibb.co/7Nyx7df/Insomnia4.png "Insomnia4")
seguido vamos a los Headers, creamos un campo llamado authorization y ponemos el token.[![Insomnia5](https://i.ibb.co/VTjnWk9/Insomnia5.png "Insomnia5")](https://i.ibb.co/VTjnWk9/Insomnia5.png "Insomnia5")
por ultimo le damos enviar.
[![Insomnia6](https://i.ibb.co/gJ1Sp7Q/Insomnia6.png "Insomnia6")](https://i.ibb.co/gJ1Sp7Q/Insomnia6.png "Insomnia6")Esto nos dara como resultado un JSON con una unica propiedad llamada palindromo, con el contenido del palindromo mas largo encontrado.
