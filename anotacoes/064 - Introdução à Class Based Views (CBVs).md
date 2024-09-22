# Introdução às Class Based Views (CBVs) no Django

As **Class Based Views (CBVs)** no Django são uma forma alternativa de criar views, usando classes em vez de funções. Elas permitem uma maior modularidade e reutilização de código, especialmente quando há necessidade de realizar operações repetitivas ou comuns em diferentes views.

## Diferença entre Function Based Views (FBVs) e Class Based Views (CBVs)
- **FBVs** são implementadas como funções simples que recebem uma requisição e retornam uma resposta.
- **CBVs** utilizam classes para organizar a lógica da view em métodos, permitindo a reutilização de comportamento, o que torna o código mais limpo e estruturado, principalmente em cenários mais complexos.

## Vantagens das Class Based Views:
- **Reutilização de código**: Como as CBVs são baseadas em herança, elas permitem a criação de views que compartilham comportamento, diminuindo a duplicação de código.
- **Modularidade**: É fácil estender e modificar o comportamento de views individuais, adicionando ou sobrescrevendo métodos em subclasses.
- **Estrutura clara**: Em cenários complexos, como a manipulação de formulários e listagens, CBVs oferecem uma estrutura mais organizada do que FBVs.

## Exemplo de CBV: `ListView`
O **`ListView`** é uma CBV que facilita a listagem de objetos de um determinado modelo no Django.

Aqui está um exemplo básico de como usar a **`ListView`** para listar os carros do modelo **Car**:

```python
from django.views.generic import ListView
from cars.models import Car

class CarListView(ListView):
    model = Car  # O modelo que será listado
    template_name = 'car_list.html'  # O template que será renderizado
    context_object_name = 'cars'  # O nome da variável no contexto do template
```

Neste exemplo:
- **`model`** define o modelo que será listado.
- **`template_name`** especifica qual template será utilizado para renderizar a página.
- **`context_object_name`** define o nome da variável que será usada no template para acessar os dados.

## Configurando a Rota para a CBV no `urls.py`:

```python
from django.urls import path
from cars.views import CarListView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),  # Associando a CBV com a rota
]
```

## Exemplo de Template (`car_list.html`):

```html
{% extends 'base.html' %}

{% block content %}
    <h1>Lista de Carros</h1>
    <ul>
        {% for car in cars %}
            <li>{{ car.model }} - {{ car.brand.name }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

## Tipos Comuns de Class Based Views:
- **`ListView`**: Para listar objetos.
- **`DetailView`**: Para exibir os detalhes de um único objeto.
- **`CreateView`**: Para criar novos objetos com formulários.
- **`UpdateView`**: Para editar objetos existentes.
- **`DeleteView`**: Para excluir objetos.

### 1. **`TemplateView`**
A `TemplateView` é uma CBV básica que simplesmente renderiza um template HTML sem interagir diretamente com um modelo ou banco de dados. Ela é útil quando você só precisa exibir uma página estática ou adicionar dados básicos ao contexto.

**Exemplo:**
```python
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
```

**Uso:**
- Exibição de páginas estáticas como páginas de contato, "sobre", etc.

---

### 2. **`ListView`**
A `ListView` é usada para exibir uma lista de objetos de um determinado modelo. Ela fornece automaticamente um conjunto de dados do modelo no contexto do template.

**Exemplo:**
```python
from django.views.generic import ListView
from cars.models import Car

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'
```

**Uso:**
- Listar objetos de um banco de dados, como uma lista de produtos, posts de blog, etc.

**Parâmetros Comuns:**
- `model`: Define o modelo que será listado.
- `template_name`: Especifica o template para renderizar a view.
- `context_object_name`: Define o nome da variável que será usada no template para acessar a lista de objetos.

---

### 3. **`DetailView`**
A `DetailView` é usada para exibir os detalhes de um único objeto. Ela recupera automaticamente o objeto do banco de dados com base no `id` ou `slug` fornecido na URL.

**Exemplo:**
```python
from django.views.generic import DetailView
from cars.models import Car

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'
```

**Uso:**
- Exibir os detalhes de um objeto específico, como um perfil de usuário ou a descrição de um produto.

**Parâmetros Comuns:**
- `model`: O modelo que será usado para buscar o objeto.
- `context_object_name`: Nome da variável no template.

---

### 4. **`CreateView`**
A `CreateView` é usada para exibir um formulário de criação de objetos e salvar o novo objeto no banco de dados, se o formulário for válido.

**Exemplo:**
```python
from django.views.generic import CreateView
from cars.models import Car
from django.urls import reverse_lazy

class CarCreateView(CreateView):
    model = Car
    fields = ['model', 'brand', 'factory_year', 'model_year', 'value']
    template_name = 'car_form.html'
    success_url = reverse_lazy('car_list')  # Redireciona após a criação
```

**Uso:**
- Criar novos registros no banco de dados, como um novo post de blog ou um novo produto.

**Parâmetros Comuns:**
- `fields`: Lista de campos do modelo que devem ser incluídos no formulário.
- `success_url`: URL para redirecionar após o sucesso da criação.

---

### 5. **`UpdateView`**
A `UpdateView` permite a edição de objetos existentes. Ela exibe um formulário pré-preenchido com os dados do objeto e salva as alterações, se o formulário for válido.

**Exemplo:**
```python
from django.views.generic import UpdateView
from cars.models import Car
from django.urls import reverse_lazy

class CarUpdateView(UpdateView):
    model = Car
    fields = ['model', 'brand', 'factory_year', 'model_year', 'value']
    template_name = 'car_form.html'
    success_url = reverse_lazy('car_list')
```

**Uso:**
- Editar registros já existentes no banco de dados.

**Parâmetros Comuns:**
- `fields`: Lista de campos do modelo a serem editados.
- `success_url`: URL para redirecionar após o sucesso da edição.

---

### 6. **`DeleteView`**
A `DeleteView` é usada para excluir objetos do banco de dados. Ela exibe uma página de confirmação e remove o objeto após a confirmação do usuário.

**Exemplo:**
```python
from django.views.generic import DeleteView
from cars.models import Car
from django.urls import reverse_lazy

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = reverse_lazy('car_list')
```

**Uso:**
- Excluir objetos do banco de dados, como a exclusão de uma conta de usuário ou produto.

**Parâmetros Comuns:**
- `success_url`: URL para redirecionar após a exclusão.

---

### 7. **`FormView`**
A `FormView` oferece uma maneira flexível de lidar com formulários sem estar diretamente ligada a um modelo específico. Ela pode ser usada para qualquer tipo de formulário personalizado.

**Exemplo:**
```python
from django.views.generic import FormView
from cars.forms import ContactForm
from django.urls import reverse_lazy

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('thank_you')
```

**Uso:**
- Lidar com formulários que não estão necessariamente relacionados a um modelo, como formulários de contato.
