# Notes Here

I followed this article to create a CRUD todo app in python [link here](https://dev.to/__junaidshah/creating-a-crud-app-using-flask-and-sqlalchemy-2m5k)

I created a virtual environment so the module I installed are only in the virtual environment. I ran this command

`python3 -m venv venv`

Then to activate the virtual environment I ran this command since I am using Mac and ZSH

`source venv/bin/activate `

I created static and templates folder to be used with jinja. Then I needed to do pip installs for flask and sqlalchemy

`pip install flask`

`pip install flask_sqlalchemy`

I had issues creating a database file for sqlalchemy so I used this [link to stackoverflow](https://stackoverflow.com/questions/34122949/working-outside-of-application-context-flask#:~:text=Two%20possible%20solution)

Looking at that I ran the following commands in my terminal

`flask shell`

and then

`db.create_all()`

That created a database file called `todo.db` in the instance folder and then I moved it outside of the instance folder and deleted the folder.

I had issues finding the database file in my code so I had to use a solution I found from this [website](https://itnext.io/build-a-simple-crud-todo-app-with-python-flask-in-100-lines-of-code-or-less-97d8792f24be)

Eventually I was able to create different endpoints and specify the database schema, how I want to create, read, update and delete items from the sqlite database.