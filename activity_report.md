# Data Integration Tool Activities

## Activity 1: ETL with PySpark

### Environment Setup
- Installed Java JDK 11
- Installed Apache Spark 3.5.0 (pre-built for Hadoop 3.3)
- Installed Python 3.10 and pip
- Installed PySpark using `pip install pyspark`
- Set environment variables: `JAVA_HOME`, `HADOOP_HOME`, `SPARK_HOME`

### Files Used
- **sample_data.csv**
```csv
ID,Name,Age,Department,Salary
1,Alice,30,HR,60000
2,Bob,45,Finance,45000
3,Charlie,25,IT,70000
4,Diana,29,HR,52000
5,Edward,31,Finance,48000
```

- **etl_script.py**
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("BasicETL").getOrCreate()
df = spark.read.csv("data/sample_data.csv", header=True, inferSchema=True)
filtered_df = df.filter(col("Salary") > 50000).select("ID", "Name", "Salary")
filtered_df.write.csv("data/transformed_data.csv", header=True, mode="overwrite")
spark.stop()
```

### Result Output
`data/transformed_data.csv/part-0000...` contains:
```csv
ID,Name,Salary
1,Alice,60000
3,Charlie,70000
4,Diana,52000
```

### Issues Faced
- Needed winutils.exe for Windows compatibility
- Required setting up environment variables

### Learnings
- Understood how to create a SparkSession and perform ETL operations.
- Learned to apply filters and write output files in PySpark.

---

## Activity 2: Comparison of Apache Hadoop vs Apache Spark

| Feature         | Apache Hadoop                        | Apache Spark                                |
|----------------|--------------------------------------|---------------------------------------------|
| Architecture    | Disk-based with MapReduce framework  | In-memory processing with DAG engine         |
| Data Processing | Batch processing                     | Real-time & batch processing                 |
| Scalability     | Highly scalable (horizontal scaling) | Also scalable but more memory-intensive      |
| Ease of Use     | Steeper learning curve               | Easier with rich APIs (Python, Scala, etc.)  |
| Use Cases       | ETL, log processing, big data archiving | Real-time analytics, machine learning      |

### Summary
- **Hadoop** is suited for large batch processing on huge datasets stored in HDFS.
- **Spark** excels in iterative workloads, real-time stream processing, and machine learning due to its in-memory capabilities.
