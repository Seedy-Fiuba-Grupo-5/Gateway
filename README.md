# Gateway
Gateway de acceso a los servicios de la aplicación.  
 
## Tecnologias
- Flask (framework del servicio web)

## Entorno Local
### Construcción
```
docker-compose build
```
### Ejecución
Iniciar servicio:  
```
docker-compose up
```
Nota: agregar flag '-d' despues del 'up', para ejecutar en segundo plano.  
  
Detener servicio:  
```
docker-compose stop
```

### Destrucción
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
heroku git:remote -a seedy-fiuba
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
