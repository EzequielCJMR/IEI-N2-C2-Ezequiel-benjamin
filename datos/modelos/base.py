from peewee import Model
from datos.conexion import conectar

database = conectar()


class BaseModel(Model):
    class Meta:
        database = database