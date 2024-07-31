import base64
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, udf
from pyspark.sql.types import StringType
from faker import Faker

# Initialize Faker
fake = Faker()

# UDFs for Base64 encoding
def base64_encode(text):
    if text:
        return base64.b64encode(bytes(text, 'utf-8')).decode('utf-8')
    return text

# Register UDFs with PySpark
base64_encode_udf = udf(base64_encode, StringType())


def anonymize_data(input_csv, output_csv):
    spark = SparkSession.builder \
        .appName("AnonymizeData") \
        .getOrCreate()
    
    # Read the CSV file
    df = spark.read.csv(input_csv, header=True, inferSchema=True)
    
    # Anonymize the data
    anonymized_df = df.withColumn('first_name', base64_encode_udf(col('first_name'))) \
                      .withColumn('last_name', base64_encode_udf(col('last_name'))) \
                      .withColumn('address', base64_encode_udf(col('address')))
    
    # Write the anonymized data to a new CSV file
    anonymized_df.write.format('csv').csv(output_csv, header=True, mode='overwrite', encoding='utf-8')
    
    spark.stop()

# Run the anonymization process
anonymize_data('test_data.csv', 'anonymized_data.csv')