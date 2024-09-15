# Entendendo os arquivos das Apps
Quando você cria uma nova **App** no Django com o comando `python manage.py startapp nome_da_app`, o Django gera uma estrutura básica de diretórios e arquivos. Esses arquivos servem para configurar e organizar diferentes aspectos da App. Aqui está uma descrição mais detalhada de cada arquivo e diretório criado:

## Estrutura de Arquivos e Diretórios Criados

1. **`nome_da_app/`** (diretório principal da App):
   - **`__init__.py`**:
     - **Descrição**: Um arquivo vazio que transforma o diretório `nome_da_app` em um pacote Python. Este arquivo é essencial para que Python reconheça o diretório como um pacote e permita a importação dos módulos nele contidos.
   - **`admin.py`**:
     - **Descrição**: Arquivo onde você registra os modelos da App para que eles possam ser gerenciados através da interface administrativa do Django. Você usa o `admin.site.register(Model)` para adicionar modelos à administração.
     - **Exemplo**:
       ```python
       from django.contrib import admin
       from .models import Carro

       admin.site.register(Carro)
       ```
   - **`apps.py`**:
     - **Descrição**: Contém a configuração da App. A classe `AppConfig` herda de `django.apps.AppConfig` e pode ser usada para configurar várias opções da App, como seu nome e configuração específica.
     - **Exemplo**:
       ```python
       from django.apps import AppConfig

       class CarsConfig(AppConfig):
           name = 'cars'
       ```
   - **`models.py`**:
     - **Descrição**: Onde você define os modelos de dados da App. Modelos são classes que representam tabelas no banco de dados, e cada atributo da classe é um campo da tabela. O Django utiliza essas classes para criar e modificar a estrutura do banco de dados.
     - **Exemplo**:
       ```python
       from django.db import models

       class Carro(models.Model):
           marca = models.CharField(max_length=100)
           modelo = models.CharField(max_length=100)
           ano = models.IntegerField()
       ```
   - **`tests.py`**:
     - **Descrição**: Arquivo destinado a escrever testes automatizados para a App. Os testes ajudam a garantir que o código da App funcione corretamente e que as alterações futuras não quebrem funcionalidades existentes.
     - **Exemplo**:
       ```python
       from django.test import TestCase
       from .models import Carro

       class CarroModelTest(TestCase):
           def test_carro_str(self):
               carro = Carro(marca="Toyota", modelo="Corolla", ano=2021)
               self.assertEqual(str(carro), "Toyota Corolla")
       ```
   - **`views.py`**:
     - **Descrição**: Onde você define as funções ou classes que processam as requisições e retornam respostas. As views manipulam a lógica do negócio e interagem com os modelos para fornecer os dados necessários para as páginas HTML.
     - **Exemplo**:
       ```python
       from django.shortcuts import render
       from .models import Carro

       def lista_carros(request):
           carros = Carro.objects.all()
           return render(request, 'cars/lista_carros.html', {'carros': carros})
       ```
   - **`migrations/`** (diretório):
     - **Descrição**: Armazena os arquivos de migração que são gerados quando você faz alterações nos modelos e executa o comando `makemigrations`. As migrações descrevem as mudanças no esquema do banco de dados e são usadas para aplicá-las com o comando `migrate`.
     - **`__init__.py`**:
       - **Descrição**: Um arquivo vazio que permite que o diretório `migrations` seja tratado como um pacote Python. O Django utiliza este diretório para manter o controle das migrações aplicadas.
