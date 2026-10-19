from peewee import DateField, IntegerField, AutoField, SQL
from datos.modelos.base import BaseModel


class Reporte(BaseModel):
    id_reporte = AutoField()
    id_encuesta = IntegerField(index=True)
    fecha_generacion = DateField(constraints=[SQL("DEFAULT curdate()")], null=True)
    total_participantes = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    total_respuestas = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = "reporte"