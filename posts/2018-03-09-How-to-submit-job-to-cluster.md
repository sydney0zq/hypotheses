---
title: How to submit job to cluster?
---

## Understand job and HDFS

A job is a project to run on GPU Cluster. And HDFS is a distrubtion filesystem which is very large but slow.


## Procedure

### Prepare your code and data

Firstly you should make sure your code works fine on your local machine. And if everything goes well, we could get started.

The first step is create a virtual environment, you could use `miniconda` or `virtualenv`, here I use `miniconda3`, and my working directory is `~/JOBENV` while the virtual environment directory is `~/JOBENV/SOT`. After we install miniconda3 in virtual directory, we install necessary packages refered by our project.

And then you could copy the following `job.sh` and `submit.sh` into your job environment.


<pre> <code>
#!/bin/bash

cd ${TMPDIR}
# add PATH and LD_LIBRARY_PATH
#export LD_LIBRARY_PATH="lib:${LD_LIBRARY_PATH}"
ls ./

uname -a
#date
#env
date

CWD=`pwd`
#SAVE_PATH="hdfs://hobot-bigdata/user/cheng.wang/run_output/"
export PYTHONPATH=${CWD}:$PYTHONPATH
echo $CWD
echo $TMPDIR
#set this to enable reading from hdfs 
export CLASSPATH=$HADOOP_PREFIX/lib/classpath_hdfs.jar
export JAVA_TOOL_OPTIONS="-Xms2000m -Xmx10000m"

#variable ${LOCAL_OUTPUT} dir can save data of you job, after exec it will be upload to hadoop_out path 
./SOT/bin/python PyTorch-GOTURN/train.py
#./SOT/bin/python open-reid/examples/triplet_loss.py -d market1501 -a resnet50 -b 256 --num-instances 16 --data-dir open-reid/data --logs-dir local_run_output/logs/market1501-resnet50-s00/ --lr 0.0003 --margin 0.5 -j 4 --epochs 160 --combine-trainval --start_save 100 
</code> </pre>


Here is `submit.sh`.

<pre> <code>
#!/bin/bash
HDFS=hdfs://hobot-bigdata/
export HADOOP_PREFIX='/usr/'
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HADOOP_PREFIX/lib/native
export HADOOP_HOME=/usr/local/hadoop-2.7.2
export PATH=${HADOOP_HOME}/bin/:${PATH}
export HADOOP_PREFIX=${HADOOP_HOME}
export JAVA_HOME=/usr/lib/jvm/java-1.7.0
export CLASSPATH=$($HADOOP_HOME/bin/hadoop classpath --glob)

JOB_NAME='GOTURN-ALEXNET-ORI-CLUSTER-TEST'

PROJ_DIR='JOBENV'

host=`hostname`
ids=`date +%Y%m%d%H%M%S`
job_id="${JOB_NAME}_${ids}"
echo "Starting Job Submit. Jobid == ${job_id}....."

HADOOP_OUT=/user/qiang.zhou/idea/${job_id}
#you can save working data to localoutput dir, after exec, this dir will be upload to $HADOOP_OUT
qsub_i \
    -N ${job_id} \
    --hdfs $HDFS  --ugi `whoami`,regular-engineer \
    --hout $HADOOP_OUT \
    --files $PROJ_DIR \
    --localoutput experiments \
    --pods 4 \
    -l walltime=256:30:00  \
    ./$PROJ_DIR/job.sh

echo "Your sys job_name : ${job_id}
</code> </pre>


The final file tree should be like this:

<pre><code>
~
 +-JOBENV
 + +-SOT
 + + +-bin
 + + +-include
 + + +-...
 + + 
 + +-YourProjectDir
 + +-job.sh
 +-submit.sh
</code></pre>


Before you submit your code, you should RUN it on your local machine to make sure it works well, you also should check your HDFS API.


### Submit

Just use `bash submit.sh`, this script will create a `.tar.gz` zipped file to run on cluster machine. And then it will create necessary directories and dump all models to your specified directory in the above scripts.



