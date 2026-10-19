from peewee import IntegerField, CharField, DateField
from datos.modelos.base import BaseModel


class Administrador(BaseModel):
    id_usuario = IntegerField(primary_key=True)
    cargo = CharField(max_length=50)
    fecha_contratacion = DateField()

    class Meta:
        table_name = "administrador"

