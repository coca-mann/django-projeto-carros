# Utilizando DetailView

A **DetailView** é uma **Class-Based View** (CBV) no Django que facilita a exibição de detalhes de um objeto específico em sua aplicação. Essa view é ideal quando você precisa mostrar informações detalhadas de um único registro do banco de dados.

A seguir, vamos configurar uma `DetailView` chamada `CarDetailView`, que exibe as informações detalhadas de um carro específico. 

---

### 1. **Criação da View `CarDetailView`**

A `CarDetailView` é uma classe que herda de `DetailView`, configurada para exibir os detalhes de um carro selecionado.

```python
from django.views.generic.detail import DetailView
from cars.models import Car

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
```

- **`model`**: Define qual modelo a `DetailView` utilizará. Neste caso, estamos usando o modelo `Car`.
  
- **`template_name`**: Especifica o template que será renderizado para exibir os detalhes do carro. Aqui, usamos `'car_detail.html'`.

### 2. **Configuração da Rota**

Para associar essa view a uma URL, adicionamos uma nova rota no arquivo `urls.py`.

```python
from django.urls import path
from cars.views import CarDetailView

urlpatterns = [
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]
```

- **`path('car/<int:pk>/')`**: Configura uma URL dinâmica que aceita um inteiro como parâmetro (`<int:pk>`), que corresponde à chave primária do carro no banco de dados.
  
- **`CarDetailView.as_view()`**: Vincula a `CarDetailView` à URL, permitindo que ela seja chamada como uma função de visualização.

- **`name='car_detail'`**: Dá um nome à rota para facilitar o uso em outras partes do projeto, como em templates.

### 3. **Criação do Template `car_detail.html`**

O template `car_detail.html` é responsável por renderizar os detalhes do carro usando as variáveis fornecidas pela `DetailView`.

```html
<div class="car-card">
      <img src="{{ object.photo.url }}" alt="{{ object.model }} - {{ object.brand }}">
      <h2>{{ object.brand }} {{ object.model }}</h2>
      <p><strong>Tipo:</strong> {{ object.type }}</p>
      <p><strong>Ano de fabricação:</strong> {{ object.factory_year }}</p>
      <p><strong>Ano do modelo:</strong> {{ object.model_year }}</p>
      <p><strong>Placa:</strong> {{ object.plate }}</p>
      <p><strong>Preço:</strong> R$ {{ object.value }}</p>
</div>
```

## Explicação do Template:

- **`{{ object.photo.url }}`**: Exibe a imagem do carro, utilizando a URL armazenada no campo `photo` do modelo `Car`.

- **`{{ object.model }}`** e **`{{ object.brand }}`**: Exibem o modelo e a marca do carro, respectivamente.

- **`{{ object.type }}`**: Mostra o tipo de carro, que é uma chave estrangeira para o modelo `Type`.

- **`{{ object.factory_year }}`** e **`{{ object.model_year }}`**: Exibem os anos de fabricação e do modelo do carro.

- **`{{ object.plate }}`**: Exibe a placa do carro.

- **`{{ object.value }}`**: Mostra o preço do carro.
