---
title: Long time log about  strange bugs in projects
---


## Python3

- You couldn't use `open` function to write content to a file in a class's `__del__` function, it will result in `open NotFound`





## Vision

- `io.imread` result is **RGB(MxNx3)** while `cv2.imread` result is **BGR(MxNx3)**. The bridge API is `im=im[..., ::-1]`
- `Image.open('.jpg').size` is **wxh** while `cv2.imread.shape` is **hxw**
