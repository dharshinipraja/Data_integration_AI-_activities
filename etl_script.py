from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark session
spark = SparkSession.builder.appName("BasicETL").getOrCreate()

# Read the input CSV
df = spark.read.csv("data/sample_data.csv", header=True, inferSchema=True)

# Transformation: Filter and select
filtered_df = df.filter(col("Salary") > 50000).select("ID", "Name", "Salary")

# Write to new CSV
filtered_df.write.csv("data/transformed_data.csv", header=True, mode="overwrite")

# Stop the Spark session
spark.stop()
