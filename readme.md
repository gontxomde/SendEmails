# Mensajes a grupos en Python
Repositorio que puede usarse para enviar emails personalizados a conjuntos de usuarios. Explicamos su uso a través de un ejemplo:

> Queremos enviar los correos necesarios para organizar un amigo invisible.

Para ello, partiremos de un fichero llamado emails.csv que contendrá la dirección de email de cada participante junto a un texto que contiene el nombre de la persona a quien tiene comprar un regalo.

El fichero tendrá que tener esta estructura:

```
sender,name,present_to
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

Es necesario que haya tantos {} en el cuerpo del mensaje como columnas distintas del destinatario haya en el .csv

En el fichero config_secret.ini (ejemplo en config_secret-example.ini) se deberá poner la informaión de la cuenta que enviará los emails.

## Envio de contraseñas

En su primera versión, la única forma de enviar elementos era en la cadena de texto. Esto podía suponer un problema para enviar contraseñas, ya que había que hacerlo en texto plano. Ahora se implementa la posibilidad de enviar un captcha generado automáticamente a partir de un texto del csv. Por ejemplo, si tenemos una columna del csv que es una contraseña, al instanciar la clase Mailer haremos lo siguiente:

```python
from mailer import Mailer
m = Mailer('emails.csv', toCaptcha = 'nombreCampoContraseña')
```
Cuando lea el campo enviado en toCaptcha en vez de enviarse el campo como texto, se generará un captcha que contenga ese texto y se adjuntará al email como imagen.