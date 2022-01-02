import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import col
import pyspark.sql.functions as F

sc = SparkContext.getOrCreate()
sql_context = SQLContext(sc)

country = sys.argv[1]
#country = "India"
pathtocity = sys.argv[2]
#df = sql_context.read.csv('/home/pes1ug19cs567/Desktop/a3/task1/city_sample_5percent.csv', header=True)
df = sql_context.read.csv(pathtocity, header=True)
df = df.withColumn('AverageTemperature', col('AverageTemperature').cast('float'))
df = df.filter(df.Country == country)



dfcity = df.groupBy('City').avg('AverageTemperature')
dfjoin = df.join(dfcity, ['City'])
dfjoin = dfjoin.withColumnRenamed("avg(AverageTemperature)", "avgtempcity")
dfjoin = dfjoin.filter(dfjoin.AverageTemperature > dfjoin.avgtempcity)
xxx = dfjoin.groupBy('City').count().orderBy("City")
rdd1 = xxx.rdd

for row in rdd1.collect():
	print(row['City'], row['count'], sep='\t')


#command to run
#/opt/spark/bin/pyspark < task1.py cmdline args





# df = df.filter(df.word == word) # transformation

# counts_by_rec = df.groupBy(df.recognized).agg(
#     {"Total_Strokes": "avg"}).collect()

# num_items = len(counts_by_rec)
# if num_items > 0:
#     counts_by_rec = sorted(list(map(lambda x: (x[0], x[1]), counts_by_rec)))
#     output_dict = {"True": 0, "False": 0}

#     for status, avg in counts_by_rec:
#         output_dict[status] = avg

#     print(round(output_dict["True"], 5))
#     print(round(output_dict["False"], 5))
# else:
#     print("0.00000")
#     print("0.00000")
