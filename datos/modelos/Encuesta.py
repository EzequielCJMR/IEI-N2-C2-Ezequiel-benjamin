from peewee import TextField, CharField, DateField, IntegerField, AutoField, SQL
from datos.modelos.base import BaseModel


class Encuesta(BaseModel):
    id_encuesta = AutoField(primary_key=True)
    titulo = CharField(max_length=100)
    descripcion = TextField(null=True)
    estado = CharField(
        constraints=[SQL("DEFAULT 'BORRADOR'")], max_length=20, null=True
    )
    fecha_creacion = DateField(constraints=[SQL("DEFAULT curdate()")], null=True)
    fecha_expiracion = DateField(null=True)
    id_admin = IntegerField(index=True)
    id_categoria = IntegerField(index=True, null=True)

    class Meta:
        table_name = "encuesta"