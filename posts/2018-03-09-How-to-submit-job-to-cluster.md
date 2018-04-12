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

Here I want to emphasis one thing: `submit.sh` is executed by me on host machine while `job.sh` is executed by `gpuwork` on remote machine. `HADOOP_OUT` is a directory that when your job finished on remote machine, the `localoutput` directory contents will be moved into this `HADOOP_OUT`.


Before you submit your code, you should RUN it on your local machine to make sure it works well, you also should check your HDFS API.


### Advanced

After a long time usage of cluster, I began to know the internal mechanism behind the user interface. And in a segmentation coorperated with HuangZilong senior, I developed a more robust and flexible script to submit our jobs.

You could firstly zip your miniconda3 into a `tar.gz` file, and then upload it to HDFS, after that when your project runs on remote machine, you could fetch it and then unzip it. Of course you could handle more giga files like so. The goodness of this operation is that you could save a lot of time in submit process and you would never need to re-zip miniconda3.

Here is our `job.sh`. Notice `JAVA_TOOL_OPTIONS` variable, if you enable it, you couldn't use `hadoop fs -get` commands, which confuses me for a long time.


<pre> <code>
#!/bin/bash
cd ${TMPDIR}
# add PATH and LD_LIBRARY_PATH
#export LD_LIBRARY_PATH="lib:${LD_LIBRARY_PATH}"

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
#export JAVA_TOOL_OPTIONS="-Xms2000m -Xmx10000m"        # For JNI MXNET

HADOOP_BIN_ROOT="hdfs://hobot-bigdata/user/qiang.zhou/bin"
hadoop fs -get $HADOOP_BIN_ROOT/miniconda3.tar.gz .
hadoop fs -get $HADOOP_BIN_ROOT/vgg16-397923af.pth ./$PROJ_BRANCH/models
hadoop fs -get $HADOOP_BIN_ROOT/cache ./$PROJ_BRANCH
#ls . -R

tar -xzf miniconda3.tar.gz
PYTHON_EXE=./miniconda3/bin/python
SNAPSHOT_DIR=snapshots_coco
EVALRES_DIR=evaluation_davis17

#variable ${LOCAL_OUTPUT} dir can save data of you job, after exec it will be upload to hadoop_out path
$PYTHON_EXE $PROJ_BRANCH/osmn_coco_pretrain.py --model_save_path local_run_output/$SNAPSHOT_DIR \
--max_iters $MAX_ITER \
--steps $STEPS \
--learning_rate $LR \
--batch_size $BS
#--gpu_id $GPUs \

$PYTHON_EXE $PROJ_BRANCH/osmn_train_eval.py     --whole_model_path local_run_output/$SNAPSHOT_DIR/osmn_${MAX_ITER}.pth \
--result_path local_run_output/$EVALRES_DIR \
--data_version 2017 \
--save_score
#--gpu_id $GPUs \
$PYTHON_EXE $PROJ_BRANCH/davis_eval.py $PROJ_BRANCH/cache/DAVIS local_run_output/evaluation_davis17 2017 val
</code></pre>

This script definately is not suitable for your projects, please read it before you deploy.

And our `submit.sh`. `job.sh` uses some variables exported by our `submit.sh`.


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

export GPUs=1
export BS=8
export LR='1e-5 1e-6'
export STEPS='200000 300000'
export MAX_ITER=300000


PROJ_DIR="SEGENV"
export PROJ_BRANCH="$1"
[ "$1" == "" ] && echo -e "Usage:\n\t$0 PROJ_BRANCH" && exit
#export JOB_NAME="OSMN~Loss_No_Average~-BS_${BS}_LR_${LR// /-}_Steps_${STEPS// /-}"
export JOB_NAME="$1-BS_${BS}_LR_${LR//[ -]/_}_Steps_${STEPS// /_}"

echo "***NOTICE the project branch you submit is $1"

host=`hostname`
ids=`date +%Y%m%d%H%M%S`
job_id="${JOB_NAME}_${ids}"
echo "Starting Job Submit. Jobid == ${job_id}....."

HADOOP_OUT=/user/`whoami`/seg/${job_id}
#hadoop fs -mkdir -p ${HADOOP_OUT}
#hadoop fs -chmod 777 ${HADOOP_OUT}
#you can save working data to localoutput dir, after exec, this dir will be upload to $HADOOP_OUT
time qsub_i \
-N ${job_id} \
--hdfs $HDFS  --ugi `whoami`,regular-engineer \
--hout $HADOOP_OUT \
--files $PROJ_DIR \
--localoutput local_run_output \
--pods ${GPUs} \
-l walltime=256:30:00  \
./$PROJ_DIR/job.sh

echo "Your sys job_name : ${job_id}"
</code></pre>

These advanced scripts help me a lot and really speed up my projects.


### Submit

Just use `bash submit.sh`, this script will create a `.tar.gz` zipped file to run on cluster machine. And then it will create necessary directories and dump all models to your specified directory in the above scripts.



