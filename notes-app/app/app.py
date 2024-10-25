# app/app.py
from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

# MySQL database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    note_content = request.form['note']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO notes (content) VALUES (%s)', (note_content,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/')

@app.route('/delete_note/<int:note_id>')
def delete_note(note_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM notes WHERE id = %s', (note_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

