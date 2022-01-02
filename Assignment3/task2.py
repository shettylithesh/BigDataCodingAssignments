import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import col

cityPath=sys.argv[1]
globalPath=sys.argv[2]

sc = SparkContext.getOrCreate()
sql_context = SQLContext(sc)

df = sql_context.read.csv(cityPath , header=True)
#df.show()
df = df.withColumn('AverageTemperature', col('AverageTemperature').cast('float'))
#df.show()

df=df.groupBy(['Country','dt']).max('AverageTemperature')
df= df.withColumnRenamed("max(AverageTemperature)", "maxtempcity")


df2 = sql_context.read.csv(globalPath, header=True)
df2 = df2.withColumn('LandAverageTemperature', col('LandAverageTemperature').cast('float'))

df= df.join(df2,["dt"])
df = df.filter(df.maxtempcity > df.LandAverageTemperature)

df= df.groupBy('Country').count().orderBy("Country")
for row in df.collect():
	print(row['Country'].strip(), row['count'],sep='\t')

#command to run
#/opt/spark/bin/pyspark < task1.py cmdline args
