# Utilizando UpdateView (Generic Views)

A **UpdateView** é uma **Class-Based View (CBV)** do Django que facilita a atualização de objetos existentes no banco de dados. Quando você utiliza a `UpdateView`, o Django gera automaticamente um formulário baseado no modelo especificado, permitindo que o usuário edite e salve as alterações de forma eficiente.

Aqui vamos criar a funcionalidade de edição para os carros já cadastrados em nosso sistema, permitindo que o usuário edite suas informações e salve as alterações.

---

### 1. **Criação da View `CarUpdateView`**

A `CarUpdateView` é uma classe que herda de `UpdateView`, utilizada para editar os detalhes de um carro específico.

```python
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from cars.models import Car
from cars.forms import CarModelForm

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = reverse_lazy('cars_list')
```

- **`model`**: Define qual modelo será atualizado. Neste caso, estamos utilizando o modelo `Car`.

- **`form_class`**: Especifica o formulário que será usado para editar o objeto. Aqui utilizamos o `CarModelForm`, que inclui todos os campos do modelo `Car`.

- **`template_name`**: Especifica o template que será renderizado, neste caso, `'car_update.html'`, onde o formulário de edição será exibido.

- **`success_url`**: Define para onde o usuário será redirecionado após salvar as alterações. Utilizamos `reverse_lazy('cars_list')` para redirecionar o usuário de volta à lista de carros.

### 2. **Configuração da Rota**

Para associar a `CarUpdateView` a uma URL, adicionamos uma nova rota no arquivo `urls.py`.

```python
from django.urls import path
from cars.views import CarUpdateView

urlpatterns = [
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
]
```

- **`path('car/<int:pk>/update/')`**: Configura uma URL dinâmica que aceita um inteiro (`<int:pk>`) como chave primária do carro que será editado.

- **`CarUpdateView.as_view()`**: Chama a `CarUpdateView` para tratar a rota.

- **`name='car_update'`**: Nomeia a rota como `car_update`, facilitando sua referência em templates e redirecionamentos.

### 3. **Adicionando Botão de Edição no Template de Detalhe do Carro**

Agora, no template `car_detail.html`, adicionamos um botão para permitir a edição dos detalhes do carro. Este botão vai redirecionar o usuário para a página de edição.

```html
<div class="buttons-container">
    <a href="{% url 'car_update' pk=object.pk %}" class="btn btn-primary">Editar</a>
</div>
```

- **`{% url 'car_update' pk=object.pk %}`**: Utiliza o nome da rota `car_update` e passa o ID (`pk`) do carro atual para criar a URL de edição correspondente.

### 4. **Criação do Template `car_update.html`**

Este é o template onde o formulário de edição será exibido e o usuário poderá fazer as alterações.

```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <h1>Editar Carro</h1>
    <table>
        {{ form.as_table }}
    </table>
    <div>
        <div class="buttons-container">
            <input type="submit" value="Salvar Alterações" class="btn btn-primary">
            <a href="{% url 'cars_list' %}" class="btn btn-secondary">Cancelar</a>
        </div>
    </div>
</form>
```

- **`{{ form.as_table }}`**: Renderiza o formulário em formato de tabela. Todos os campos definidos no `CarModelForm` são exibidos para edição.
  
- **`{% csrf_token %}`**: Inclui um token CSRF para proteger o formulário contra ataques de Cross-Site Request Forgery.

- **Botões**:
  - O botão "Salvar Alterações" envia o formulário.
  - O botão "Cancelar" redireciona o usuário de volta para a lista de carros (`cars_list`).

### Explicação do Processo

- A **`UpdateView`** é uma view genérica que facilita a edição de um objeto existente.
- O formulário utilizado na view é gerado automaticamente pelo Django com base no modelo especificado.
- O template `car_update.html` renderiza o formulário e permite que o usuário faça alterações e as envie.
- A URL é configurada para capturar o ID do carro (`pk`) que será editado, e a view trata a lógica de busca e atualização do objeto.
- Após salvar, o usuário é redirecionado para a lista de carros.
