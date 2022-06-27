from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *
from prophecy.utils import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_IrsZipcodesSource = IrsZipcodesSource(spark)
    df_Reformat_2 = Reformat_2(spark, df_IrsZipcodesSource)
    df_FarmersMarketsSource = FarmersMarketsSource(spark)
    df_Filter_1 = Filter_1(spark, df_FarmersMarketsSource)
    df_Reformat_5 = Reformat_5(spark, df_IrsZipcodesSource)
    df_Filter_2 = Filter_2(spark, df_Reformat_5)
    df_Aggregate_1 = Aggregate_1(spark, df_Reformat_2)
    df_Reformat_3 = Reformat_3(spark, df_Aggregate_1)
    df_Reformat_1 = Reformat_1(spark, df_Filter_1)
    df_Aggregate_2 = Aggregate_2(spark, df_Reformat_1)
    Target_2(spark, df_Reformat_3)
    df_Reformat_4 = Reformat_4(spark, df_Aggregate_2)
    Target_1(spark, df_Reformat_3)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.start(spark)
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
