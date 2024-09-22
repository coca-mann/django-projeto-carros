# Criando Nossa Rota de Registro de Usuários

Neste exemplo, vamos configurar uma rota de registro de usuários utilizando o Django. Isso inclui a criação de um novo app chamado **`accounts`**, a utilização do **`UserCreationForm`** da biblioteca de autenticação do Django e a criação de um template simples para exibir o formulário de registro.

## Passo a Passo:

1. **Criação do App Accounts**:
   - Para organizar a lógica de autenticação de usuários, criamos um novo app chamado **`accounts`**.
   - Execute o seguinte comando no terminal para criar o app:
     ```bash
     python manage.py startapp accounts
     ```

2. **Configuração do `settings.py`**:
   - Após criar o app, adicione-o à lista de apps instalados no **`settings.py`** do projeto para que ele seja reconhecido pelo Django:
     ```python
     INSTALLED_APPS = [
         # outros apps
         'accounts',
     ]
     ```

3. **Criação da View `register_view` em `accounts/views.py`**:
   - Na view, vamos utilizar o formulário **`UserCreationForm`**, que já vem pronto no Django para facilitar a criação de usuários. Este formulário cuida de todas as validações necessárias.
   - A função da view renderiza o formulário e trata o envio de dados quando o método for POST:
     ```python
     from django.shortcuts import render, redirect
     from django.contrib.auth.forms import UserCreationForm

     def register_view(request):
         if request.method == 'POST':
             user_form = UserCreationForm(request.POST)
             if user_form.is_valid():
                 user_form.save()
                 return redirect('login_view')  # Redireciona para a tela de login após o registro
         else:
             user_form = UserCreationForm()

         return render(request, 'register.html', {'user_form': user_form})
     ```

4. **Configuração da Rota no `app/urls.py`:**
    - Para a rota de registro de usuários, a configuração é feita no arquivo principal de rotas do projeto, geralmente **`app/urls.py`**, incluindo a rota para a view de registro.

    ```python
    from django.urls import path
    from accounts.views import register_view  # Importando a view do app accounts

    urlpatterns = [
        # outras rotas
        path('register/', register_view, name='register_view'),  # Rota para o registro de usuários
    ]
    ```

Essa rota aponta para a função `register_view` no app **`accounts`**, mas a definição da URL ocorre no arquivo principal do projeto, **`app/urls.py`**, garantindo que a página de registro seja acessível pela URL **`/register/`**.


5. **Criação do Template `register.html`**:
   - Agora, crie o template **`register.html`** dentro da pasta **`templates`** do app `accounts`.
   - Esse template renderiza o formulário de registro e inclui o token CSRF para segurança:
     ```html
     {% extends 'base.html' %}

     {% block content %}
         <form method="POST">
             {% csrf_token %}
             {{ user_form.as_p }}
             <input type="submit" value="Cadastrar usuário">
         </form>
     {% endblock %}
     ```

   - O formulário exibe os campos de criação de usuário, como nome de usuário e senha, de forma automática, utilizando o método **`as_p`** que formata os campos como parágrafos.

6. **Testando o Registro**:
   - Acesse a URL **`/accounts/register/`** no navegador, onde você verá o formulário de registro de usuário.
   - Após preencher os campos e enviar o formulário, se o formulário for válido, o usuário será criado e redirecionado para a página de login (ou outra página definida no redirecionamento).

## Explicações Adicionais

- **`UserCreationForm`**: Esse formulário padrão do Django já inclui campos como nome de usuário, senha e confirmação de senha. Ele realiza todas as validações necessárias, como verificação da força da senha e checagem se o nome de usuário já está em uso.
  
- **`csrf_token`**: O token CSRF (Cross-Site Request Forgery) é uma medida de segurança que evita que terceiros submetam dados falsificados para o servidor. No Django, ele é incluído de maneira automática nos formulários para métodos POST.

- **`user_form.as_p`**: O método **`as_p`** converte todos os campos do formulário para parágrafos HTML, facilitando a exibição rápida dos inputs.

Essa configuração básica permite que os usuários se registrem facilmente no seu sistema Django.