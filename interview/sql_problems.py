import sqlite3
from typing import List, Tuple

class SQLQueries:
    """
    Fix the SQL queries to produce the correct results.
    Each method should return a SQL query string.
    """
    def __init__(self):
        self.conn = sqlite3.connect('data/interview.db')
        self.cursor = self.conn.cursor()
    
    def get_product_sales_report(self) -> str:
        """
        Bug: Should return products with their total revenue and quantity sold
        Expected columns: product_name, total_revenue, units_sold
        Ordered by revenue (highest first)
        """
        return """
        SELECT p.name as product_name, 
               COUNT(oi.quantity) as units_sold
        FROM products p
        LEFT JOIN order_items oi ON p.id = oi.product_id
        -- Bug: Missing revenue calculation
        -- Bug: Missing proper GROUP BY
        -- Bug: Missing ORDER BY
        """
    
    def find_top_customers(self) -> str:
        """
        Bug: Find customers who spent more than average
        Return their name, total spent, and number of orders
        """
        return """
        SELECT u.name, COUNT(o.id) as order_count
        FROM users u
        JOIN orders o ON u.id = o.user_id
        -- Bug: Missing joins with order_items
        -- Bug: Missing total spent calculation
        -- Bug: Missing HAVING clause for above average
        GROUP BY u.id
        """
    
    def execute_query(self, query: str) -> List[Tuple]:
        """Execute a query and return results"""
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def __del__(self):
        self.conn.close()

    def get_top_products(self):
        """
        Bug: Should return top 5 products by revenue
        Tables: 
        - products (id, name, price)
        - orders (id, product_id, quantity, order_date)
        """
        return """
        SELECT p.name, SUM(o.quantity) as total_sold
        FROM products p
        JOIN orders o ON p.id = o.product_id
        -- Bug: Missing GROUP BY
        -- Bug: Missing ORDER BY
        LIMIT 5
        """

    def find_active_users(self):
        """
        Bug: Should find users who made at least 3 orders in the last 30 days
        Tables:
        - users (id, name, email)
        - orders (id, user_id, order_date)
        """
        return """
        SELECT u.name, COUNT(*) as order_count
        FROM users u
        JOIN orders o ON u.id = o.user_id
        -- Bug: Missing WHERE clause for date range
        -- Bug: Missing GROUP BY and HAVING
        """ 