from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def hospital_beds_input(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("X", DoubleType(), True), StructField("Y", DoubleType(), True), StructField("OBJECTID", IntegerType(), True), StructField("HOSPITAL_NAME", StringType(), True), StructField("HOSPITAL_TYPE", StringType(), True), StructField("HQ_ADDRESS", StringType(), True), StructField("HQ_ADDRESS1", StringType(), True), StructField("HQ_CITY", StringType(), True), StructField("HQ_STATE", StringType(), True), StructField("HQ_ZIP_CODE", IntegerType(), True), StructField("COUNTY_NAME", StringType(), True), StructField("STATE_NAME", StringType(), True), StructField("STATE_FIPS", IntegerType(), True), StructField("CNTY_FIPS", IntegerType(), True), StructField("FIPS", IntegerType(), True), StructField("NUM_LICENSED_BEDS", IntegerType(), True), StructField("NUM_STAFFED_BEDS", IntegerType(), True), StructField("NUM_ICU_BEDS", IntegerType(), True), StructField("BED_UTILIZATION", DoubleType(), True), StructField("Potential_Increase_In_Bed_Capac", IntegerType(), True)
        ])
        )\
        .option("header", True)\
        .option("inferSchema", True)\
        .option("sep", ",")\
        .csv(f"dbfs:/databricks-datasets/COVID/ESRI_hospital_beds/Definitive_Healthcare__USA_Hospital_Beds_{Config.INPUT_DATE}.csv")
