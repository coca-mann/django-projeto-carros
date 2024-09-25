# Utilizando CreateView

No Django, a **CreateView** é uma **Class-Based View** (CBV) especializada em facilitar a criação de novos registros no banco de dados. Ela encapsula toda a lógica necessária para exibir um formulário, validar os dados, e salvar o novo objeto, reduzindo significativamente a quantidade de código que precisamos escrever.

Abaixo, vamos ver como configurar uma `CreateView` para criar novos registros de carros utilizando o modelo `Car` e o formulário `CarModelForm`.

---

### Exemplo da `NewCarCreateView` utilizando `CreateView`

```python
from django.views.generic.edit import CreateView
from cars.models import Car
from cars.forms import CarModelForm

class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'
```

---

## Explicação das Etapas:

### 1. **Herança da Classe `CreateView`**:
   A `NewCarCreateView` herda da classe genérica `CreateView`, que já possui implementada toda a lógica necessária para criar um novo objeto a partir de um formulário, como a exibição do formulário, a validação dos dados e o salvamento no banco de dados.

### 2. **Definição dos Atributos**:

- **`model`**: Aqui, especificamos o modelo `Car`, que será o alvo da criação de novos registros.

- **`form_class`**: Este atributo indica qual formulário será utilizado para capturar os dados. No caso, utilizamos `CarModelForm`, que já define os campos e validações necessárias para o modelo `Car`.

- **`template_name`**: Define o template que será renderizado para exibir o formulário. Neste exemplo, o template `'new_car.html'` será utilizado.

- **`success_url`**: Após o formulário ser submetido com sucesso (ou seja, após o novo carro ser salvo no banco de dados), o usuário será redirecionado para a URL especificada. Neste caso, o usuário será redirecionado para a página de listagem de carros (`'/cars/'`).

---

## Template (`new_car.html`)

No template, renderizamos o formulário `CarModelForm` utilizando o nome de contexto padrão `form`. Abaixo está o código HTML do template:

```html
{% extends "base.html" %}

{% block content %}
    <form enctype="multipart/form-data" method="post">
        {% csrf_token %}

        <table>
            {{ form.as_table }}
        </table>

        <input type="submit" value="Cadastrar" class="btn btn-primary">
    </form>
{% endblock %}
```

## Explicação do Template:

- **Formulário HTML**: Utiliza o método `POST` para enviar os dados do formulário, e `enctype="multipart/form-data"` é necessário para permitir o upload de arquivos, como imagens de carros.

- **CSRF Token**: É obrigatório em formulários Django para proteger contra ataques CSRF (Cross-Site Request Forgery).

- **Renderização do Formulário**: A variável `form` (definida na view `CreateView`) é renderizada no template utilizando `{{ form.as_table }}`, o que gera uma tabela HTML com todos os campos do formulário.

- **Botão de Submissão**: O botão de submissão `Cadastrar` envia o formulário quando clicado, e o Django cuida do resto, incluindo a validação dos dados e o redirecionamento para a URL de sucesso.
