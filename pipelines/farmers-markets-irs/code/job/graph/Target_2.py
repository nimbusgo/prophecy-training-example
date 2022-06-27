from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Target_2(spark: SparkSession, in0: DataFrame):
    if spark.catalog._jcatalog.tableExists(f"test.zip_delta"):
        from delta.tables import DeltaTable, DeltaMergeBuilder
        DeltaTable\
            .forName(spark, f"test.zip_delta")\
            .alias("target")\
            .merge(in0.alias("source"), (col("source.zip") == col("target.zip")))\
            .whenMatchedUpdateAll()\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write.format("delta").mode("overwrite").saveAsTable("test.zip_delta")
