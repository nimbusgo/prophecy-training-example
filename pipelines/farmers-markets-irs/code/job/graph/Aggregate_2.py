from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Aggregate_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("zip"))

    return df1.agg(count(lit(1)).alias("count"))