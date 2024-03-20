# Geral sobre o fastAPI
- comunicação feita por JSON
- uma vez que uma rota tenha sido criada, por padrão, o fastAPI já cria uma documentação para ela, que pode ser acessada em: `/docs`
- devido a necessidade intrinseca de informar o tipo de dado que está sendo passado, o fastAPI já faz a validação dos dados, e caso o tipo de dado passado não seja o esperado, ele já retorna um erro

# Instalações

### Criando env 

```
conda create -n fast-api python=3.9
```
### Instalação de pacotes

```
pip install fastapi
pip install uvicorn  # ASGI server

```

### Rodando o servidor

- Nome do arquivo: main.py
- Nome da aplicação: app
- Reload: Atualiza o servidor automaticamente

```
uvicorn main:app --reload
```

### Uma vez que o básico de um app esteja de pé, podemos adicionar mais funcionalidades como as rotas

- as rotas são os caminhos que o usuário pode acessar, por exemplo: /users, /items, /users/{user_id}
- quando o usuário acessa um desses caminhos, ele pode fazer uma requisição do tipo GET, POST, PUT, DELETE, etc.
    - *GET*: para pegar informações
    - *POST*: para enviar informações
    - *PUT*: para atualizar informações
    - *DELETE*: para deletar informações
- cada requisição pode ter um retorno diferente, por exemplo: um usuário acessa /users e faz uma requisição do tipo GET, ele pode receber uma lista de usuários, ou um usuário específico, ou um erro, etc.


# Informações avançadas

Tutorial completo de FASTAPI: https://www.youtube.com/watch?v=0sOvCWFmrtA 

**Pontos de estudo**:

- Schema validation with Pydantic (1.07)
- Path order matters (1.48.10) 
  - A ordem das rotas importa, pois o fastAPI vai tentar casar a rota com o primeiro path que ele encontrar
- Changing response status code (1.52.46)
- Automatic documentation (2.18.02)
- What is CORS (11.14.28)
- Testing (14.14.51 - 16.22.09)

### Criando os envs

Tudo vai ficar salvo no `venv` e para ativar o ambiente, basta rodar o comando `source venv/bin/activate`.

Uma vez instalando as ferramentas, elas vão ficar salvas no `venv/lib/python3.*/site-packages`.

```
python -m venv venv
source venv/bin/activate
# install depends

pip install fastapi
pip install uvicorn 

```

### Porque precisamos de Schema validation?

- é complicado pegar os valores do body 
- cliente pode enviar o que eles quiserem 
- precisamos validar os dados que estão sendo enviados
- devemos garantir e forçar que o cliente envie os dados corretos (no esquema de dados que estamos esperando)

Para isso usamos a validaçao de esquema do **Pydantic**

### O que é o CRUD?

- Create - POST
- Read - GET
- Update - PUT/PATCH
- Delete - DELETE

São as operações básicas que podemos fazer em um banco de dados. No fastAPI, podemos fazer essas operações com as rotas

Sempre nomeamos as rotas com o plural do que estamos fazendo, e não com o verbo que estamos usando. 


```
- Exemplo: 
    - POST /users: cria um novo usuário
    - GET /users: pega todos os usuários
    - GET /users/{user_id}: pega um usuário específico
    - PUT /users/{user_id}: atualiza um usuário específico
    - DELETE /users/{user_id}: deleta um usuário específico
```

### A ordem das rotas importa

- A ordem das rotas importa, pois o fastAPI vai tentar casar a rota com o primeiro path que ele encontrar
- Se tivermos uma rota que é `/users/me` e outra que é `/users/{user_id}`, o fastAPI vai tentar casar a rota com a primeira que ele encontrar, ou seja, se o usuário tentar acessar `/users/me`, o fastAPI vai tentar casar com a rota `/users/{user_id}` e não com a rota `/users/me`
- Para resolver isso, podemos usar o `path` para especificar o tipo de dado que estamos esperando, por exemplo: `path: int` ou `path: str`
- Sempre se antentar para garantir que as rotas estão na ordem correta para que o fastAPI consiga casar a rota corretamente 