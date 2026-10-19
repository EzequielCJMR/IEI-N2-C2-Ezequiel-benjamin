from peewee import IntegerField
from datos.modelos.base import BaseModel


class Preguntaescala(BaseModel):
    id_pregunta = IntegerField(primary_key=True)
    escala_min = IntegerField()
    escala_max = IntegerField()

    class Meta:
        table_name = "preguntaescala"