import sqlite3
from typing import Dict, List
from collections import defaultdict

class DataAnalyzer:
    """
    This class combines SQL queries with Python data processing.
    Fix the implementations to make all tests pass.
    """
    def __init__(self):
        self.conn = sqlite3.connect('data/interview.db')
        self.conn.row_factory = sqlite3.Row
    
    def get_category_statistics(self) -> Dict:
        """
        Bug: Calculate statistics for each product category
        Should return: {
            category: {
                'avg_price': float,
                'total_stock': int,
                'product_count': int
            }
        }
        """
        cursor = self.conn.cursor()
        # Bug: Query is incorrect
        cursor.execute("SELECT category, price FROM products")
        rows = cursor.fetchall()
        
        # Bug: Statistics calculation is incorrect
        stats = defaultdict(lambda: {'avg_price': 0, 'total_stock': 0, 'product_count': 0})
        for row in rows:
            category = row['category']
            stats[category]['avg_price'] += row['price']
            
        return dict(stats)
    
    def analyze_user_behavior(self) -> List[Dict]:
        """
        Bug: Analyze user purchasing patterns
        Should return list of users with their:
        - most bought category
        - average order value
        - total orders
        """
        cursor = self.conn.cursor()
        # Bug: Missing joins and calculations
        cursor.execute("""
            SELECT u.name, o.id
            FROM users u
            JOIN orders o ON u.id = o.user_id
        """)
        rows = cursor.fetchall()
        
        # Bug: Analysis is incomplete
        return [{'name': row['name'], 'orders': 1} for row in rows]
    
    def __del__(self):
        self.conn.close() 