from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Reformat_5(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        sum(expr("if(((NOT (zipcode = '00000')) AND (NOT (zipcode = '99999'))), 1, 0)")).alias("zip_count")
    )
