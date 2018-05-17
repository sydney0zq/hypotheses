---
title: Long term machine learning basis
---

## Recall and Precision

![](http://okye062gb.bkt.clouddn.com/20180417170149_CW6UU9_Screenshot.jpeg)

## 1x1 convolution for segmentation network

Classify for each pixel.

## FPN architecture

![](http://okye062gb.bkt.clouddn.com/20180517104713_diskWP_Screenshot.jpeg)

首先我们有一张图片，左边是一个普通的 ResNet 网络，其中的 stride 表示相对于原图分辨率降低了多少，例如 stride=2 代表相对于原图降低了2倍，stride=4相对于原图降低了 4 倍。然后右侧是从每一个 ResNet Block 的 ElementWise 加之后再经过 ReLU，进行 1x1 卷积得到的 feature map，即 M2～M5。之后我们就将M5的分辨率提升一倍加入到 M4 的特征中，依次类推，与此同时，我们利用 3x3 的卷积（因为特征相加之后会有噪声）去得到 P5～P2。这就是 FPN 的基本架构。











