# Retornando Templates para o Usuário no Django

No Django, em vez de retornar diretamente texto nas **Views**, é possível e recomendado retornar páginas HTML completas, utilizando **templates**. Os templates permitem separar a lógica Python do layout da interface de usuário, tornando o desenvolvimento mais organizado.

## 1. **Criando a Pasta de Templates**

A estrutura do Django permite que os arquivos HTML sejam organizados em uma pasta chamada **templates** dentro do diretório da aplicação. Para começar, siga os seguintes passos:

- Dentro do diretório da sua aplicação, crie uma pasta chamada `templates`.
- Dentro dessa pasta, crie um arquivo HTML básico, como `cars.html`.

A estrutura de pastas será algo como:

```
my_project/
    cars/
        templates/
            cars.html
        views.py
        urls.py
```

## 2. **Criando um Template HTML**

No arquivo `templates/cars.html`, adicione um conteúdo HTML básico:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Meus Carros</title>
</head>
<body>
    <h1>Lista de Carros</h1>
    <p>Aqui estão os meus carros!</p>
</body>
</html>
```

Este arquivo será o template que será renderizado e retornado como resposta ao usuário.

## 3. **Ajustando a View para Retornar o Template**

Agora, vamos ajustar a função **View** para renderizar o template HTML em vez de retornar um `HttpResponse` simples. Para isso, utilizamos a função `render` do Django, que combina o template com o contexto (dados) e retorna uma página HTML completa.

No arquivo `views.py`, modifique a função `cars_view` da seguinte forma:

```python
from django.shortcuts import render

def cars_view(request):
    return render(request, 'cars.html')
```

- **`render(request, 'cars.html')`**: O Django procura o arquivo `cars.html` na pasta `templates` da sua aplicação e o retorna como resposta ao usuário. Aqui, estamos apenas retornando o template, mas também podemos passar dados adicionais (como uma lista de carros) no contexto, se necessário.

## 4. **Passo a Passo Resumido**

1. **Crie a Pasta e o Template**: No diretório da aplicação, crie a pasta `templates` e o arquivo HTML (ex. `cars.html`) que servirá de página para o usuário.
2. **Ajuste a View**: No arquivo `views.py`, utilize a função `render` para retornar o template HTML.
3. **Acesse no Navegador**: Quando o usuário acessar a URL configurada (ex. `http://seusite.com/cars/`), o template HTML será exibido no navegador.
