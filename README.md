# TCC

## Objetivo
- Projeto desenvolvido para verificar informações monitoradas em Jogos Sérios por meio de Dashboards.

## Desenvolvimento

- Para o desenvolvimento foi utilizado docker com 3 containers principais: frontend, backend e banco de dados.

### Frontend

- Utilizado VueJS 3.

### Backend

- Utilizado Django.

### Banco de dados

- Utilizado PostgreSQL.

## Containers

1. frontend

- Container responsável pelo frontend. Necessário arquivo `./frontend/nginx.conf`.

2. gunicorn

- Container responsável pelo backend. Necessário arquivos `./backend/.env` e `./backend/entrypoint.sh`.

3. db

- Container responsável pelo banco de dados. Necessário arquivo `./.env.prod.db`.

4. nginx

- Container responsável pelo tratamento das requisições. Necessário do arquivo `./nginx/default.conf`.

## Execução

### Local

- Para execução local apenas executar `docker-compose up -d`.

### Produção

Para execução é necessário possuir no ambiente os arquivos:

- [docker-compose.yml](docker-compose.yml)
- [.env.prod.db](.env.prod.db)
- [frontend](frontend)
  - [nginx.conf](frontend/nginx.conf)
- [backend](backend)
  - [.env](backend/.env)
  - [entrypoint.sh](backend/entrypoint.sh)
- [nginx](nginx)
  - [default.conf](nginx/default.conf)

Executar `docker-compose up -d`.