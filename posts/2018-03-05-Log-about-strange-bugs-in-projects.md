---
title: Long time log about  strange bugs in projects
---


## Python3

- You couldn't use `open` function to write content to a file in a class's `__del__` function, it will result in `open NotFound`





## Vision

- `io.imread` result is **RGB(MxNx3)** while `cv2.imread` result is **BGR(MxNx3)**. The bridge API is `im=im[..., ::-1]`
- `Image.open('.jpg').size` is **wxh** while `cv2.imread.shape` is **hxw**
- If save a **mean-sub** image using `cv2.imwrite`, you will lose the pixels whose value is negative, they will be black. But if you view them online after you subtract mean, you will get a colorful image but not right. [FloatView](https://ws4.sinaimg.cn/large/006tNc79ly1fpsmbe3zjzj306b06bdfq.jpg) vs [Uint8View](https://ws2.sinaimg.cn/large/006tNc79gy1fpsmbrasalj306b06b74q.jpg)
