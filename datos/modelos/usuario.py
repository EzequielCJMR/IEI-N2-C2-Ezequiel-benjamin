from peewee import AutoField, CharField, DateField, BooleanField, SQL
from datos.modelos.base import BaseModel


class Usuario(BaseModel):
    id_usuario = AutoField()
    nombre = CharField(max_length=50)
    rut = CharField(max_length=20, unique=True)
    email = CharField(max_length=100, unique=True)
    contrasena = CharField(max_length=100)
    rol = CharField()
    activo = BooleanField(constraints=[SQL("DEFAULT 1")], null=True)
    fecha_registro = DateField(constraints=[SQL("DEFAULT curdate()")], null=True)

    class Meta:
        table_name = "usuario"