from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def IrsZipcodesSource(spark: SparkSession) -> DataFrame:
    if Config.fabricName == "demos":
        return spark.read\
            .option("header", True)\
            .option("sep", ",")\
            .csv("dbfs:/databricks-datasets/data.gov/irs_zip_code_data/data-001/2013_soi_zipcode_agi.csv")
    else:
        raise Exception("No valid dataset present to read fabric")
