from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute('CREATE TABLE if not exists accounts (username TEXT, password TEXT, email TEXT)')
print("Table created successfully");
conn.close()
  
  
@app.route('/')
def index():
    msg = ''
    return render_template('main.html', msg = msg)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    msg = ''
    return render_template('main.html', msg = msg)
  
@app.route('/logout')
def logout():
    return redirect(url_for('login'))
  
@app.route('/register')
def register():
    msg = ''
    msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)


if __name__ == '__main__':
    app.run()
