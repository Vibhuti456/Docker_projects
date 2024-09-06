from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
def get_db_connection():
    connection = mysql.connector.connect(
        host='db',  # Docker service name for MySQL
        user='root',
        password='rootpassword',
        database='shopping_cart'
    )
    return connection

# Create the products table if it doesn't exist
def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            price FLOAT
        )
    ''')
    connection.commit()
    cursor.close()
    connection.close()

create_table()

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form['name']
    price = request.form['price']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO products (name, price) VALUES (%s, %s)', (name, price))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

