# Gateway
Gateway de acceso a los micro servicios de la aplicación.

## Tecnologias
- Flask (framework del servicio web)

## Configuración local y en Heroku
#### Variables de entorno
Las siguientes variables de entorno debe ser establecidas en el contenedor donde se ejecuta el servicio:
- `PROJECTS_BACKEND_URL`: url del micro servicios de proyectos
- `USERS_BACKEND_URL`: url del micro servicio de usuarios
- `PAYMENTS_BACKEND_URL`: url del micro servicio de pagos
- `PAYMENTS_API_KEY`: API KEY para interactuar con el micro servicio de pagos.

#### Firebase y Google Cloud
Se debe crear un archivo `firebaseKey.json` en la carpeta `prod/api/` con el siguiente formato:

```
{
  "type": ,
  "project_id": ,
  "private_key_id": ,
  "private_key": ,
  "client_email": ,
  "client_id": ,
  "auth_uri": ,
  "token_uri": ,
  "auth_provider_x509_cert_url": ,
  "client_x509_cert_url":
}
```
Cada campo deber ser completado con los valores que define la documentación de Firebase.

Este archivo contiene información sensible y, por lo tanto, no se _pushea_ al repositorio remoto.

### Localmente
Se debe crear un archivo `.env` en el mismo directorio donde se encuentran los _dockerfiles_. En el mismo, se podran definir variables de entorno sensibles que no se van a _pushear_ al repositorio remoto. Por ejemplo, allí se puede definir la API KEY del micro servicio de pagos.

Tambien configurarse el puerto donde se levantara el servicio a traves de la siguiente variable de entorno:
- `PORT`

La configuración no sensible puede setearse en el archivo `docker-compose.yml`


## Entorno Local

### Requerimientos
- docker (Docker version 20.10.7, build f0df350)
- docker-compose (docker-compose version 1.29.1, build c34c88b2)

### Construcción
```
docker-compose build
```

### Ejecución
```
docker-compose up [-d]
```
Nota: agregar flag '-d' despues del 'up', para ejecutar en segundo plano.

Este comando levantará dos servicios:
- `service_gateway`: Es el mismo servicio que se ejecuta en Heroku.
- `test`: Servicio para _testing_. Tiene las URLs de los microservicios truncadas de forma de no interactura con los mismos en producción. Además, deshabilita la interacción con Firebase y Google Cloud.

### _Tests_
```
docker-compose exec test pytest "dev/tests" -p no:warnings
```
Nota: El servicio `test` debe estar levantado.

Tambien se pueden ejecutar a traves del siguiente _script_:
```
./run_tests.sh
```
#### Detalles
Los pruebas se implementarón mockeando las peticiones y respuestas hacia y desde los micros servicios. Para ello, se utilizo la dependencias `requests_mock`.

### Detener:
```
docker-compose stop
```

### Destruir
```
docker-compose down
```

## Entorno Heroku
### Informacion
Nombre de la aplicacion Heroku (App): seedy-fiuba
Nombre del repositorio Heroku: https://git.heroku.com/seedy-fiuba.git

URL de la aplicacion: https://seedy-fiuba.herokuapp.com/

### Despliegue
Conectarse a Heroku:
```
heroku login
```

Agregar repositorio remoto de Heroku
```
heroku git:remote --app seedy-fiuba
```
Nota: El creador del repositorio de Heroku deberia hacer colaborado a quienes quieren pushear al mismo.

Conectarse al contenedor de Heroku:
```
heroku container:login
```

Construir imagen de la aplicacion y pushear a heroku:
```
heroku container:push web --app seedy-fiuba
```

Ejecutar la imagen subida en la instancia de heroku
```
heroku container:release web --app seedy-fiuba
```

### Prendido y apagado del servicio
Prendido del servicio :
```
heroku ps:scale web=1 --app seedy-fiuba
```

Apagado del servicio :
```
heroku ps:scale web=0 --app seedy-fiuba
```
