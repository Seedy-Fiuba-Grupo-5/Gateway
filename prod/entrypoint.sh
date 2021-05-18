#!/bin/sh
# Indica a Flask que levante un servidor
# 0.0.0.0 : El servidor sera publicamente visible
# ${PORT:-5002} : El puerto donde se bindea el server
# esta especificado por la variable de entorno PORT.  
# PORT=5001, por defecto.
flask run --host=0.0.0.0 --port=${PORT:-5002}
