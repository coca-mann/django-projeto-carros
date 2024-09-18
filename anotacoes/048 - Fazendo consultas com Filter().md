### Fazendo Consultas com `filter()` no Django ORM

O método `filter()` do Django ORM permite realizar consultas filtradas no banco de dados, retornando apenas os registros que correspondem a certas condições. Neste exemplo, utilizamos o filtro para buscar carros cuja marca (brand) está relacionada a outra tabela, no caso, a tabela `Brand`. 

#### 1. **Exemplo de View com Filtro**

No arquivo `views.py`, utilizamos o método `filter()` para trazer todos os carros onde a marca seja "Ford". A consulta é realizada usando uma chave estrangeira (ForeignKey) que aponta para a tabela `Brand`.

```python
from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    # Consulta os carros filtrando pela marca 'Ford'
    cars = Car.objects.filter(brand__name='Ford')

    # Renderiza a página com a lista de carros filtrados
    return render(
        request,
        'cars.html',
        {'cars': cars}
    )
```

#### Explicação Detalhada

- **`Car.objects.filter(brand__name='Ford')`**: Neste comando, `filter()` busca todos os carros cujo campo `brand.name` seja igual a "Ford". O Django ORM usa a sintaxe `brand__name` para acessar o atributo `name` do modelo `Brand`, que está relacionado ao modelo `Car` através da chave estrangeira `brand`.
  
- **Chave Estrangeira (`ForeignKey`)**: O campo `brand` no modelo `Car` é uma chave estrangeira que referencia o modelo `Brand`. Isso permite que a consulta seja feita de maneira relacional entre as duas tabelas.

#### 2. **Modelo Car e Brand**

Abaixo estão os modelos `Brand` e `Car` no arquivo `models.py`. Note que a tabela `Car` possui uma relação de chave estrangeira com a tabela `Brand`, o que permite realizar filtros com base nas marcas.

```python
from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='brands')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='type', null=True, blank=True)

    def __str__(self):
        return self.model
```

#### Explicação dos Modelos

- **`Brand`**: Este modelo representa a tabela de marcas de carros. Ele possui um campo `name` que armazena o nome da marca, como "Ford" ou "Chevrolet". O método `__str__` retorna o nome da marca como sua representação em string.
  
- **`Car`**: O modelo `Car` possui uma chave estrangeira (`ForeignKey`) para o modelo `Brand`, o que significa que cada carro está associado a uma marca específica. O parâmetro `related_name='brands'` permite que possamos acessar os carros relacionados a uma marca através do ORM usando `brand.brands.all()`.

#### 3. **Template para Exibir os Carros Filtrados**

No arquivo `cars.html`, podemos ajustar o template para exibir os carros retornados pela consulta.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meus Carros</title>
</head>
<body>
    <h1>Carros da marca Ford</h1>
    <ul>
        {% for car in cars %}
            <li>{{ car.brand.name }} {{ car.model }} - Ano: {{ car.factory_year }}</li>
        {% empty %}
            <li>Nenhum carro encontrado.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

Neste template:
- **`{{ car.brand.name }}`**: Exibe o nome da marca relacionada ao carro.
- **`{% for car in cars %}`**: Faz um loop sobre os carros filtrados pela marca "Ford". Caso nenhum carro seja encontrado, o bloco `{% empty %}` exibe uma mensagem informando que não há carros disponíveis.

Dessa forma, podemos usar o `filter()` do Django ORM para buscar carros com base em atributos relacionados em outras tabelas, simplificando a consulta e o uso de chaves estrangeiras.