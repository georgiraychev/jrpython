import pytest
from pyspark.sql import Row
from interview.spark_problems import SparkTransformations

@pytest.fixture
def spark_transformer():
    return SparkTransformations()

def test_age_statistics(spark_transformer):
    test_data = [
        Row(name="Alice", age=25),
        Row(name="Bob", age=30),
        Row(name="Charlie", age=35)
    ]
    df = spark_transformer.spark.createDataFrame(test_data)
    result = spark_transformer.calculate_age_statistics(df)
    
    row = result.collect()[0]
    assert row.avg_age == 30.0
    assert row.max_age == 35
    assert row.min_age == 25

def test_top_customers(spark_transformer):
    test_data = [
        Row(customer_id=1, order_value=100.0),
        Row(customer_id=1, order_value=150.0),
        Row(customer_id=2, order_value=50.0),
        Row(customer_id=3, order_value=300.0)
    ]
    df = spark_transformer.spark.createDataFrame(test_data)
    result = spark_transformer.find_top_customers(df)
    
    rows = result.collect()
    assert len(rows) == 3
    assert rows[0].customer_id == 3  # Highest total
    assert rows[0].total_value == 300.0 