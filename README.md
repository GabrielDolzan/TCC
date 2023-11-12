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

- Para execução é necessário possuir no ambiente os arquivos:
1. docker-compose.yml.
2. ./.env.prod.db
3. ./frontend/nginx.conf
4. ./backend/.env
5. ./backend/entrypoint.sh
6. ./nginx/default.conf

- Executar `docker-compose up -d`.