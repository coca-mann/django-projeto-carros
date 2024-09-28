# Atualizando nosso inventário com Signals

Ao utilizar **Django Signals**, podemos automatizar o processo de atualização do inventário de carros em nossa aplicação. Neste exemplo, usamos os signals **`post_save`** e **`post_delete`** para manter um registro atualizado da contagem de carros e do valor total dos carros no inventário, tudo isso através de uma função que é chamada sempre que um carro é salvo ou deletado.

### O Problema
Queremos manter um inventário que registre o número total de carros e a soma dos valores de todos os carros armazenados no banco de dados. Ao invés de atualizar manualmente o inventário toda vez que um carro é criado, atualizado ou excluído, podemos automatizar esse processo com Django Signals.

### A Solução
Utilizando os signals **`post_save`** e **`post_delete`**, podemos interceptar os momentos em que um carro é salvo ou deletado e, assim, atualizar automaticamente o inventário de carros.

### Código de Exemplo

1. **Função de Atualização do Inventário**

A função `car_inventory_update` calcula a quantidade total de carros e a soma dos seus valores no banco de dados. Em seguida, ela cria uma nova instância do modelo **`CarInventory`** com esses dados.

```python
from django.db.models import Sum
from cars.models import Car, CarInventory

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )
```

A função `car_inventory_update` desempenha um papel crucial na manutenção e atualização do inventário de carros. Vamos detalhar cada parte da função para entender como ela funciona:

#### 1. **Objetivo da Função**
A função **`car_inventory_update`** é responsável por calcular e atualizar o número total de carros e o valor total desses carros no banco de dados. Ela faz isso toda vez que um carro é salvo (criado ou atualizado) ou deletado, garantindo que o inventário sempre reflita o estado mais recente.

#### 2. **Passo a Passo**

##### a) `cars_count = Car.objects.all().count()`

- **Descrição**: 
    - Este comando obtém todos os objetos do modelo **`Car`** presentes no banco de dados e conta quantos carros existem.
    - O método **`count()`** retorna o número total de registros na tabela `Car`.
  
- **Função**:
    - Ele calcula a quantidade total de carros no banco de dados. Isso é útil para manter um inventário preciso de quantos carros estão registrados.

##### b) `cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']`

- **Descrição**:
    - Aqui, utilizamos o método **`aggregate()`**, que é usado para executar operações de agregação (como somas, médias, máximos, etc.) nos campos de um modelo.
    - A função **`Sum('value')`** soma todos os valores do campo `value` de cada carro no banco de dados. O resultado é um dicionário com a chave `'total_value'`.
    - **`['total_value']`** extrai o valor específico da soma total dos carros.

- **Função**:
    - Esse comando calcula a soma total de todos os valores dos carros registrados no banco de dados, permitindo que o sistema tenha o valor combinado de todos os carros.

##### c) `CarInventory.objects.create(...)`

- **Descrição**:
    - Aqui, criamos um novo registro no modelo **`CarInventory`** com os valores calculados anteriormente.
    - **`cars_count`** e **`cars_value`** são os dados que atualizam a contagem de carros e o valor total no inventário.

- **Função**:
    - Esse comando insere um novo registro no inventário de carros, armazenando o número total de carros e o valor acumulado de todos eles. Esse registro inclui também a data em que essa contagem foi feita, usando o campo **`created_at`** do modelo `CarInventory`.

#### 3. **Por que usar `aggregate()`?**
Usamos o método **`aggregate()`** porque ele permite realizar operações matemáticas diretamente no banco de dados, em vez de calcular essas somas em Python. Isso é mais eficiente, especialmente quando lidamos com grandes volumes de dados.

Ao usar `Sum('value')`, a soma de todos os valores dos carros é calculada no banco de dados, retornando apenas o valor agregado, o que é mais rápido e menos exigente em termos de processamento.

#### 4. **Benefícios da Abordagem**
- **Automação**: Não é necessário atualizar manualmente o inventário sempre que um carro é adicionado, removido ou modificado. A função é chamada automaticamente pelos signals `post_save` e `post_delete`.
- **Precisão**: Como a função consulta diretamente o banco de dados a cada execução, a contagem de carros e o valor total são sempre exatos e atualizados.
- **Eficiência**: Utilizando operações de banco de dados como `count()` e `aggregate()`, a função evita trazer grandes quantidades de dados para a aplicação, melhorando o desempenho.

#### 5. **Exemplo de Execução**
Vamos imaginar que o inventário tem 10 carros, com valores que somam R$200.000. Quando um carro novo é adicionado ou um existente é removido, a função `car_inventory_update` será chamada pelos signals, e o inventário será recalculado e atualizado para refletir corretamente os novos números.

Se for adicionado um carro de valor R$50.000:
- **`cars_count`**: agora será 11.
- **`cars_value`**: agora será R$250.000.

Se um carro de R$30.000 for deletado:
- **`cars_count`**: será atualizado para 10.
- **`cars_value`**: será recalculado para R$220.000.

2. **Signal para Criação e Atualização de Carros (`post_save`)**

Sempre que um carro é salvo no banco de dados, seja criado ou atualizado, o signal **`post_save`** é disparado, acionando a função `car_inventory_update`.

```python
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from cars.models import Car

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()
```

3. **Signal para Exclusão de Carros (`post_delete`)**

Quando um carro é deletado, o signal **`post_delete`** é disparado, também chamando a função `car_inventory_update` para recalcular o inventário.

```python
@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
```

4. **Modelo de Inventário (`CarInventory`)**

O modelo **`CarInventory`** armazena os dados do inventário, incluindo a quantidade total de carros, o valor total, e a data em que a atualização ocorreu.

```python
from django.db import models

class CarInventory(models.Model):
    id = models.AutoField(primary_key=True)
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
```

- **`cars_count`**: Armazena o número total de carros no inventário.
- **`cars_value`**: Armazena a soma dos valores de todos os carros.
- **`created_at`**: Mantém o registro de quando a contagem foi criada ou atualizada.

### Fluxo de Funcionamento
- Quando um carro é **criado, atualizado ou excluído**, o Django dispara os signals `post_save` ou `post_delete`.
- Esses signals chamam a função `car_inventory_update`, que calcula e cria um novo registro no modelo `CarInventory` com a contagem atualizada de carros e o valor total.
