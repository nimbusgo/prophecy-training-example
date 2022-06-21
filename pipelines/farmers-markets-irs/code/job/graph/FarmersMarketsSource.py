from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def FarmersMarketsSource(spark: SparkSession) -> DataFrame:
    if Config.fabricName == "demos":
        return spark.read\
            .option("header", True)\
            .option("sep", ",")\
            .csv("dbfs:/databricks-datasets/data.gov/farmers_markets_geographic_data/data-001/market_data.csv")
    else:
        raise Exception("No valid dataset present to read fabric")
