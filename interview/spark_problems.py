from pyspark.sql import SparkSession
from pyspark.sql import functions as F

class SparkTransformations:
    """
    Fix the PySpark transformations to make all tests pass.
    """
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("InterviewTest") \
            .master("local[1]") \
            .getOrCreate()

    def calculate_age_statistics(self, df):
        """
        Bug: Calculate correct age statistics from a DataFrame
        Input DataFrame schema: name (string), age (integer)
        Should return: DataFrame with columns (avg_age, max_age, min_age)
        """
        return df.agg(
            F.avg("age").alias("avg_age"),
            # Bug: Using sum instead of max
            F.sum("age").alias("max_age"),
            # Bug: Using count instead of min
            F.count("age").alias("min_age")
        )

    def find_top_customers(self, orders_df):
        """
        Bug: Find top 5 customers by total order value
        Input DataFrame schema: customer_id (integer), order_value (double)
        Should return: DataFrame with columns (customer_id, total_value)
        """
        return orders_df.groupBy("customer_id") \
            # Bug: Using avg instead of sum
            .agg(F.avg("order_value").alias("total_value")) \
            .limit(5) 