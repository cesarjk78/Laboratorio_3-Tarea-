descragar el archivo, una ves hecho eso en el cmd poner:

1. python -m venv venv
2. venv\Scripts\activate
3. pip install django
4. code . (vemos que todo este bien)
5. python manage.py migrate  (y ponerlo en el sql lite administrator)
6. por ultimo python manage.py runserver y la tarea estara funcionando
7. en la url poner http://127.0.0.1:8000/registro/registrar_propietario/  y veremos nuestro programa corriendo
