from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "todo.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    description = db.Column(db.String(200), nullable=False)
    def __repr__(self) :
        return "{} is the title and {} is the description".format(self.title,self.description)


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

@app.route("/delete/<int:sno>")
def delete(sno):
    deletetodo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(deletetodo)
    db.session.commit()
    return redirect("/")

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

if __name__ == '__main__':
        app.run()
