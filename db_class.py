from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://y:123@localhost:5432/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["IMAGE_UPLOADS"] = 'uploads'
db = SQLAlchemy(app)

class List(db.Model):
  __tablename__ = 'list'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  def __repr__(self):
    return "<List ID: {}, name: {}>".format(self.id, self.name)


class Todo(db.Model):
  __tablename__ = 'todo'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  date = db.Column(db.String())
  description = db.Column(db.String())
  list_id = db.Column(db.Integer, db.ForeignKey('list.id'))
  list = db.relationship(List)



  def __repr__(self):
    return "<Todo ID: {}, name: {}, List Id:{}>".format(self.id, self.name, self.list_id)
db.create_all()
