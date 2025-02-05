class SQLQueries:
    """
    Fix the SQL queries to produce the correct results.
    Each method should return a SQL query string.
    """
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