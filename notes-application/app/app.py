from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="notes-db",
        user="user",
        password="userpass",
        database="notes_db"
    )
    return connection

# Create the table if it does not exist
def initialize_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content TEXT NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

initialize_db()

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("index.html", notes=notes)

@app.route('/add', methods=["POST"])
def add_note():
    content = request.form["content"]
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for("index"))

@app.route('/delete/<int:id>')
def delete_note(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM notes WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

