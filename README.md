<a name="readme-top"></a>

<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## CRM Service
Django API for a CRM Service.

</div>

<details>
<summary>Tabla de contenidos</summary>

- [Install and setting up the app](#Install-and-setting-up-the-app)
- [Using the app](#Using-the-app)
  - [Create super user](#Create-super-user)
  - [Launch the app](#Launch-the-app)

</details>

## Install and setting up the app
```shell
pip install -r requirements.txt
```

```shell
python manage.py makemigrations
python manage.py migrate
```

## Using the app
### Create super user
```shell
python manage.py createsuperuser
```

### Launch the app
```shell
python manage.py runserver
```
open http://127.0.0.1:8000/
