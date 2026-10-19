from peewee import TextField, DateField, IntegerField, AutoField, SQL
from datos.modelos.base import BaseModel


class Respuesta(BaseModel):
    fecha_respuesta = DateField(constraints=[SQL("DEFAULT curdate()")], null=True)
    id_participacion = IntegerField(index=True)
    id_pregunta = IntegerField(index=True)
    id_respuesta = AutoField()
    valor = TextField()

    class Meta:
        table_name = "respuesta"