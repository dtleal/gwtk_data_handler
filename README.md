# gwtk_data_handler

An awesome Pizza Place

## How its work
This project is a Clean-Architecture based. We have 3 important layers
Frameworks: responsible for all interactions with the external world
Interface Adapters: responsible for adapt the external world into business logic
Domain (Applicaion + entities): responsible for create and exec all business logic in fact

In this project we have:
    FastAPI
    Dependency-Injector
    SqlAlchemy
    Poetry
    Docker
    Postgres
    Pydantic
    Alembic

# How to start?

IMPORTANT.: See the `makefile` (please, use make style to get a better code)to get to know some alias and follow the commands

1. We use poetry to deal with dependency management, so take a look in poetry documentation for more details. To create an environment, run:

$ poetry shell - create/actiate a new environment
$ poetry install - install project dependencies

2. Using Makefile, please run as following
    a. make db_up (this will create our awesome postgres database)
    b. make db_create_tables (this will create our tables using alembic)
    c. make db_insert_data (this will persist our CSV files into database)

3. Now we have our database setting up and stored, lets run our application
    a. make run (without debug)
    or
    b. make debug (to see the FastAPI debug)

4. Take a look at swagger accesing /docs on your local to see our routes
    example: https:localhost:8000/docs
