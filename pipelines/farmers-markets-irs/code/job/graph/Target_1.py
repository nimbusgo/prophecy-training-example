from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Target_1(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder

    if DeltaTable.isDeltaTable(spark, "dbfs:/FileStore/Users/nimbus/training/zip_delta"):
        DeltaTable\
            .forPath(spark, "dbfs:/FileStore/Users/nimbus/training/zip_delta")\
            .alias("target")\
            .merge(in0.alias("source"), (col("source.zip") == col("target.zip")))\
            .whenMatchedUpdateAll()\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write.format("delta").mode("overwrite").save("dbfs:/FileStore/Users/nimbus/training/zip_delta")
