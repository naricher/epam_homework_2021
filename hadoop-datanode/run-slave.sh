#!/bin/bash
echo "Start datanode"
$HADOOP_HOME/bin/hdfs --daemon start datanode
echo "Start Node Manager"
#$HADOOP_HOME/bin/yarn --daemon start nodemanager
/bin/bash
