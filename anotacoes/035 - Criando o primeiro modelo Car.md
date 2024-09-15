Para criar um modelo `Car` no Django com os campos `id`, `model`, `brand`, `factory_year`, `model_year` e `value`, siga os passos abaixo. Este modelo representa um carro e armazena informações essenciais sobre ele.

## Passos para Criar o Modelo `Car`

1. **Defina o Modelo no Arquivo `models.py`**:
   No arquivo `models.py` da sua App, você cria uma classe `Car` que herda de `models.Model`. Cada atributo da classe representa um campo no banco de dados.

   ```python
   from django.db import models

   class Car(models.Model):
       # O Django já cria um campo id automaticamente como chave primária
       model = models.CharField(max_length=100)
       brand = models.CharField(max_length=100)
       factory_year = models.IntegerField()
       model_year = models.IntegerField()
       value = models.DecimalField(max_digits=10, decimal_places=2)

       def __str__(self):
           return f"{self.brand} {self.model} ({self.model_year})"
   ```

   - **`model`**: Armazena o modelo do carro (ex. "Corolla"). Tipo `CharField` com limite de 100 caracteres.
   - **`brand`**: Armazena a marca do carro (ex. "Toyota"). Tipo `CharField` com limite de 100 caracteres.
   - **`factory_year`**: Armazena o ano de fabricação do carro. Tipo `IntegerField`.
   - **`model_year`**: Armazena o ano do modelo do carro. Tipo `IntegerField`.
   - **`value`**: Armazena o valor do carro. Tipo `DecimalField` para valores com precisão, com até 10 dígitos no total e 2 casas decimais.

2. **Crie as Migrações**:
   Gere um arquivo de migração para incluir o novo modelo no banco de dados.

   ```bash
   python manage.py makemigrations
   ```

3. **Aplique as Migrações**:
   Execute o comando `migrate` para aplicar as migrações e criar a tabela `car` no banco de dados.

   ```bash
   python manage.py migrate
   ```

