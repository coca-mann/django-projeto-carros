# Comando makemigrations
O comando `makemigrations` no Django é utilizado para criar "migrações" com base nas alterações feitas nos modelos (models) do projeto. Migrações são como um histórico das mudanças na estrutura do banco de dados ao longo do tempo. Sempre que você faz alterações nos seus modelos, como adicionar um campo, remover uma tabela ou modificar atributos, o comando `makemigrations` gera um arquivo de migração que descreve essas mudanças de forma que o Django possa aplicá-las ao banco de dados.

## Funcionalidade do `makemigrations`:
- **Criação de migrações**: Examina os modelos e detecta mudanças, gerando os arquivos de migração necessários.
- **Rastreia alterações**: As migrações são registradas em arquivos que descrevem como o banco de dados deve ser atualizado.
- **Não aplica as alterações**: O `makemigrations` apenas cria os arquivos de migração. Para aplicar as mudanças no banco de dados, você precisa rodar o comando `migrate`.

## Exemplo de Uso:
1. Após alterar ou criar um novo modelo:
   ```bash
   python manage.py makemigrations
   ```

2. O Django gerará um arquivo de migração na pasta `migrations/` dentro da App correspondente, descrevendo as mudanças a serem aplicadas ao banco de dados.

## Fluxo com `migrate`:
Após rodar o `makemigrations`, você deve usar o comando `migrate` para aplicar essas migrações ao banco de dados:
```bash
python manage.py migrate
```

Assim, `makemigrations` é essencial para manter a estrutura do banco de dados em sincronia com os modelos Python do projeto.