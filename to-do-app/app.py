from flask import Flask, render_template, request, redirect
from urllib.parse import quote as url_quote
import mysql.connector

app = Flask(__name__)

# Function to get the MySQL connection
def get_db_connection():
    conn = mysql.connector.connect(
        host='mysql',  # Name of the MySQL container
        user='root',  # MySQL root user
        password='rootpass',  # MySQL root password
        database='todo'  # Database name
    )
    return conn

# Initialize database
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(255) NOT NULL
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Route to display the list of tasks
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Route to add a task
@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()  # Initialize the database on app startup
    app.run(host='0.0.0.0', port=5000)

