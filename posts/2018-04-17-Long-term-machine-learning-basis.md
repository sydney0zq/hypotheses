---
title: Long term machine learning basis
---

## Theory basis

- PCA is a linear transformation that can be easily learnt in one layer of the network

<hr>

## Recall and Precision

![](http://okye062gb.bkt.clouddn.com/20180417170149_CW6UU9_Screenshot.jpeg)

<hr>

## 1x1 convolution for segmentation network

Classify for each pixel.

<hr>

## FPN architecture

<img width="70%" src="http://okye062gb.bkt.clouddn.com/20180517104713_diskWP_Screenshot.jpeg" />

首先我们有一张图片，左边是一个普通的 ResNet 网络，其中的 stride 表示相对于原图分辨率降低了多少，例如 stride=2 代表相对于原图降低了2倍，stride=4相对于原图降低了 4 倍。然后右侧是从每一个 ResNet Block 的 ElementWise 加之后再经过 ReLU，进行 1x1 卷积得到的 feature map，即 M2～M5(Top-Down lateral modules)。之后我们就将M5的分辨率提升一倍加入到 M4 的特征中，依次类推，与此同时，我们利用 3x3 的卷积（因为特征相加之后会有噪声）去得到 P5～P2。这就是 FPN 的基本架构。
[__代码__](https://github.com/roytseng-tw/Detectron.pytorch/blob/master/lib/modeling/FPN.py)

<hr>

## Learning Rate warming up

- **Constant warmup**: In constant warm up , you train the model with a small learning rate for few epochs(usually 5) and then increase the learning rate to “k times learning rate” .However this approach may cause a spike in the training error when the learning rate is changed.

- **Gradual warmup**: As the name suggests , you start with a small learning rate and then gradually increase it by a constant for each epoch till it reaches “k times learning rate”. This approach helps the model to perform better with huge batch sizee, which is in par with the training error of the model trained with smaller batches.

<hr>











