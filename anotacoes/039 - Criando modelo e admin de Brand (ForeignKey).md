# Criando Modelo e Admin de Marcas com ForeignKey

Ao criar um sistema para gerenciar carros e suas marcas, você pode usar o relacionamento de chave estrangeira (`ForeignKey`) para associar carros a marcas. Além disso, podemos adicionar o argumento `related_name` para facilitar o acesso inverso, e proteger a exclusão de marcas que possuem carros associados.

## 1. **Criando o Modelo `Brand`**
Primeiro, criamos o modelo `Brand` para representar as marcas. Esse modelo será relacionado ao modelo `Car` usando uma chave estrangeira.

No arquivo `models.py`, adicione o seguinte código:

```python
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

- **`name`**: Armazena o nome da marca (ex. "Toyota", "Honda").
- **`__str__`**: Define a representação em texto de uma instância do modelo `Brand`, retornando o nome da marca.

## 2. **Alterando o Modelo `Car` para Usar `Brand` com ForeignKey, `related_name` e Proteção Contra Exclusão**
Agora, alteramos o modelo `Car` para associá-lo ao modelo `Brand` usando uma chave estrangeira com proteção contra exclusão e adicionamos o parâmetro `related_name` para facilitar o acesso aos carros a partir de uma marca.

Atualize o modelo `Car` em `models.py`:

```python
class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.model_year})"
```

- **`brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars')`**: 
  - **`on_delete=models.PROTECT`**: Protege contra a exclusão de uma marca se houver carros associados a ela. Tentar excluir uma marca que tenha carros associados resultará em um erro.
  - **`related_name='cars'`**: Permite o acesso aos carros de uma marca através do atributo `cars`. Por exemplo, a partir de uma instância de `Brand`, você pode acessar todos os carros associados com `brand.cars.all()`.
  
- O método `__str__` é usado para exibir o nome da marca seguido pelo modelo do carro e o ano do modelo.

## 3. **Atualizando o Admin para `Brand` e `Car`**

Para gerenciar tanto as marcas quanto os carros no admin do Django, registre ambos os modelos no arquivo `admin.py` e personalize a exibição.

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

- **`BrandAdmin`**: Gerencia as marcas na interface administrativa, permitindo a listagem e a busca por marcas.
- **`CarAdmin`**: Gerencia os carros, exibindo o campo `brand` como uma chave estrangeira e permitindo a busca por marca.

## 4. **Criando e Aplicando as Migrações**

Após fazer as alterações no modelo, crie e aplique as migrações para refletir as mudanças no banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```
