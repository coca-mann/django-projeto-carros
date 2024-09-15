# Criando Modelo e Admin de Marcas com ForeignKey

Ao criar um sistema de gerenciamento de carros, é comum que cada carro esteja associado a uma marca (brand). Para isso, podemos criar um modelo separado chamado `Brand` e referenciar esse modelo no nosso modelo `Car` usando um relacionamento de chave estrangeira (`ForeignKey`). Isso melhora a organização dos dados e evita a repetição de informações de marcas.

## 1. **Criando o Modelo `Brand`**
Primeiro, criamos o modelo `Brand` para representar as marcas de carros. Esse modelo será referenciado pelo modelo `Car` através de uma chave estrangeira (ForeignKey).

No arquivo `models.py`, adicione o seguinte código:

```python
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

- **`name`**: Armazena o nome da marca (ex. "Toyota", "Honda").
- **`__str__`**: Define como as instâncias de `Brand` serão representadas em texto, retornando o nome da marca.

## 2. **Alterando o Modelo `Car` para Usar `Brand` com ForeignKey**
Agora, alteramos o modelo `Car` para associar cada carro a uma marca usando uma chave estrangeira (`ForeignKey`). Em vez de armazenar a marca como um simples campo de texto, usamos uma relação com o modelo `Brand`.

Atualize o modelo `Car` em `models.py`:

```python
class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.model_year})"
```

- **`brand = models.ForeignKey(Brand, on_delete=models.CASCADE)`**: Estabelece a relação de chave estrangeira com o modelo `Brand`. O parâmetro `on_delete=models.CASCADE` indica que, se uma marca for deletada, todos os carros associados também serão removidos.
- O método `__str__` agora usa `brand.name` para exibir o nome da marca ao lado do modelo do carro.

## 3. **Atualizando o Admin para `Brand` e `Car`**

Para gerenciar tanto as marcas quanto os carros na interface administrativa do Django, você precisa registrar ambos os modelos no arquivo `admin.py` e personalizar a exibição.

No arquivo `admin.py`, adicione:

```python
from django.contrib import admin
from .models import Car, Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand__name')
    list_filter = ('brand', 'factory_year', 'model_year')
```

- **`BrandAdmin`**: Define como as marcas (`Brand`) serão exibidas e gerenciadas no admin. Você pode listar e buscar pelas marcas.
- **`CarAdmin`**: Atualizado para exibir o campo `brand` como um relacionamento de chave estrangeira e permite buscar por marcas através de `brand__name`.

#### 4. **Criando e Aplicando as Migrações**

Após alterar os modelos, crie e aplique as migrações para atualizar o banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

