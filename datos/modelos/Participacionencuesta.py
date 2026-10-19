from peewee import BooleanField, DateField, IntegerField, AutoField, SQL
from datos.modelos.base import BaseModel


class Participacionencuesta(BaseModel):
    id_participacion = AutoField()
    id_encuesta = IntegerField(index=True)
    id_encuestado = IntegerField(index=True)
    fecha_participacion = DateField(constraints=[SQL("DEFAULT curdate()")], null=True)
    completada = BooleanField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = "participacionencuesta"