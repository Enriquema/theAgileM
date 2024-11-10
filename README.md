<a name="readme-top"></a>

<div align="center">

## CRM Service
Django API for a CRM Service.

</div>

<details>
<summary>Content table</summary>

- [Install and setting up the app](#Install-and-setting-up-the-app)
- [Using the app](#Using-the-app)
  - [Create super user](#Create-super-user)
  - [Launch the app](#Launch-the-app)

</details>

## Install and setting up the app
The following command will let you install the required libraries to have the web app and the API running.
```shell
pip install -r requirements.txt
```

Once you have download and installed all the required libraries, you can go to the project folder:
```shell
cd theagile_crm
```
And apply the corresponding database creation and migrations in order to set up the database schema for your project and have everything ready to work.
```shell
python manage.py makemigrations
python manage.py migrate
```

## Using the app
### Create super user
The following command will allow you to have a super user, which will be the super user to manage normal users.
```shell
python manage.py createsuperuser
```

### Launch the app
Finally, just start running the web app/API locally.
```shell
python manage.py runserver
```
And open the following link http://127.0.0.1:8000/ in order to check whatever you need.
>Note: Please take into account, that if you are using the port 8000 locally, your Django web app could be using other port, just read the Django logging from you terminal.
