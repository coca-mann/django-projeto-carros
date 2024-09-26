# Utilizando DeleteView (Generic Views)

O **DeleteView** é uma **Class-Based View (CBV)** genérica do Django que facilita a exclusão de objetos do banco de dados. Ele gera automaticamente uma página de confirmação, onde o usuário pode decidir se deseja prosseguir com a exclusão de um objeto.

A seguir, vamos criar uma funcionalidade para deletar carros cadastrados no sistema.

---

### 1. **Criação da View `CarDeleteView`**

A `CarDeleteView` herda de `DeleteView` e é responsável por exibir uma página de confirmação e excluir o carro caso o usuário confirme.

```python
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from cars.models import Car

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('cars_list')
```

- **`model`**: Define qual modelo será deletado. Neste caso, o `Car`.
- **`template_name`**: O template onde será exibida a confirmação da exclusão, neste caso `'car_delete.html'`.
- **`success_url`**: Define a URL de redirecionamento após a exclusão ser concluída com sucesso. Aqui utilizamos `reverse_lazy('cars_list')` para redirecionar o usuário de volta à lista de carros.

### 2. **Configuração da Rota**

Agora, configuramos a URL que vai acessar a `CarDeleteView`. No arquivo `urls.py`:

```python
from django.urls import path
from cars.views import CarDeleteView

urlpatterns = [
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
]
```

- **`<int:pk>`**: Captura o ID do carro (chave primária) que será deletado.
- **`CarDeleteView.as_view()`**: Chama a `CarDeleteView` para lidar com a requisição.
- **`name='car_delete'`**: Nome da rota para facilitar sua referência em templates e redirecionamentos.

### 3. **Criação do Template `car_delete.html`**

No template `car_delete.html`, será exibida uma mensagem perguntando ao usuário se ele tem certeza de que deseja deletar o carro.

```html
<div class="card">
    <div class="card-header">
        <h1 class="card-title">Deletar Carro</h1>
    </div>
    <div class="card-body">
        <p>Tem certeza que deseja deletar o carro <strong>{{ object.brand }} {{ object.model }}</strong>?</p>
        <form method="post">
            {% csrf_token %}
            <div class="buttons-container">
                <button type="submit" class="btn btn-danger">Deletar Carro</button>
                <a href="{% url 'car_update' pk=object.pk %}" class="btn btn-secondary">Cancelar</a>
            </div>
        </form>
    </div>
</div>
```

- **`{{ object.brand }} {{ object.model }}`**: Exibe a marca e o modelo do carro que será deletado.
- **`{% csrf_token %}`**: Adiciona o token CSRF para proteger o formulário contra ataques de CSRF.
- **Botão "Deletar Carro"**: O botão envia o formulário para confirmar a exclusão.
- **Botão "Cancelar"**: Redireciona o usuário de volta à página de edição, permitindo cancelar a exclusão.

### 4. **Adicionando um Botão de Exclusão**

No template de detalhes do carro (`car_detail.html`), podemos adicionar um botão para que o usuário tenha a opção de deletar o carro diretamente.

```html
<div class="buttons-container">
    <a href="{% url 'car_delete' pk=object.pk %}" class="btn btn-danger">Deletar</a>
</div>
```

- **`{% url 'car_delete' pk=object.pk %}`**: Gera a URL de exclusão do carro, passando o `pk` (chave primária) do carro que será deletado.

---

### Explicação do Processo

1. **Criação da View `CarDeleteView`**: Esta classe trata toda a lógica de exclusão do carro. Quando o usuário acessa a página de deleção, ele verá uma mensagem de confirmação. Ao confirmar, o carro é excluído do banco de dados.

2. **Configuração da Rota**: A URL é configurada para capturar o ID do carro a ser deletado e redirecionar para a `CarDeleteView`.

3. **Criação do Template `car_delete.html`**: A página de confirmação exibe os detalhes do carro e oferece opções para confirmar ou cancelar a exclusão.

4. **Botão de Exclusão**: Adicionamos um botão na página de detalhes do carro que redireciona o usuário para a página de confirmação de deleção.
