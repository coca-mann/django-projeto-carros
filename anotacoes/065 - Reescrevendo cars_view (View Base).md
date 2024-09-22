# Reescrevendo a `cars_view`: De Function-Based View (FBV) para Class-Based View (CBV)

No Django, uma **Function-Based View (FBV)** é uma função Python regular que recebe uma requisição, processa a lógica de negócio e retorna uma resposta. No entanto, as **Class-Based Views (CBVs)** permitem estruturar o código de maneira mais organizada e reutilizável, separando as lógicas de requisição, o que facilita a manutenção e a expansão do código.

Abaixo, explico como reescrever a função `cars_view` como uma **Class-Based View** (CBV) utilizando o código fornecido.

---

### Function-Based View (FBV)

```python
def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:
        cars = cars.filter(model__icontains=search)

    return render(
        request,
        'cars.html',
        {'cars': cars }
    )
```

Na **FBV**, o fluxo ocorre da seguinte maneira:

1. **Recebendo a requisição**: A view recebe a requisição HTTP via o objeto `request`.
2. **Buscando os dados do banco**: Os carros são obtidos do banco de dados usando o Django ORM, com `Car.objects.all()`, e ordenados pelo campo `model`.
3. **Filtrando os resultados**: A view verifica se há um parâmetro `search` na requisição GET. Se o parâmetro estiver presente, os resultados são filtrados com base no campo `model`, utilizando o operador `icontains` para realizar uma busca que não diferencia maiúsculas de minúsculas.
4. **Renderizando o template**: Por fim, os dados (os carros) são passados para o template `'cars.html'`, que é renderizado com o contexto contendo os carros filtrados.

---

### Reescrevendo como Class-Based View (CBV)

A mesma funcionalidade pode ser implementada de maneira mais modular e orientada a objetos com uma **CBV**.

```python
from django.views import View
from django.shortcuts import render
from cars.models import Car

class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)

        return render(
            request,
            'cars.html',
            {'cars': cars }
        )
```

---

## Etapas no Código da Class-Based View (CBV)

1. **Herança da Classe `View`**:
   A nova view herda da classe base `View` do Django (`django.views.View`), o que permite estruturar o código de maneira mais modular. A classe `View` contém métodos específicos para lidar com diferentes tipos de requisições HTTP (GET, POST, etc.).

2. **Definindo o Método `get()`**:
   Em vez de receber todos os tipos de requisições em uma função única, a CBV define métodos para cada tipo de requisição. Neste caso, estamos tratando uma requisição GET, então o método `get()` é definido. Ele recebe o objeto `request` e processa a requisição GET.

3. **Consultando os Carros no Banco de Dados**:
   A lógica de consultar todos os objetos `Car` e ordená-los por `model` é idêntica à FBV, mas agora está encapsulada no método `get()`. Isso mantém o código mais organizado e fácil de estender.

4. **Processando o Parâmetro de Busca**:
   Da mesma forma que na FBV, verificamos se o parâmetro `search` foi passado na URL através de `request.GET.get('search')`. Se houver um valor, filtramos os carros com base no campo `model`, utilizando `icontains` para tornar a busca case-insensitive.

5. **Renderizando o Template**:
   O método `render()` é utilizado para retornar o template `'cars.html'`, passando o contexto com os carros filtrados.

---

## Comparação: FBV vs CBV

- **Modularidade**: A CBV separa as lógicas de requisição, permitindo maior reutilização de código. Se precisarmos adicionar um comportamento para outro tipo de requisição (como POST), podemos adicionar facilmente um método `post()`.
  
- **Manutenção**: Em projetos maiores, as CBVs facilitam a organização e manutenção do código, pois permitem reutilizar classes herdadas e comportamentos prontos, como `ListView`, `DetailView`, etc.

- **Expansibilidade**: As CBVs são mais fáceis de expandir e ajustar, pois são orientadas a objetos e podem ser combinadas e estendidas com outras views.
