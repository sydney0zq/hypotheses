---
title: Long time log about  strange bugs in projects
---


## Python3

- You couldn't use `open` function to write content to a file in a class's `__del__` function, it will result in `open NotFound`





## Vision

- `io.imread` result is **RGB(MxNx3)** while `cv2.imread` result is **BGR(MxNx3)**. The bridge API is `im=im[..., ::-1]`
- `Image.open('.jpg').size` is **wxh** while `cv2.imread.shape` is **hxw**
- If save a **mean-sub** image using `cv2.imwrite`, you will lose the pixels whose value is negative, they will be black. But if you view them online after you subtract mean, you will get a colorful image but not right. [FloatView](https://ws4.sinaimg.cn/large/006tNc79ly1fpsmbe3zjzj306b06bdfq.jpg) vs [Uint8View](https://ws2.sinaimg.cn/large/006tNc79gy1fpsmbrasalj306b06b74q.jpg)
- When try to tranpose a CHW to a HWC tensor, you should never use `np.reshape`, you should use `np.transpose((1, 2, 0))` instead. Otherwise you will get a 9x9 cell weird image.
- cudaCheckError() failed : invalid device function, it is because when you compile the .cu file, your `compute_arch` is not supporting all functions. Check your `CUDA_ARCH` as a clue, maybe you need add more arch into this variable.



## Pure bugs

Q1: `TypeError: int() argument must be a string, a bytes-like object or a number, not 'Image'` when using cropimage lambda function, `cropimage = lambda x, bbox: np.array(Image.fromarray(x.astype(np.uint8)).crop(bbox), x.dtype)`
A1: 这是由于bbox太小，导致扣出来一个空的区域，这样的话就会导致在转换的时候出现错误
