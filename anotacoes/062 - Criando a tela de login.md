# Criando a Tela de Login no Django

A tela de login é essencial para autenticar usuários e garantir o acesso às áreas restritas da aplicação. Vamos criar um template de **login.html**, configurar a rota para a view **`login_view`**, e criar a view responsável por processar o login dos usuários.

## Passos para Implementar a Tela de Login:

1. **Criação da View `login_view`**:
   - A view **`login_view`** é responsável por processar o formulário de login. Ela verifica o método da requisição (GET ou POST) e, em caso de sucesso, autentica o usuário e redireciona-o para uma página específica (neste exemplo, a lista de carros).
   - Se as credenciais não forem válidas, o formulário é redisponibilizado para o usuário tentar novamente.
   
```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        # Obtendo as credenciais do formulário
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticando o usuário
        user = authenticate(request, username=username, password=password)
        
        # Verificando se o usuário existe
        if user is not None:
            login(request, user)  # Loga o usuário
            return redirect('cars_list')  # Redireciona para a página de carros
        else:
            # Caso as credenciais estejam incorretas, exibe o formulário novamente
            login_form = AuthenticationForm()
    else:
        # Se for uma requisição GET, apenas exibe o formulário de login
        login_form = AuthenticationForm()
    
    return render(request, 'login.html', {'login_form': login_form})
```

2. **Configuração da Rota no `urls.py`**:
   - Adicione a rota para a página de login no arquivo de rotas principal **`app/urls.py`**:
   
```python
from django.urls import path
from accounts.views import login_view

urlpatterns = [
    # outras rotas
    path('login/', login_view, name='login_view'),  # Rota para o login de usuários
]
```

3. **Criação do Template `login.html`**:
   - Crie o template **`login.html`** dentro da pasta **`templates`**. Ele renderiza o formulário de login, utilizando o método **`as_table`** para exibir os campos de autenticação como uma tabela.
   - O token CSRF é incluído para garantir a segurança do formulário.
   
```html
{% extends 'base.html' %}

{% block content %}
    <form method="post">
        {% csrf_token %}

        <table>
            {{ login_form.as_table }}  <!-- Exibe os campos de login -->
        </table>

        <input type="submit" value="Entrar">
    </form>
{% endblock %}
```

4. **Explicações Adicionais**:
   - **`authenticate(request, username, password)`**: Esta função tenta autenticar o usuário com base nas credenciais fornecidas (nome de usuário e senha). Se as credenciais forem corretas, retorna o objeto do usuário, caso contrário, retorna **`None`**.
   - **`login(request, user)`**: Caso o usuário seja autenticado com sucesso, a função **`login()`** é usada para iniciar a sessão do usuário.
   - **`AuthenticationForm()`**: Formulário padrão do Django para autenticação. Ele já inclui os campos de **username** e **password**, além de validações internas.
   - **`csrf_token`**: Token que protege contra ataques de **CSRF** (Cross-Site Request Forgery), garantindo que a requisição seja segura.

5. **Testando o Login**:
   - Acesse a URL **`/login/`** no navegador, onde o formulário de login será exibido.
   - Após preencher o nome de usuário e senha, o sistema autentica o usuário e o redireciona para a página de carros, ou exibe o formulário novamente em caso de erro.

Essa configuração básica permite que os usuários façam login no sistema de maneira segura, utilizando o Django como back-end de autenticação.