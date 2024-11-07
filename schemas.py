from ninja import ModelSchema, Schema, Schema
from .models import Livros

class LivroSchema(ModelSchema):
    class Meta:
        model = Livros
        fields = ['nome', 'streaming', 'categorias']

class AvaliacaoSchema(ModelSchema):
    class Meta:
        model = Livros
        fields = ['nota', 'comentarios']

class FiltrosSortear(Schema):
    nota_minima: int = None
    categorias: int = None
    reassistir: bool = False

class LivrosViewSchema(ModelSchema):
    class Meta:
        model = Livros
        fields = ['id', 'nome', 'streaming', 'categorias']