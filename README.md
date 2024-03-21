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
# or you can specify the path to the main file
uvicorn app.main:app --reload
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

### O que são os CORS?

- Cross-Origin Resource Sharing (CORS) é um mecanismo que usa cabeçalhos HTTP adicionais para informar a um navegador que permita que um aplicativo Web seja executado em um domínio (origem) com permissão para acessar recursos selecionados de um servidor em um domínio distinto  
- O CORS é um mecanismo de segurança que permite que os recursos de uma página da web sejam solicitados a partir de outro domínio fora do domínio de origem
- O CORS é uma especificação do W3C e faz parte das especificações do HTML5

```
# Devemos deixar as origens em um .env de preferência
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:8080",
    "https://myapp.herokuapp.com",
]

```


```
from fastapi.middleware.cors import CORSMiddleware

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # allow all methods
    allow_headers=["*"],  # allow all headers
)
```

### Sobre env e dependências

Uma vez que todas as dependências estejam instaladas, podemos criar um arquivo `requirements.txt` para salvar todas as dependências do projeto. 

``` 
pip freeze > requirements.txt
```

E para instalar todas as dependências de um projeto, basta rodar o comando:

```
pip install -r requirements.txt
```

### Teste o coração do seu app e sua segurança

- Testes são muito importantes para garantir que o seu app está funcionando corretamente
- O fastAPI já vem com um sistema de testes embutido, que pode ser acessado em: `/docs` e clicando em `Try it out`
- Podemos usar o `pytest` para fazer testes mais complexos
- Podemos criar os testes no root do projeto, dentro de um folder chamado `tests` e em um arquivo chamado `test_main.py` e rodar o comando `pytest` para rodar os testes
- Existem algumas convenções para criar os testes, por exemplo: `test_` no começo do nome do teste, `assert` para verificar se o teste passou ou não, etc. O mesmo para o nome das funções, por exemplo: `def test_read_main()`, `def test_read_main_invalid_token()`, etc.
- testes por padrão não printam nada, a não ser que o teste falhe

Para roda os testes, basta rodar o comando `pytest -v` no terminal.

Para realizar mais de um teste, para cada função podemos usar @pytest.mark.parametrize para passar os valores que queremos testar. 

``` 
import pytest

@pytest.mark.parametrize("test_input, expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

```
Quando vamos iniciar algumas variáveis que vão ser usadas em vários testes, podemos usar o `setup` e `teardown` para inicializar e finalizar as variáveis. Também podemos utilizar o fixture para isso, que é uma função que vai ser executada antes e depois dos testes, e que pode ser usada em vários testes diferentes.  

```
import pytest

@pytest.fixture
def setup():
    print("Setup")
    yield
    print("Teardown")

```

Em caso de warnings de Deprecation, podemos adicionar o seguinte código ao `pytest.ini`:

```
[pytest]
filterwarnings =
    ignore::DeprecationWarning
```
Para ativar o teste

```
pytest -v -s -x
```