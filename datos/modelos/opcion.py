from peewee import CharField, IntegerField, AutoField, SQL
from datos.modelos.base import BaseModel


class Opcion(BaseModel):
    id_opcion = AutoField()
    id_pregunta = IntegerField(index=True)
    texto = CharField()
    contador_votos = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = "opcion"