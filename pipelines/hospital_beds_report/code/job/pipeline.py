from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *
from prophecy.utils import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_hospital_beds = hospital_beds(spark)
    df_Aggregate_1 = Aggregate_1(spark, df_hospital_beds)
    df_Reformat_1 = Reformat_1(spark, df_Aggregate_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "2109/pipelines/hospital_beds_report")
    MetricsCollector.start(spark = spark, pipelineId = "2109/pipelines/hospital_beds_report")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
