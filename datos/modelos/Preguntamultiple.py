from peewee import IntegerField, BooleanField, SQL
from datos.modelos.base import BaseModel


class Preguntamultiple(BaseModel):
    id_pregunta = IntegerField(primary_key=True)
    permite_multiple = BooleanField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = "preguntamultiple"