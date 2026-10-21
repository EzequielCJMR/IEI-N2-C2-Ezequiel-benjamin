from peewee import AutoField, CharField, TextField
from datos.modelos.base import BaseModel

class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre = CharField(max_length=50)
    descripcion = TextField(null=True)

    class Meta:
        table_name = "categoria"