import pytest
from interview.sql_problems import SQLQueries

@pytest.fixture
def sql():
    return SQLQueries()

def test_product_sales_report(sql):
    query = sql.get_product_sales_report()
    results = sql.execute_query(query)
    
    # Verify the results
    assert len(results) > 0
    # Laptop should be highest revenue
    assert results[0][0] == 'Laptop'
    assert float(results[0][1]) > 900  # Total revenue
    assert results[0][2] == 1  # Units sold

def test_top_customers(sql):
    query = sql.get_top_customers()
    results = sql.execute_query(query)
    
    # Verify the results
    assert len(results) > 0
    # John Doe should be top customer
    assert 'John Doe' in results[0]
    assert results[0][1] > 1000  # Total spent
    assert results[0][2] == 2  # Number of orders 