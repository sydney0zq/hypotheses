---
title: How to debug a model from scratch
---

## The problem description

In my last several blogs, I said about I build a tracker myself from scratch, based on GOTURN. GOTURN works fine, except a little concussion. I replace the FC regressor to FCN regressor, and use YOLO loss to detect the being tracked object. However, the trainer built by myself doesn't work well. Its IOU firstly suspends on 0.50 and cannot to raise. So here I log my debug experience. Bily helps me a lot who clears my thoughts.


## Procedure

### Check inputs

Pheno: My training batch average iou always concusses, and even down to 0 sometimes. I check my three inputs, `batch_x1, batch_x2, batch_y`, in `train.py`. At last I found `batch_y` is wrong, I fullfill the `batch_y` only from one fixed sample. So next time, I should check it carefully.

After repairing this mistake, I still find my model is hard to converge, cause the IOU always remain on 0.5 or lower. After a long time struggle, I ask Bily for help.

<br>
> Note: PyTorch backward function works very well. You could compute `forward(inputs, targets)` and check `inputs.grad` value to ensure your implementation.

### Training stucks on specified iteration

In my training stage, I found sometimes my model will stuck on some specified iteration but the it still occupy CPU resource. Under this situtation, the best way to solve this issue is that comment module by module, line by line. But note you should be sure you could reproduce the same issue precisely.

### Firstly, overfit on one sample

First of everything all, you should overfit your model on one single model to determine your **learning rate**, **size average bool**, **epoch number**. You must overfit your model on this single example.

### Secondly, overfit on one batch

And then you get these important hyper-parameters settled, you could overfit on on single batch. And re-adapt **size average bool** and **learning rate**.

### Finally, train on the whole dataset


