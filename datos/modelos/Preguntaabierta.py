from peewee import IntegerField
from datos.modelos.base import BaseModel


class Preguntaabierta(BaseModel):
    id_pregunta = IntegerField(primary_key=True)
    max_caracteres = IntegerField()

    class Meta:
        table_name = "preguntaabierta"