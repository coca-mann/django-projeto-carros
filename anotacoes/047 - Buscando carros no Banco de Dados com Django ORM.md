# Buscando Carros no Banco de Dados com Django ORM

O Django ORM (Object-Relational Mapping) facilita a interação com o banco de dados sem a necessidade de escrever SQL diretamente. Neste exemplo, vamos configurar uma view que busca carros no banco de dados e os exibe em um template.

## 1. **Criando o Modelo de Carros**

Primeiro, defina o modelo `Car` no arquivo `models.py`, que representa a tabela de carros no banco de dados:

```python
from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.model
```

Esse modelo cria uma tabela no banco de dados com colunas para o modelo do carro, marca, ano de fabricação, ano do modelo e valor. O método `__str__` define como o objeto será representado quando for convertido em uma string.

Depois de criar o modelo, execute as migrações para aplicar essas mudanças ao banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 2. **Configurando a View para Buscar Carros**

Agora, crie uma função de view no arquivo `views.py` para buscar os carros usando o Django ORM e passar esses dados para o template.

```python
from django.shortcuts import render
from .models import Car

def cars_view(request):
    # Utiliza o Django ORM para buscar todos os registros de carros no banco de dados.
    cars = Car.objects.all()

    # A função 'render' combina o template 'cars.html' com o contexto fornecido (neste caso, a lista de carros)
    # e retorna o resultado como uma resposta HTTP.
    return render(
        request,          # O objeto request, necessário para processar a requisição HTTP.
        'cars.html',      # O template que será renderizado.
        {'cars': cars}    # O contexto, passando a lista de carros que será utilizada no template.
    )
```

## Explicação Detalhada da View

- **`Car.objects.all()`**: O Django ORM oferece o método `all()` para buscar todos os registros do modelo `Car` no banco de dados. Esse método retorna um **QuerySet**, que é essencialmente uma lista de objetos `Car` contendo todos os registros da tabela de carros.
  
- **`render(request, 'cars.html', {'cars': cars})`**: A função `render` combina o template HTML com os dados do contexto fornecido. Neste caso, o contexto é um dicionário `{'cars': cars}`, onde a chave `'cars'` contém o resultado da consulta do ORM, ou seja, a lista de carros. O template `cars.html` utilizará esse contexto para exibir os dados na página.

## 3. **Ajustando o Template para Exibir os Carros**

No arquivo `cars.html`, use um loop para exibir cada carro da lista passada pela view. Se a lista estiver vazia, uma mensagem apropriada será exibida.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meus Carros</title>
</head>
<body>
    <h1>Lista de Carros</h1>
    <ul>
        {% for car in cars %}
            <li>{{ car.brand }} {{ car.model }} - Ano de Fabricação: {{ car.factory_year }} - Ano do Modelo: {{ car.model_year }} - Valor: R$ {{ car.value }}</li>
        {% empty %}
            <li>Nenhum carro disponível.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

- **`{% for car in cars %}`**: Este loop percorre a lista de carros passada no contexto pela view. Para cada carro, os atributos como marca, modelo, ano de fabricação, ano do modelo e valor são exibidos.
  
- **`{% empty %}`**: Caso a lista `cars` esteja vazia, esta tag exibe uma mensagem dizendo que nenhum carro está disponível.

- **`{{ car.brand }}`, `{{ car.model }}`, etc.**: São placeholders que serão substituídos pelos valores correspondentes no contexto. Eles acessam os atributos de cada objeto `Car` retornado pelo ORM.

## 4. **Mapeando a URL**

Por fim, no arquivo `urls.py`, adicione o caminho para a view `cars_view`, para que ela seja acessível a partir de uma URL específica.

```python
from django.urls import path
from .views import cars_view

urlpatterns = [
    path('cars/', cars_view),
]
```

Com isso, quando você acessar `/cars/` no navegador, a view buscará todos os carros no banco de dados e os exibirá na página usando o template configurado.