# Linguagem de Templates do Django e Uso de Contexto com Herança de Templates

A **Linguagem de Templates** do Django facilita a criação de páginas dinâmicas, permitindo que variáveis e estruturas de controle sejam inseridas diretamente no HTML. Além disso, o Django suporta **herança de templates**, que ajuda a reutilizar código e criar layouts mais organizados.

Neste exemplo, vamos passar dados da view para o template utilizando o **contexto**, e ao mesmo tempo, entender como a herança de templates funciona.

## 1. **Herança de Templates**

A herança de templates é uma forma de criar um layout base que pode ser reutilizado em diferentes páginas do seu projeto. Com isso, você pode definir uma estrutura comum (como cabeçalho e rodapé) e substituir apenas partes específicas da página, como o conteúdo principal.

Neste exemplo, usamos as tags `{% block %}` e `{% endblock %}` para definir seções que podem ser substituídas em outros templates.

## 2. **Passando Contexto para o Template**

Para enviar dados dinâmicos do servidor para o template, usamos a função `render`, passando um dicionário com o contexto. O contexto é utilizado no template para exibir valores.

No arquivo `views.py`, criamos uma função `cars_view` que passa um modelo de carro (no contexto) para o template:

```python
from django.shortcuts import render

def cars_view(request):
    return render(
        request,
        'cars.html',
        {'cars': {'model': 'Astra 2.0'}}
    )
```

- **Contexto**: O dicionário `{'cars': {'model': 'Astra 2.0'}}` é passado para o template, onde a chave `'cars'` contém os detalhes do carro, como o modelo `'Astra 2.0'`.

## 3. **Estrutura de um Template com Herança**

No arquivo `cars.html`, temos um exemplo de como herdar um layout base e inserir conteúdo dinâmico. Vamos analisar o HTML:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Meus carros</title>
    </head>
    {% block content %}
        <body>
            <h1>Carro 1: {{ cars.model }}</h1>
        </body>
    {% endblock %}
</html>
```

### Explicação do HTML

- **`<!DOCTYPE html>`**: Define o tipo de documento HTML, informando ao navegador que estamos utilizando HTML5.
- **`<html lang="en">`**: A tag `<html>` define a estrutura do documento, e o atributo `lang="en"` especifica que a linguagem do conteúdo é inglês.
- **`<meta charset="UTF-8">`**: Define a codificação de caracteres como UTF-8, que permite suportar uma ampla variedade de caracteres.
- **`<meta name="viewport" content="width=device-width, initial-scale=1.0">`**: Define a exibição da página para dispositivos móveis, garantindo que o layout seja responsivo.
- **`<title>Meus carros</title>`**: Define o título da página que será exibido na aba do navegador.
- **`{% block content %}` e `{% endblock %}`**: São usadas para definir uma seção substituível do template. Qualquer conteúdo entre essas tags pode ser sobrescrito por outro template que herde este.
- **`{{ cars.model }}`**: Insere o valor dinâmico da variável `model` dentro da chave `cars` do contexto. Nesse caso, o valor "Astra 2.0" será exibido.

## 4. **Passo a Passo para Passar o Contexto e Renderizar o Template**

1. **Crie a View**: No arquivo `views.py`, use a função `render` para passar o contexto contendo os dados do carro.

```python
from django.shortcuts import render

def cars_view(request):
    return render(
        request,
        'cars.html',
        {'cars': {'model': 'Astra 2.0'}}
    )
```

2. **Crie o Template**: No arquivo `cars.html`, crie o layout HTML com a herança de templates e o uso de variáveis.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Meus carros</title>
    </head>
    {% block content %}
        <body>
            <h1>Carro 1: {{ cars.model }}</h1>
        </body>
    {% endblock %}
</html>
```

3. **Mapeie a URL**: No arquivo `urls.py`, mapeie a URL `/cars/` para a função `cars_view`.

```python
from django.urls import path
from .views import cars_view

urlpatterns = [
    path('cars/', cars_view),
]
```

## 5. **Expansão: Adicionando Mais Carros**

Se você quiser passar mais de um carro no contexto, basta alterar o dicionário na view. Por exemplo:

```python
def cars_view(request):
    return render(
        request,
        'cars.html',
        {'cars': [
            {'model': 'Astra 2.0'},
            {'model': 'Civic 1.8'},
            {'model': 'Corolla 2.0'}
        ]}
    )
```

No template, você poderia usar um loop `{% for %}` para listar os carros:

```html
{% block content %}
    <body>
        <h1>Lista de Carros:</h1>
        <ul>
            {% for car in cars %}
                <li>{{ car.model }}</li>
            {% endfor %}
        </ul>
    </body>
{% endblock %}
```
