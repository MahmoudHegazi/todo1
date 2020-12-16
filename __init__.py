#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import render_template, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from db_class import List, Todo, db, app
import requests
import os
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename



@app.route('/<int:listid>')
def todoList(listid):
    todos = Todo.query.filter_by(list_id=listid).all()
    lists = List.query.all()
    #todo = Todo(name='Lovely Todo')
    #db.session.add(todo)
    #db.session.commit()
    return render_template('index.html', todos=todos, lists=lists)

@app.route('/')
def index():
    #lis = List(name='last')
    #db.session.add(lis)
    #db.session.commit()

    #todo = Todo(name='Nice todo', list_id=2)
    #db.session.add(todo)
    #db.session.commit()
    todos = Todo.query.all()
    lists = List.query.all()
    return render_template('index.html', todos=todos, lists=lists)

@app.route('/add_todo', methods=['POST'])
def adder_todo():
    if request.method == 'POST':
        todo_name = request.form.get("todoname")
        todo_date = request.form.get("tododate")
        list_id = request.form.get("todolist")
        lis = Todo(name=todo_name, date=todo_date, list_id=list_id)
        db.session.add(lis)
        db.session.commit()
        todos = Todo.query.all()
        lists = List.query.all()
        db.session.close()
        flash('New Todo Item Added')
        return redirect(url_for('todoList', listid=list_id))
        return render_template('index.html', todos=todos, lists=lists)


@app.route('/add_list', methods=['POST'])
def adder_list():
    if request.method == 'POST':
        list_name = request.form.get("listname")
        the_list = List(name=list_name)
        db.session.add(the_list)
        db.session.commit()
        todos = Todo.query.all()
        lists = List.query.all()
        db.session.close()
        flash('New Todo Item Added')
        return redirect(url_for('todoList', listid=the_list.id))
        return render_template('index.html', todos=todos, lists=lists)

@app.route('/delete_todo', methods=['POST','GET'])
def deleteTodo():
    if request.method == 'POST':
        todo_id = request.form.get("todo_id")
        todo_delete = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo_delete)
        db.session.commit()
        db.session.close()
        flash_message = todo_id
        flash_message += '| Item Deleted ID: ' + str(todo_id)
        return flash_message
    return
if __name__ == '__main__':
    app.secret_key = 'S&Djry636qyye21777346%%^&&&#^$^^y___'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
