#!/bin/bash
echo "Formatting namenode"
$HADOOP_HOME/bin/hdfs namenode -format
echo "Start namenode"
$HADOOP_HOME/bin/hdfs --daemon start namenode
#echo "Start Resource Manage"
#$HADOOP_HOME/bin/yarn --daemon start resourcemanager
/bin/bash


