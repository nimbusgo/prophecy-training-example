from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def hospital_beds(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder

    if DeltaTable.isDeltaTable(spark, "dbfs:/Prophecy/nimbus@simpledatalabs.com/training/hospital_beds_delta"):
        DeltaTable\
            .forPath(spark, "dbfs:/Prophecy/nimbus@simpledatalabs.com/training/hospital_beds_delta")\
            .alias("target")\
            .merge(
              in0.alias("source"),
              (
                (col("source.date_string") == col("target.date_string"))
                & (col("source.OBJECTID") == col("target.OBJECTID"))
              )
            )\
            .whenMatchedUpdateAll()\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write\
            .format("delta")\
            .mode("overwrite")\
            .save("dbfs:/Prophecy/nimbus@simpledatalabs.com/training/hospital_beds_delta")
