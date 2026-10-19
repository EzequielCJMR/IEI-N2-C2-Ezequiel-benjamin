from peewee import CharField, DateField, IntegerField
from datos.modelos.base import BaseModel


class Encuestado(BaseModel):
    id_usuario = IntegerField(primary_key=True)
    fecha_nacimiento = DateField()
    genero = CharField(max_length=20, null=True)
    ocupacion = CharField(max_length=50, null=True)
    pais = CharField(max_length=50)

    class Meta:
        table_name = "encuestado"