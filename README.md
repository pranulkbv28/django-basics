# DJANGO BASICS

## PREREQUISITES

- Python
- pip
- python basics

## INSTALLATION

- `cd` into the project folder
- create an `environment`, so you do not install globally

```bash
    python -m venv your-env
```

- activate the environment

For mac/Linux:

```bash
    source your-env/bin/activate
```

For Windows:

```powershell
    .\your-env\Scripts\activate
```

- install django

```bash
    pip install django djangorestframework
```

## BASIC USAGE

- create a `django` project

```bash
    django-admin startproject project_name
```

- after this, you will see a folder named `project_name` let us callit  `project`, and in it, there will be another folder named the same and a `manage.py` file.

- in the `project` folder, there will be a lot of `.py` files like the `urls.py`, `settings.py` to name a few.

- here, the `settings.py` file has the `project's` settings maintained. As in, the `db info`, the `secret key`, etc. We will also be maintaining the `apps`, and other cvonfigurations here.

- the `urls.py` file has the `urls` of the project.

- in `django`, you cn create `apps` which are basically `microservices`, or in other words, `functionalities` of the project. This brings a lot of flexibilty to the project and also helps in organising it.

- Let us go ahead and create one

```bash
    django-admin startapp app_name
```

- now, a folder with the name `app_name` will be created with similar and others files to the `project` in it.

- in the `app`, you will find a file named `models.py`, in which you will be defing the models of the data that you will be storing in the `database`.

- there is another file named `views.py` in which you will be defining the `views` of the `app`. Which essentially means, the `functionalities`.

- please check app folders like `api` and `custom_auth` to check how the files are connected.

## HOW TO RUN THE PROJECT

- before running the `project` for the first time, you have to run a few commands.

- `cd` into the directory which contains the `manage.py` file

``` bash
    python manage.py makemigrations
    python manage.py migrate
```

- after this is done successfully, you can now run the `server`. Usually, you can run the server even without these, but to avoid warnings and build some practice, it is better to do this as well.

- run the server with the following commands

```bash
    python manage.py runserver
```

### NOTE

- whenever there are any changes in any of the `models.py` files, you will have to stop the server, run the `makemigrations` and `migrate` commands, and start the server again.
  