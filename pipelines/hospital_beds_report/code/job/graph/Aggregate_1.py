from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Aggregate_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("date_string"))

    return df1.agg(
        sum(col("BED_UTILIZATION") * col("NUM_LICENSED_BEDS")).alias("utilized_beds"), 
        count(lit(1)).alias("num_rows")
    )
