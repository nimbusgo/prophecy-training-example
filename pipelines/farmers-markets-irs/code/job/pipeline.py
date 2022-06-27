from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *
from prophecy.utils import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_IrsZipcodesSource = IrsZipcodesSource(spark)
    df_FilterOutBadZips = FilterOutBadZips(spark, df_IrsZipcodesSource)
    df_CastDataTypes = CastDataTypes(spark, df_FilterOutBadZips)
    df_GroupByZip = GroupByZip(spark, df_CastDataTypes)
    df_FarmersMarketsSource = FarmersMarketsSource(spark)
    df_FilterOutNullZips = FilterOutNullZips(spark, df_FarmersMarketsSource)
    df_Aggregate_5 = Aggregate_5(spark, df_FilterOutNullZips)
    df_Reformat_9 = Reformat_9(spark, df_GroupByZip)
    df_Join_1 = Join_1(spark, df_Aggregate_5, df_Reformat_9)
    df_Reformat_12 = Reformat_12(spark, df_Join_1)
    df_Reformat_11 = Reformat_11(spark, df_Reformat_12)
    df_Reformat_13 = Reformat_13(spark, df_Reformat_11)
    df_Filter_2 = Filter_2(spark, df_Reformat_13)
    df_Reformat_1 = Reformat_1(spark, df_Reformat_13)

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
