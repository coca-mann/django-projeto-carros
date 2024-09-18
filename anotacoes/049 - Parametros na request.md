# Parâmetros da `request` no Django

Quando uma URL é acessada com parâmetros enviados via **query string** (ex.: `?param=value`), esses valores podem ser obtidos na view utilizando o objeto `request.GET`. O Django oferece uma maneira simples de capturar esses parâmetros e usá-los em sua lógica de aplicação.

## Exemplo de URL com Parâmetros

```plaintext
http://localhost:8000/cars/?brand=Ford&year=2020
```

Nesta URL, estamos enviando dois parâmetros: `brand` com o valor "Ford" e `year` com o valor "2020". Esses valores podem ser acessados na view através de `request.GET`.

## Exemplo de View que Obtém Parâmetros da URL

No arquivo `views.py`, podemos capturar esses parâmetros usando `request.GET` e usá-los para filtrar dados, por exemplo.

```python
from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    # Obtém os parâmetros 'brand' e 'year' da URL
    brand = request.GET.get('brand')
    year = request.GET.get('year')

    # Inicia um queryset vazio
    cars = Car.objects.all()

    # Se o parâmetro 'brand' for fornecido, filtra pelo nome da marca
    if brand:
        cars = cars.filter(brand__name=brand)

    # Se o parâmetro 'year' for fornecido, filtra pelo ano de fabricação
    if year:
        cars = cars.filter(factory_year=year)

    # Renderiza o template com os carros filtrados
    return render(
        request,
        'cars.html',
        {'cars': cars}
    )
```

## Explicação do Código

- **`request.GET.get('brand')`**: Obtém o valor do parâmetro `brand` enviado na URL. Se o parâmetro não for fornecido, o método `get()` retornará `None`.
  
- **Filtragem Condicional**: Se o parâmetro `brand` ou `year` estiver presente, o **QuerySet** será filtrado com base nesses valores. Por exemplo, se `brand` for "Ford", a consulta será filtrada para exibir apenas os carros da marca Ford.

- **Renderização do Template**: Após obter e filtrar os carros com base nos parâmetros, o template `cars.html` é renderizado e recebe os dados filtrados.

## Template para Exibir os Carros Filtrados

O arquivo `cars.html` pode ser ajustado para exibir a lista de carros filtrados.

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
            <li>{{ car.brand.name }} {{ car.model }} - Ano: {{ car.factory_year }}</li>
        {% empty %}
            <li>Nenhum carro encontrado.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

## Como Utilizar

Se você acessar a URL `http://localhost:8000/cars/?brand=Ford&year=2020`, a view irá buscar no banco de dados todos os carros da marca Ford fabricados no ano de 2020 e exibi-los no template. Se os parâmetros não forem fornecidos, a consulta será feita sem filtro, retornando todos os carros.