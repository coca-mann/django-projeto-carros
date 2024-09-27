# O que são Signals no Django?

**Signals** no Django são uma forma de permitir que certos eventos sejam "escutados" e reagidos, sem a necessidade de modificar diretamente o código que dispara o evento. Eles servem para conectar pedaços de código em momentos específicos do ciclo de vida de uma aplicação, facilitando a execução de tarefas automáticas quando certos eventos acontecem, como a criação, atualização ou exclusão de um objeto.

Signals são particularmente úteis para **desacoplar** funcionalidades e manter o código mais organizado, já que permitem adicionar lógica reativa em resposta a eventos sem modificar diretamente as funções ou classes que originam esses eventos.

## Funcionamento dos Signals

O Django oferece alguns signals integrados que são disparados automaticamente em momentos-chave, como:
- **`pre_save`**: Disparado antes de um objeto ser salvo no banco de dados.
- **`post_save`**: Disparado após um objeto ser salvo no banco de dados.
- **`pre_delete`**: Disparado antes de um objeto ser deletado.
- **`post_delete`**: Disparado após um objeto ser deletado.

## Exemplo de Uso de Signals

### Criando um Signal que é disparado após um registro ser salvo (post_save):

Neste exemplo, quando um novo carro é criado ou atualizado no banco de dados, o signal **`post_save`** será disparado, e uma mensagem de log será gerada.

1. Crie um arquivo `signals.py` no seu app (por exemplo, `cars/signals.py`).

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from cars.models import Car

@receiver(post_save, sender=Car)
def car_saved_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Um novo carro foi criado: {instance.model} ({instance.brand})")
    else:
        print(f"O carro {instance.model} foi atualizado.")
```

2. No arquivo `apps.py` do seu app, conecte os signals:

```python
from django.apps import AppConfig

class CarsConfig(AppConfig):
    name = 'cars'

    def ready(self):
        import cars.signals  # Importa o módulo de signals quando a aplicação está pronta
```

3. Certifique-se de que o app esteja registrado no `INSTALLED_APPS` no `settings.py`:

```python
INSTALLED_APPS = [
    # outros apps
    'cars.apps.CarsConfig',
]
```

### Explicação do Exemplo:
- **`@receiver(post_save, sender=Car)`**: Este decorator conecta a função `car_saved_signal` ao signal `post_save` para o modelo `Car`. Isso significa que sempre que um carro for salvo no banco de dados, essa função será executada.
- **`instance`**: É o objeto do modelo `Car` que acabou de ser salvo.
- **`created`**: Indica se o objeto foi criado (True) ou atualizado (False).
- A função imprime mensagens diferentes dependendo se o carro foi criado ou atualizado.

## Exemplo de Signal pré-salvamento (pre_save):

Você pode usar o signal **`pre_save`** para executar alguma ação antes que o objeto seja salvo. No exemplo a seguir, garantimos que o nome do modelo do carro esteja sempre em maiúsculas antes de salvar.

```python
from django.db.models.signals import pre_save
from django.dispatch import receiver
from cars.models import Car

@receiver(pre_save, sender=Car)
def capitalize_car_model(sender, instance, **kwargs):
    instance.model = instance.model.upper()  # Coloca o nome do modelo em maiúsculas
```

### Explicação:
- **`pre_save`**: Ocorre antes de o objeto ser salvo no banco de dados.
- O modelo do carro é convertido para letras maiúsculas antes de ser salvo.
