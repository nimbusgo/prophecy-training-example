from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Aggregate_3(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("zipcode"))

    return df1.agg(collect_set(col("STATE")).alias("states"))
