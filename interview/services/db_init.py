import sqlite3
import os

def init_database():
    """Initialize the SQLite database with sample data"""
    # Ensure the data directory exists
    os.makedirs('data', exist_ok=True)
    
    conn = sqlite3.connect('data/interview.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.executescript("""
        DROP TABLE IF EXISTS products;
        DROP TABLE IF EXISTS orders;
        DROP TABLE IF EXISTS users;
        DROP TABLE IF EXISTS order_items;
        
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price DECIMAL(10,2),
            category TEXT,
            stock INTEGER
        );
        
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
        
        CREATE TABLE order_items (
            id INTEGER PRIMARY KEY,
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            price_at_time DECIMAL(10,2),
            FOREIGN KEY (order_id) REFERENCES orders (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
        );
    """)
    
    # Insert sample data
    cursor.executescript("""
        INSERT INTO products (name, price, category, stock) VALUES
        ('Laptop', 999.99, 'Electronics', 50),
        ('Smartphone', 499.99, 'Electronics', 100),
        ('Headphones', 79.99, 'Electronics', 200),
        ('Coffee Maker', 39.99, 'Kitchen', 30),
        ('Blender', 29.99, 'Kitchen', 40);
        
        INSERT INTO users (name, email) VALUES
        ('John Doe', 'john@example.com'),
        ('Jane Smith', 'jane@example.com'),
        ('Bob Wilson', 'bob@example.com');
        
        INSERT INTO orders (user_id, status) VALUES
        (1, 'completed'),
        (1, 'completed'),
        (2, 'pending'),
        (3, 'completed'),
        (2, 'cancelled');
        
        INSERT INTO order_items (order_id, product_id, quantity, price_at_time) VALUES
        (1, 1, 1, 999.99),
        (1, 3, 2, 79.99),
        (2, 2, 1, 499.99),
        (3, 4, 3, 39.99),
        (4, 5, 2, 29.99),
        (4, 3, 1, 79.99);
    """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database() 