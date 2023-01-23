# Documentation

I have a link to the notes on some of my issues during this project [notes](https://github.com/ahmedk2/todo/blob/main/notes/Notes.md)

To run this project you need to make sure you have python installed on your system. It should be available on your computer if you type `python`. However if you do not have it you can download it using this [link](https://www.python.org/downloads/)

Once you have python installed run this to create a virtual environment

`python3 -m venv venv`

Then to activate the virtual environment

`source venv/bin/activate`

Install these modules in the virtual environment

`pip install flask`

`pip install flask_sqlalchemy`

You should be able to run this app locally using this command

`python app.py`

## Optional Section

You may need to run the following two commands to create a database file. Then execution app.py would work.

```python
flask shell

db.create_all()
```
