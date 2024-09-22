# Utilizando ListView (Generic Views)

No Django, as **Generic Views** oferecem uma maneira eficiente e simplificada de lidar com as operações comuns que envolvem a exibição de listas de objetos e detalhes de instâncias específicas. Uma das mais usadas é a **ListView**, que abstrai a lógica comum de exibir listas de objetos, como por exemplo, exibir todos os carros em uma página.

Abaixo explicamos como utilizar a **ListView** e personalizá-la para realizar buscas com um parâmetro de pesquisa, como o exemplo da classe `CarsListView`.

---

## Exemplo da `CarsListView` utilizando `ListView`

```python
from django.views.generic import ListView
from cars.models import Car

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars
```

---

### Explicação das Etapas:

### 1. **Herança da Classe `ListView`**:
   A `CarsListView` herda da classe genérica `ListView`, que já vem com a lógica implementada para exibir listas de objetos de um modelo. Isso economiza tempo ao não precisar reescrever funções como o manuseio de requisições GET ou a iteração sobre os objetos.

### 2. **Definição dos Atributos**:

- **`model`**: Aqui, especificamos que o modelo que será listado é o `Car`. A `ListView` automaticamente busca todos os objetos desse modelo no banco de dados.
  
- **`template_name`**: Este atributo indica qual template será renderizado. No caso, o template `'cars.html'` será utilizado para exibir os carros.

- **`context_object_name`**: Com este atributo, estamos especificando o nome que será utilizado no contexto para referenciar os objetos no template. No caso, será `'cars'`. Assim, no template, poderemos usar `{{ cars }}` para acessar a lista de carros.

### 3. **Método `get_queryset()`**:
   
O método `get_queryset()` é sobrescrito para personalizar a query de objetos retornados pelo banco de dados.

- **Chamada do método `super()`**: Utilizamos `super().get_queryset()` para obter a query padrão de todos os objetos `Car` no banco de dados, e logo em seguida aplicamos uma ordenação por `model`.

- **Captura do parâmetro de busca (`search`)**: Utilizamos `self.request.GET.get('search')` para verificar se um parâmetro de busca foi passado pela URL (via `GET`). Caso o parâmetro esteja presente, o método filtra os resultados utilizando o operador `icontains`, que realiza uma busca que não diferencia maiúsculas de minúsculas no campo `model` dos carros.

### 4. **Retorno dos resultados filtrados**:
   Após aplicar a filtragem, o método retorna o queryset de carros, que será renderizado no template.

---

## Diferenças entre `View` e `ListView`:

- **`ListView`** simplifica o processo de exibir listas de objetos, pois já contém toda a lógica para lidar com requisições GET, listar objetos e renderizar templates, enquanto a `View` exige a implementação manual dessas funcionalidades.

- **`get_queryset()`**: O método `get_queryset()` permite personalizar a consulta ao banco de dados de maneira simples, sem precisar reescrever toda a lógica da view.

---

## Template (`cars.html`)

No template `cars.html`, é possível acessar a variável de contexto `cars`, que contém a lista de carros retornada pelo `get_queryset()`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meus carros</title>
</head>
<body>
    <h1>Lista de Carros</h1>
    <form method="GET">
        <input type="text" name="search" placeholder="Buscar modelo...">
        <button type="submit">Buscar</button>
    </form>
    <ul>
        {% for car in cars %}
            <li>{{ car.model }} - {{ car.brand.name }}</li>
        {% empty %}
            <li>Nenhum carro encontrado.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

Neste template:
- **Formulário de busca**: O formulário permite que o usuário insira um termo de busca, que será enviado como parâmetro GET na URL.
- **Lista de carros**: A lista de carros é exibida utilizando o `for` do Django Template Language para iterar sobre os objetos `cars` retornados pelo `get_queryset()`.
