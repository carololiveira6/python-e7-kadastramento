## **Table of Contents**
- [E7 - Kadastramento](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1esj4slvm0) 
  - [Objetivo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1f3b8ajms0)
  - [Preparativos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1f3b8ajms1)
- [Entradas e saídas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1esq74qsl4) 
  - [Input 1 - Requisição POST para /signup.](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1f3lbhppp0)
  - [Output 1 - Resposta do servidor](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1f3lbhppp1)
  - [Input 2 - Requisição POST para /login](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1f3lbhppp2)
  - [Output 2 - Resposta do servidor](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1evmvfg2u6)
  - [Input 3 - Requisição PATCH para /profile/](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1f3lbhppp4)
  - [Output 3 - Resposta do servidor](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1evmvfg2u7)
  - [Input 4 - Requisição DELETE para /profile/](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1f3lbhppp5) 
  - [Output 4 - Resposta do servidor](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1evmvfg2u9)
  - [Input 5 - Requisição GET para /users](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1f3lbhppp6) 
  - [Output 5 - Resposta do servidor](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1evmvfg2u9)
- [Entregáveis](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1egvoav555j) 
  - [Repositório](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_01_kadastramento.html&ref=master#mcetoc_1eh146n6m3) 
# **E7 - Kadastramento**
Para essa entrega, você criará um sistema que permitirá o cadastramento e a manutenção de um usuário em uma plataforma.
## **Objetivo**
Essa atividade foi elaborada para trabalhar seus conhecimentos de manipulação de arquivos CSV em uma aplicação em Flask.
## **Preparativos**
Você deverá criar um arquivo chamado users.csv, que utilizará para guardar os registros de usuários. Você precisará retornar status em suas requisições, então como sugestão, utilize o [HTTP modules](https://docs.python.org/3/library/http.html#http.HTTPStatus) do Python para retornar os status corretamente! Centralize sua lógica de rotas em um arquivo chamado app.py



**Ex 1: A rota de registro deve seguir o seguinte formato:**

- URI: /signup
- Assinatura da função: signup()

**Ex 2: A rota de login deve seguir o seguinte formato:**

- URI: /login
- Assinatura da função: login()



**Ex 3: A rota de update deve seguir o seguinte formato:**

- URI: /profile/<int:user\_id>
- Assinatura da função: update\_user(user\_id)



**Ex 4: A rota de delete deve seguir o seguinte formato:**

- URI: /profile/<int:user\_id>
- Assinatura da função: delete\_user(user\_id)



**Ex 5: A rota de get dos usuários deve seguir o seguinte formato:**

- URI: /users
- Assinatura da função: all\_users()
# -----
# **Entradas e saídas**
**Exercício 1**
## **Input 1 - Requisição POST para /signup.**
**IMPORTANTE**: **Você deve verificar se já existe um usuário com o mesmo email dentro da sua base de dados**, caso exista, deve retornar status 422 - Unprocessable Entity e um **JSON vazio**.

\# Body da requisição

{   

`    `"name": "Naruto Uzumaki",

`    `"email": "naruto@konoha.com",

`    `"password": "imgoingtobeahokage123",

`    `"age": 19

}
## **Output 1 - Resposta do servidor**
{

`    `"id": "1",

`    `"name": "Naruto Uzumaki",

`    `"email": "naruto@konoha.com",

`    `"age": 19

}



**Exercício 2**
## **Input 2 - Requisição POST para /login**
\# Body da requisição

{   

`    `"email": "naruto@konoha.com",

`    `"password": "imgoingtobeahokage123"

}
## **Output 2 - Resposta do servidor**
{

`    `"id": "1",

`    `"name": "Naruto Uzumaki",

`    `"email": "naruto@konoha.com",

`    `"age": 19

}



**Exercício 3**
## **Input 3 - Requisição PATCH para /profile/<int:user\_id>**
\# Body da requisição

{   

`    `"age": 21

}
## **Output 3 - Resposta do servidor**
{

`    `"id": "1",

`    `"name": "Naruto Uzumaki",

`    `"email": "naruto@konoha.com",

`    `"age": 21

}



**Exercício 4**
## **Input 4 - Requisição DELETE para /profile/<int:user\_id>**
\# Body da requisição

NO CONTENT
## **Output 4 - Resposta do servidor**
// STATUS 204 - NO CONTENT



**Exercício 5**
## **Input 5 - Requisição GET para /users**
\# Body da requisição

NO CONTENT
## **Output 5 - Resposta do servidor**
[

`  `{

`      `"id": "1",

`      `"name": "Naruto Uzumaki",

`      `"email": "naruto@konoha.com",

`      `"age": 21

`  `},

`  `{

`    `"id": "2",

`    `"name": "Cygnus Hyoga",

`    `"email": "hyoga@cdz.com",

`    `"age": 14

`  `}

]

-----
# **Entregáveis**
## **Repositório**
- Link do **repositório** do **GitLab**
- **Código fonte:** 
  - arquivo **app.py**.
- **Privacidade** 
  - Incluir **ka-br-out-2020-correcoes** como reporter.
-----
# **Critérios de aceitação**

|**pts**|**Dado**|**Quando**|**É esperado**|
| :-: | :-: | :-: | :-: |
|1|<p>Rota /signup</p><p>funcionando corretamente</p>|POST realizado para rota /signup|Seja criado um novo usuário caso ele não exista, caso contrário, retorne um JSON vazio com status 422|
|1|<p>Rota /login</p><p>funcionando corretamente</p>|POST realizado para rota /login|Retorne um JSON com as informações do usuário, se o email ou senha estiverem inválidos, deve retornar uma resposta de erro|
|` `1|<p>Rota /profile/<int:user\_id></p><p>funcionando corretamente</p>|PATCH realizado para /profile/<int:user\_id>|Retorne um JSON com as informações do usuário atualizados e status 200|
|1|<p>Rota /profile/<int:user\_id></p><p>funcionando corretamente</p>|DELETE realizado para /profile/<int:user\_id>|Retorne um status 204 - NO CONTENT|
|1|<p>Rota /users </p><p>funcionando corretamente</p>|GET realizado para /users|Retorne um JSON com a lista de usuários registrados e o status 200 - OK|


**Boa diversão, devs! 🚀👨‍💻👩‍💻🚀**










