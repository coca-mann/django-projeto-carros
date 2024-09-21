# Criando Nosso Primeiro Formulário no Django

O Django oferece uma maneira prática e eficiente para criar e gerenciar formulários utilizando o sistema de **Django Forms**. Neste exemplo, vamos criar um formulário para adicionar um novo carro ao nosso sistema, conectando o formulário com o modelo `Car`, criando uma view para processar o formulário e renderizando-o em um template.

## Passo 1: Criar o Arquivo `forms.py`

Dentro do diretório do app `cars`, crie um arquivo chamado `forms.py`. Nesse arquivo, vamos criar uma classe `CarForm`, que será responsável por gerar os campos do formulário com base no modelo `Car`.

**Exemplo de `forms.py`:**
```python
from django import forms
from cars.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'brand', 'factory_year', 'model_year', 'value', 'photo']
```

- **`forms.ModelForm`**: Essa classe gera automaticamente os campos do formulário com base no modelo `Car`.
- **`fields`**: Define quais campos do modelo serão exibidos no formulário, como `model`, `brand`, `factory_year`, etc.

A modificação no arquivo `forms.py` substitui o uso de **`forms.ModelForm`** por **`forms.Form`**, o que significa que o formulário não estará mais vinculado diretamente ao modelo `Car` do Django. Em vez disso, criamos manualmente os campos do formulário. 

Aqui está o código modificado:

```python
from django import forms
from cars.models import Brand

class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()
```

### Detalhes dos Campos

1. **`forms.CharField(max_length=200)`**: 
   - Cria um campo de texto para o modelo do carro com o máximo de 200 caracteres.
   - Similar ao campo `models.CharField` no modelo do Django.

2. **`forms.ModelChoiceField(queryset=Brand.objects.all())`**: 
   - Cria um campo de seleção baseado no modelo `Brand`. O **`queryset`** define os itens que serão listados no campo de seleção, neste caso, todas as marcas de carros (instâncias de `Brand`) disponíveis no banco de dados.
   - Similar ao uso de **ForeignKey** no modelo, mas tratado explicitamente no formulário.

3. **`forms.IntegerField()`**:
   - Cria um campo de entrada de número inteiro para `factory_year` e `model_year`.
   - Esses campos permitem apenas valores inteiros, como seria o caso em um formulário para ano de fabricação e ano do modelo.

4. **`forms.CharField(max_length=10)`**:
   - Um campo de texto limitado a 10 caracteres para a placa do carro.
   - O uso de `max_length=10` limita a quantidade de caracteres que podem ser inseridos.

5. **`forms.FloatField()`**:
   - Cria um campo para números de ponto flutuante, que seria utilizado para o valor do carro.

6. **`forms.ImageField()`**:
   - Cria um campo de upload de arquivo de imagem, necessário para o envio da foto do carro. 
   - O Django vai exigir que o formulário esteja configurado para aceitar o envio de arquivos com `enctype="multipart/form-data"`.

### Diferença entre `forms.ModelForm` e `forms.Form`

- **`forms.ModelForm`**: Está diretamente vinculado a um modelo Django. Ele gera automaticamente os campos do formulário com base no modelo fornecido e facilita o processo de validação e salvamento dos dados no banco de dados.
  
- **`forms.Form`**: Não tem ligação automática com um modelo. Isso significa que você precisa definir manualmente cada campo e lidar com o salvamento dos dados no banco de dados separadamente. No caso de `forms.Form`, após validar o formulário, você precisaria manualmente criar uma instância do modelo e salvar os dados.

### Quando usar `forms.Form`?

- Quando você precisa de mais flexibilidade e não deseja que o formulário seja atrelado a um modelo específico.
- Quando o formulário envolve campos que não estão diretamente relacionados a um modelo do Django, ou quando o formulário manipula dados que precisam de tratamento específico antes de serem salvos no banco de dados. 


## Passo 2: Criar uma View para Processar o Formulário

Agora, vamos adicionar uma nova função no arquivo `views.py` para processar o formulário. Essa função será responsável por exibir o formulário na página e lidar com o envio de dados.

**Exemplo de `views.py`:**
```python
from django.shortcuts import render, redirect
from cars.forms import CarForm

def new_car_view(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Salva o novo carro no banco de dados
            return redirect('cars_view')  # Redireciona para a lista de carros após salvar
    else:
        form = CarForm()

    return render(request, 'new_car.html', {'new_car_form': form})
```

- **`request.method == 'POST'`**: Verifica se a requisição é um envio de formulário. Se for, ele processa os dados.
- **`form.is_valid()`**: Valida os dados do formulário.
- **`form.save()`**: Salva o novo carro no banco de dados.
- **`redirect()`**: Redireciona o usuário para a página de lista de carros após o formulário ser submetido com sucesso.

## Passo 3: Adicionar Rota para a View no `urls.py`

Agora, adicione uma nova rota no arquivo `urls.py` para que a view `new_car_view` seja acessível por uma URL.

**Exemplo de `urls.py`:**
```python
from django.urls import path
from cars.views import cars_view, new_car_view

urlpatterns = [
    path('cars/', cars_view, name='cars_view'),
    path('cars/new/', new_car_view, name='new_car_view'),
]
```

- **`new_car_view`**: A URL `/cars/new/` será usada para acessar o formulário de adição de carros.

## Passo 4: Criar o Template `new_car.html`

Agora, vamos criar o template que exibirá o formulário para adicionar um novo carro. O arquivo `new_car.html` será responsável por renderizar o formulário gerado pela classe `CarForm` e permitir que o usuário insira os dados.

**Exemplo de `new_car.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adicionar Novo Carro</title>
</head>
<body>
    <h1>Adicionar Novo Carro</h1>

    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ new_car_form.as_p }}
        <button type="submit">Salvar</button>
    </form>
</body>
</html>
```

- **`{% csrf_token %}`**: Adiciona um token de segurança ao formulário para evitar ataques CSRF.
- **`{{ new_car_form.as_p }}`**: Renderiza os campos do formulário no formato de parágrafos.
- **`enctype="multipart/form-data"`**: Permite o envio de arquivos, como imagens (campo `photo`).

## Passo 5: Testar o Formulário

Agora, ao acessar a URL `/cars/new/`, o formulário será exibido. O usuário poderá preencher os campos e submeter o formulário, que será processado pela view e salvará os dados no banco de dados.

## Campos de Formulário

Os principais tipos de campos de formulário utilizados aqui são gerados automaticamente pelo Django com base nos tipos de dados definidos no modelo `Car`:

- **`model`**: Campo de texto.
- **`brand`**: Campo de seleção (relacionado ao modelo `Brand`).
- **`factory_year` e `model_year`**: Campos numéricos.
- **`value`**: Campo para entrada de números decimais.
- **`photo`**: Campo para upload de imagens.

Com essa configuração, você terá um formulário funcional para cadastrar novos carros no seu sistema Django.