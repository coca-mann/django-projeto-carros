# Configurando o *Base Template* no Django

No Django, é comum criar um **template base** que será reutilizado em várias páginas do projeto, ajudando a manter uma estrutura consistente e facilitando a manutenção do código. O template base pode conter elementos comuns como cabeçalho, rodapé e links para arquivos de CSS e JavaScript. Neste exemplo, vamos criar o *base template* e configurá-lo para ser reutilizado no template do app `cars`.

## Passo 1: Criar o Diretório de Templates

Primeiro, crie um diretório chamado `templates` dentro da pasta do seu app, por exemplo `cars/templates/`. Esse diretório armazenará todos os arquivos HTML do seu app.

## Passo 2: Criar o *Base Template*

No diretório `templates`, crie um arquivo chamado `base.html`. Este arquivo será a estrutura principal do seu site, com blocos que podem ser sobrescritos em páginas específicas.

**Exemplo de `base.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Meu Site{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <header>
        <h1>Bem-vindo ao Meu Site</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/cars/">Carros</a></li>
            </ul>
        </nav>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>&copy; 2024 Meu Site. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
```

- **Bloco `{% block title %}`**: Este bloco permite que o título da página seja personalizado em cada template que herda de `base.html`.
- **Bloco `{% block content %}`**: Este bloco é onde o conteúdo específico de cada página será inserido.
- **Link de CSS**: O link para o arquivo `style.css` usa a tag `{% static %}`, que carrega arquivos estáticos como CSS.

## Passo 3: Configurar o Caminho de Templates no `settings.py`

Agora, configure o Django para reconhecer a pasta `templates` criada no app. Abra o arquivo `settings.py` e verifique se o diretório está incluído na configuração `TEMPLATES`.

**Exemplo de `settings.py`:**
```python
import os

# Diretório de templates do projeto
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Diretório de templates do projeto
        'APP_DIRS': True,  # Permite que o Django busque templates dentro dos apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Essa configuração permite que o Django procure templates tanto em um diretório global de templates (caso seja configurado) quanto nos diretórios `templates` dos apps.

## Passo 4: Criar um Template Específico para o App

Agora, crie o template específico para o app `cars`. Dentro do diretório `cars/templates/`, crie um arquivo chamado `cars.html`.

**Exemplo de `cars.html`:**
```html
{% extends 'base.html' %}

{% block title %}Meus Carros{% endblock %}

{% block content %}
    <h2>Lista de Carros</h2>
    <ul>
        {% for car in cars %}
            <li>{{ car.brand.name }} - {{ car.model }} ({{ car.factory_year }})</li>
        {% empty %}
            <li>Nenhum carro encontrado.</li>
        {% endfor %}
    </ul>
{% endblock %}
```

- **`{% extends 'base.html' %}`**: Este comando informa que `cars.html` herda a estrutura do template `base.html`.
- **`{% block title %}`**: O título da página será substituído por "Meus Carros".
- **`{% block content %}`**: Todo o conteúdo dentro desse bloco será exibido no lugar do bloco `content` definido no `base.html`.

## Passo 5: Adicionar Estilos ao Projeto

No diretório `static/css/`, crie o arquivo `style.css` com alguns estilos básicos.

**Exemplo de `style.css`:**
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 0;
}

header, footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 10px;
}

h1, h2 {
    color: #333;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    background-color: #fff;
    margin: 5px 0;
    padding: 10px;
    border: 1px solid #ddd;
}
```

Esse arquivo define o estilo da página, como as cores e o layout básico.

## Passo 6: Ajustar a View para Renderizar o Template

No arquivo `views.py`, ajuste a função da view para renderizar o template `cars.html`.

**Exemplo de `views.py`:**
```python
from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})
```

Aqui, a função `cars_view` busca todos os carros no banco de dados e renderiza o template `cars.html`, passando os dados de carros no contexto.
