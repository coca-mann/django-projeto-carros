# Criando Validações Personalizadas no Django Forms

No Django, podemos adicionar validações personalizadas ao formulário utilizando métodos de "cleaning". Esses métodos permitem verificar os dados enviados pelo usuário antes que eles sejam salvos no banco de dados, garantindo que atendam a requisitos específicos. Abaixo, vamos entender como fazer isso através de um formulário utilizando o **`ModelForm`**.

### Exemplo de Validações Personalizadas no `forms.py`

Aqui está o código do `CarModelForm` que valida o campo `value` (valor do carro) e o campo `factory_year` (ano de fabricação):

```python
from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'O valor mínimo do carro deve ser de R$ 20.000.')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1975.')
        return factory_year
```

## Explicação do Código

1. **`clean_value(self)`**:
   - Este método é responsável por validar o campo `value`, que representa o valor do carro.
   - Utilizamos o método **`self.cleaned_data.get('value')`** para obter o valor do campo já limpo, ou seja, após passar pelas validações automáticas do Django (como tipo de dado correto, presença de valor, etc.).
   - A condição `if value < 20000` verifica se o valor inserido é menor do que R$ 20.000. Caso seja, o método **`self.add_error('value', 'O valor mínimo do carro deve ser de R$ 20.000.')`** adiciona um erro específico ao campo `value`.
   - Finalmente, retornamos o valor validado para que, se for válido, ele siga para o próximo estágio.

2. **`clean_factory_year(self)`**:
   - Similar ao método anterior, este método valida o campo `factory_year` (ano de fabricação).
   - A linha `factory_year = self.cleaned_data.get('factory_year')` obtém o valor do campo.
   - A condição `if factory_year < 1975` garante que o carro não seja mais antigo que 1975. Caso contrário, é gerado o erro com a mensagem **`self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1975.')`**.
   - O valor validado é então retornado para continuidade no processo.

## Funcionamento do `clean_<fieldname>()`

- No Django, para cada campo que requer uma validação personalizada, você pode criar um método com o formato **`clean_<nome_do_campo>()`**.
- Esse método é chamado automaticamente durante o processo de validação.
- **`self.cleaned_data`**: Armazena os dados já limpos e validados que podem ser acessados e modificados.

## Utilizando o Formulário na View

Agora, você pode utilizar o formulário com validações personalizadas na sua view como faria com qualquer outro `ModelForm`:

```python
from django.shortcuts import render, redirect
from cars.forms import CarModelForm

def new_car_view(request):
    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars_view')
    else:
        form = CarModelForm()

    return render(request, 'new_car.html', {'new_car_form': form})
```

Se o usuário tentar cadastrar um carro com valor inferior a R$ 20.000 ou com ano de fabricação anterior a 1975, o Django exibirá automaticamente as mensagens de erro definidas nos métodos de validação.

## Benefícios das Validações Personalizadas

- **Controle adicional**: Permite aplicar regras de negócio que vão além das validações automáticas (como tipos de dados ou campos obrigatórios).
- **Mensagens de erro específicas**: Oferece feedback mais detalhado e específico ao usuário quando os dados não atendem aos critérios estabelecidos.
- **Validação diretamente no formulário**: A lógica de validação fica próxima à lógica de exibição e submissão do formulário, tornando o código mais legível e fácil de manter.

Com essas validações personalizadas, o Django garante que apenas dados válidos sejam salvos no banco de dados, protegendo a integridade das informações e facilitando a implementação de regras específicas para o domínio do projeto.