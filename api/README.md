# Shipay Backend Challenge - Wep API

Web api implementada  para o processo seletivo de Desenvolvedor Backend da Shipay.
Este projeto consiste em persistir e recuperar dados de um usuário e seus respectivos papéis e Claims 
em um banco de dados PostgreSQL atráves da api

## Como rodar o projeto
---
Primeiramente você deve ter uma instância do banco de dados PostgreSQL rodando um sua  máquina,
você pode fazer isso facilmente rodando-o dentro de um contâiner docker com o comando:

```console
sudo docker run --name psql-users-db \             
    -e POSTGRES_PASSWORD=pass \
    -e POSTGRES_USER=usr \
    -e POSTGRES_DB=usersdb \
    -p 5432:5432 \
    -d postgres
```

Com o banco de dados rodando em nossa máquina localmente, podemos rodar o projeto fácimente,
para isso, primeiro temos que instalar as dependencias:

```console
pip install -r requirements.txt
```

Então, devemos criar um arquivo .env na raiz do nosso projeto. Nele estará as variáveis de ambiente necessárias ao projeto, você deverá setar a variável DATABASE_URL nesse aquivo como a connection string para acessar o nosso banco de dados:

```.env
DATABASE_URL=postgresql://usr:pass@localhost:5432/postgres
```

Depois disso, podemos rodar nossa API:

```console
python -m api
```

## Endpoints
---
#### Recuperando papel de usuário por Id:

- Endpoint: /user/<<int:id>>

    - Body: Requisição sem corpo

    - Verbo Http: GET

    - Resposta Esperada: 
        ```json
            [
                {
                    "claim_description": "example",
                    "email": "vh141299@gmail.com",
                    "name": "Victor",
                    "role_description": "ADMIN"
                },
                {
                    "claim_description": "EXAMPLO2",
                    "email": "vh141299@gmail.com",
                    "name": "Victor",
                    "role_description": "ADMIN"
                }
            ]
        ```

    - Status: 200

- Endpoint: /user

    - Body:
        ```json
            {
                "name": "Maria",
                "email": "maria@gmail.com",
                "password": "1234",
                "role_id": 1
            }
        ```

    - Verbo Http: POST

    - Resposta Esperada: 
        ```json
            {
                "message": "created"
            }
        ```

    - Status: 201

## Realizando o deploy
---

Para fazer o deploy, temos várias opções. Para uma opção sem custos temos a plataforma heroku que faz o serviço de deploy gratuitamente, nesse caso teriamos um servidor wsgi para rodar a api e ainda contaríamos com um banco PostgreSQL também disponibilizado pela plataforma.
Caso houvesse o requisito da API estar hospedada em uma plataforma de Cloud, poderíamos utilizar a AWS, subindo a API no EKS e criando uma Instancia do PostgreSQL no Amazon RDS.