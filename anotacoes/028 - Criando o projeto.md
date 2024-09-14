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