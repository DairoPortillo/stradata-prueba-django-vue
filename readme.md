
Comandos para levantar Base de datos

```docker-compose up -d```

Comandos Django

```pip install -r requirements.txt```

```python manage.py migrate```

```python manage.py runserver```

Crear super usuario Django

```python manage.py createsuperuser```

Comandos Django para correr los tests

```python manage.py test```

Comandos para correr frontend

```cd vue-auth```

```npm run dev```


### Nota
Importar csv

### Rutas

``` http://localhost:8000/api/auth/ ``` - Autenticación

``` http://localhost:8000/api/personas/?nombre=asd&porcentaje=1 ``` - Búsqueda

``` http://localhost:8000/api/historial/ ``` - Historial

``` http://localhost:8000/api/historial/{id} ``` - Detalle Historial