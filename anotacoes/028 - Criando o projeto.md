# Os primeiros passos.
Primeiramente é necessário criar uma pasta no computador que será utilizada para o projeto. Recomenda-se que seja em algum lugar na pasta do usuário.

Após a criação, abra a pasta no VSCode.

Dentro do VSCode abra o terminal e realize alguns comandos para iniciar um projeto Python.

```pwsh
python -m venv venv
```
O comando acima irá criar um ambiente virtual em Python para o projeto. A execução não deve demorar mais que 1 minuto.

Em seguida é necessário ativar o ambiente virtual.

Esse passo é importante para que as bibliotecas, pacotes e todos os arquivos do projeto fiquem dentro do seu ambiente virtual, e não espalhados no computador.

```pwsh
.\venv\Scripts\activate
```
O comando acima irá executar um script que ativa, no terminal em execução, o ambiente virtual do projeto.

Dessa forma qualquer pacote ou biblioteca instalado, será instalado no ambiente virtual do projeto.

## Git
Aproveite e executa a inicialização do repositório Git para o versionamento do projeto.

```pwsh
git init
```

Adicione todos os arquivos do projeto em um commit do Git
```
git add .
```

Realize o primeiro commit para iniciar o versionamento
```pwsh
git commit -m "First commit"
```

## Django
O projeto em questão utilizará o framework Django.

Para instalar o Django execute o seguinte comando, dentro do ambiente virtual do projeto:

```pwsh
pip install django
```

Aguarde a instalação das bibliotecas e pacotes do Django no projeto.

Em seguida verifique a versão do Django:

```pwsh
django-admin --version
```
A execução do comando deve exibir na tela a versão do framework Django instalado.

Agora é a hora de iniciar o projeto Django

```pwsh
django-admin startproject app .
```
O código acima utiliza uma função do Django para iniciar o projeto e coloca-lo em uma pasta chamada `app`. O ponto no final do código serve para indicar que a pasta `app` será criada na raiz do projeto.

Para garantir que o projeto Django foi criado com sucesso e esta em boas condições, inicie um servidor de testes:

```pwsh
python .\manage.py runserver
```
O código acima irá executar um servidor de testes baseado no arquivo `manage.py` localizado na pasta raiz do projeto, onde contém as configurações do projeto Django.