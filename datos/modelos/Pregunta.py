from peewee import CharField, IntegerField, AutoField, BooleanField, SQL
from datos.modelos.base import BaseModel


class Pregunta(BaseModel):
    id_pregunta = AutoField()
    id_encuesta = IntegerField(index=True)
    texto = CharField()
    tipo = CharField()
    orden = IntegerField()
    obligatoria = BooleanField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = "pregunta"