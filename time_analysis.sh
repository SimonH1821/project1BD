#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1BD/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1BD/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /project1BD/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/nyc_parking_violations.csv /project1BD/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/project1BD/mapper.py -mapper ../../mapreduce-test-python/project1BD/mapper_time.py \
-file ../../mapreduce-test-python/project1BD/reducer.py -reducer ../../mapreduce-test-python/project1BD/reducer_time.py \
-input /project1BD/input/* -output /project1BD/output/
/usr/local/hadoop/bin/hdfs dfs -cat /project1BD/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1BD/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1BD/output/
../../stop.sh
