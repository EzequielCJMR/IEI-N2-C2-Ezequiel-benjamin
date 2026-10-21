from peewee import AutoField, IntegerField, CharField, DateField
from datos.modelos.base import BaseModel

class Administrador(BaseModel):
    id_administrador = AutoField()
    id_usuario = IntegerField()
    cargo = CharField(max_length=50)
    fecha_contratacion = DateField()

    class Meta:
        table_name = "administrador"