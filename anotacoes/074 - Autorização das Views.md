# Decorators em Python

Decorators são uma funcionalidade do Python que permite modificar o comportamento de funções ou classes sem alterar diretamente seu código. Eles são amplamente usados para adicionar funcionalidades a funções existentes de uma maneira limpa e reutilizável. Um decorator em Python é uma função que recebe outra função como argumento, adiciona algum comportamento a ela, e a retorna ou substitui por outra função.

### Exemplo Simples de Decorator

Aqui está um exemplo básico de um decorator que imprime uma mensagem antes de chamar a função original:

```python
def meu_decorator(func):
    def wrapper():
        print("Executando algo antes da função.")
        func()
        print("Executando algo depois da função.")
    return wrapper

@meu_decorator
def minha_funcao():
    print("Esta é a função original.")

minha_funcao()
```

Neste exemplo:
- O decorator `meu_decorator` envolve a função `minha_funcao`.
- Quando `minha_funcao` é chamada, o código no decorator é executado antes e depois da função original.
- O decorator usa o símbolo `@` para ser aplicado sobre a função.

Essa técnica é muito útil para reutilizar código, por exemplo, para adicionar verificações, logar informações ou até mesmo fazer validações.

## Utilizando Decorators no Django

No Django, os **decorators** são amplamente utilizados para adicionar funcionalidades específicas, como controle de acesso e autenticação em views. Um dos mais usados é o **`login_required`**, que restringe o acesso a uma view para apenas usuários autenticados.

### Autorização de Views com `login_required`

Em views baseadas em funções (FBVs), é comum usar o decorator **`login_required`** diretamente sobre a função. No entanto, para **Class-Based Views (CBVs)**, a abordagem é um pouco diferente, e precisamos usar o **`method_decorator`** para aplicar o decorator nos métodos da classe.

### Exemplo de `login_required` em CBVs

No código abaixo, utilizamos o decorator `login_required` para garantir que as views de criação, atualização e exclusão de carros só possam ser acessadas por usuários logados. Se um usuário não autenticado tentar acessar essas views, ele será redirecionado para a página de login.

```python
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
```

### Explicação do Código:

- **`@method_decorator(login_required, name='dispatch')`**: 
  - Aplica o decorator **`login_required`** no método `dispatch` da **Class-Based View**. O `dispatch` é o método que lida com as requisições HTTP (GET, POST, etc.) e direciona para o método adequado (como `get()` ou `post()`).
  - **`login_url='login'`**: Se o usuário não estiver autenticado, ele será redirecionado para a página de login, que é identificada pela URL com o nome `login`.
  
- **`NewCarCreateView`, `CarUpdateView`, e `CarDeleteView`**: Essas são views responsáveis por criar, atualizar e deletar carros, respectivamente. Todas elas estão protegidas com o decorator `login_required`, garantindo que apenas usuários logados possam acessar essas páginas e fazer modificações.

### Como Funciona:
1. Quando um usuário tenta acessar uma dessas views, o **`method_decorator`** verifica se o usuário está autenticado.
2. Se o usuário **não estiver logado**, ele será redirecionado para a URL de login (`login_url`).
3. Se o usuário **estiver logado**, ele poderá acessar a view normalmente e interagir com os dados.

## Por Que Usar Decorators?

- **Reutilização**: Aplicar a mesma lógica de autenticação em várias views sem repetir o código.
- **Legibilidade**: A utilização de decorators mantém o código mais limpo e fácil de entender.
- **Segurança**: Com o `login_required`, é possível proteger partes sensíveis da aplicação, como criação, edição ou exclusão de registros, garantindo que apenas usuários autenticados tenham acesso.