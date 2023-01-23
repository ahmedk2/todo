from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os


#* Here we are specifying the app configuration and the database connection
app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "todo.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

#* We are creating a database called todo.db and the related columns
class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    description = db.Column(db.String(200), nullable=False)
    def __repr__(self) :
        return "{} is the title and {} is the description".format(self.title,self.description)


#* This is the first endpoint for the home page
#* The get method is used when you fetch the URL http://127.0.0.1:5000 displays all the data in the todo database
#* The post method creates a new record in the todo database when you enter the title and description
#* The index.html file is used to display the data when a post or get method is used on the url

@app.route("/",methods=['POST', 'GET'])
def main_page():
    if request.method=='POST':
        title=request.form['title']
        description=request.form['description']
        todo=Todo(title=title ,description=description)
        db.session.add(todo)
        db.session.commit()
    alltodos=Todo.query.all()
    return render_template('index.html',todos=alltodos)


#* This is another endpoint that is called when the delete button is pressed on the index.html page
#* The point of this is to take the first occurrence of an index (sno) number. 
#* It does this by using the filter_by and first methods
#* It deletes that record from the database, save (commit) the data and return the user to the home page 

@app.route("/delete/<int:sno>")
def delete(sno):
    deletetodo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(deletetodo)
    db.session.commit()
    return redirect("/")

#* This endpoint is used to update records in the database when the update button is clicked on the home page
#* On the home page the update button is linked to an update.html file that has a new form to update the record
#* specified by the sno (database index) parameter
#* It takes the new data from the form and updates the record in the database by committing the SQL query
#* Then it returns the user to the home page and queries the database for all records

@app.route("/updatetodo/<int:sno>",methods=['POST','GET'])
def update_todo(sno):
    if request.method == 'POST':
        updatetodo = Todo.query.filter_by(sno=sno).first()
        title = request.form['title']
        description = request.form['description']
        todo = Todo(title=title, description=description)
        updatetodo.title=title
        updatetodo.description=description
        db.session.commit()
        return redirect("/")
    updatetodo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', updatetodo=updatetodo)

#* This is used to run the application when this file is executed via python

if __name__ == '__main__':
        app.run()
