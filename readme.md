# Mensajes a grupos en Python
Repositorio que puede usarse para enviar emails personalizados a conjuntos de usuarios. Explicamos su uso a través de un ejemplo:

> Queremos enviar los correos necesarios para organizar un amigo invisible.

Para ello, partiremos de un fichero .csv que contendrá la dirección de email de cada participante junto a un texto que contiene el nombre de la persona a quien tiene comprar un regalo.

El fichero tendrá que tener esta estructura:

```
mariagomez@dominio.es,María Gómez, José Luis Dominguez
joserodriguez@dominio.es,José Rodriguez, María Gómez
joseluisd@dominio.es, José Luis Dominguez, José Rodriguez
```

Aportaremos el cuerpo del mensaje en el fichero config.ini. Cada uno de los {} será un hueco a rellenar por la información dada en el csv. (salvo el primer elemento que es la dirección de destino). Por ejemplo un mensaje para poner en este caso sería:

```
Hola {}!!!! Para el amigo invisible de la empresa te ha tocado {}
```
El primer mail que se enviaría a mariagomez@dominio.es y contendría el texto:

> Hola María Gomez!!!! Para el amigo invisible de la empresa te ha tocado José Luis Dominguez

En el fichero config_secret.ini (ejemplo en config_secret-example.ini) se deberá poner la informaión de la cuenta que enviará los emails.