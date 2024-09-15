# Armazenando Imagens dos Carros no Django (Com Migrações)

Para adicionar a funcionalidade de armazenar imagens dos carros no seu projeto Django, além dos ajustes no modelo, configurações e URLs, é necessário realizar migrações para que o banco de dados reconheça o novo campo de imagem. Abaixo está uma visão geral das etapas com os comandos de migração incluídos.

## 1. **Adicionando o Campo de Imagem ao Modelo `Car`**

No arquivo `models.py` da aplicação `cars`, foi adicionado o campo `photo` ao modelo `Car`:

```python
from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.model_year})"
```

- **`photo = models.ImageField(upload_to='cars/', blank=True, null=True)`**: 
  - Este campo permite o upload de imagens de carros, armazenando-as na pasta `media/cars/`.
  - `blank=True` e `null=True` indicam que o campo não é obrigatório.

## 2. **Instalando a Biblioteca Pillow**

A biblioteca **Pillow** é necessária para o Django manipular imagens. Instale-a com o seguinte comando:

```bash
pip install Pillow
```

## 3. **Configurando Diretórios de Mídia**

No arquivo `settings.py` do projeto, adicione as configurações para o armazenamento de arquivos de mídia:

```python
import os

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

- **`MEDIA_ROOT`**: Diretório onde os arquivos de mídia serão armazenados.
- **`MEDIA_URL`**: Prefixo da URL para acessar os arquivos de mídia.

## 4. **Configurando as URLs para Arquivos de Mídia**

No arquivo `urls.py` do seu projeto, adicione as seguintes linhas para garantir que os arquivos de mídia sejam servidos corretamente no modo de desenvolvimento:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Outras rotas...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 5. **Executando as Migrações**

Depois de ajustar o modelo e as configurações, você precisa criar e aplicar as migrações para que o novo campo de imagem seja refletido no banco de dados.

1. **Criação das migrações**:

   Use o comando `makemigrations` para gerar os arquivos de migração baseados nas alterações feitas no modelo:

   ```bash
   python manage.py makemigrations
   ```

2. **Aplicação das migrações**:

   Depois de criar as migrações, aplique-as ao banco de dados com o comando `migrate`:

   ```bash
   python manage.py migrate
   ```

   Isso garantirá que o campo `photo` seja adicionado à tabela `Car` no banco de dados.
