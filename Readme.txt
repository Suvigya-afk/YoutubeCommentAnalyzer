Issue 1--> While creating virtual enviroment in windows we might face error with the usual process of creating directory -> running
command -> (python -m venv env) and then command (env/Scripts/activate.bat).
Solution--> To resolve above issue run below two command in order:
cmd 1: (Set-ExecutionPolicy RemoteSigned)
cmd 2: env/Scripts/activate

Issue 2--> `django-admin startproject backend` -> this command creates a new project called 'backend'

Issue 3--> `python manage.py startapp api` -> this command creates a new app called 'api' inside the directory.

Issue 4--> `pip install -r requirements.txt` -> this command installs all the packages mentioned inside the 'requirements.txt' file.

Issue 5--> The 'author' field in api/models.py is used to link the 'User' model and the 'Comments' model. If any particular user gets
deleted then all the relat ed commnets will be deleted (This will be useful for us when we want to empty out the database). Also the
'related_name' field helps to list out all the comments related to a User.