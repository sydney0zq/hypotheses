---
title: Long time log about  strange bugs in projects
---


## Python3

- You couldn't use `open` function to write content to a file in a class's `__del__` function, it will result in `open NotFound`

Q1: 登陆SSH之后，然后获取一个新的Shell，在PATH和PYTHONPATH对于python的系统路径没有影响的时候，但是在python的交互模式中的sys.path却出现了以前工程中的路径，检查系统变量等，都没有此路径。
<br> A1: python获取额外的sys.path源码见~/anaconda3/lib/python3.6/site.py，其中就有加入site-packages包的代码。由于在编译maskrcnn-benchmark的时候编译了RoIAlign，因此编译的时候它自动的加入到~/anaconda3/lib/python3.6/site-packages/roialignxxxx以及~/anaconda3/lib/python3.6/easy_install.pth中，最后通过删除了easy_install.pth中的内容解决的。

<hr>




## Vision

- `io.imread` result is **RGB(MxNx3)** while `cv2.imread` result is **BGR(MxNx3)**. The bridge API is `im=im[..., ::-1]`
- `Image.open('.jpg').size` is **wxh** while `cv2.imread.shape` is **hxw**
- If save a **mean-sub** image using `cv2.imwrite`, you will lose the pixels whose value is negative, they will be black. But if you view them online after you subtract mean, you will get a colorful image but not right. [FloatView](https://ws4.sinaimg.cn/large/006tNc79ly1fpsmbe3zjzj306b06bdfq.jpg) vs [Uint8View](https://ws2.sinaimg.cn/large/006tNc79gy1fpsmbrasalj306b06b74q.jpg)
- When try to tranpose a CHW to a HWC tensor, you should never use `np.reshape`, you should use `np.transpose((1, 2, 0))` instead. Otherwise you will get a 9x9 cell weird image.
- cudaCheckError() failed : invalid device function, it is because when you compile the .cu file, your `compute_arch` is not supporting all functions. Check your `CUDA_ARCH` as a clue, maybe you need add more arch into this variable.
- maskrcnnbenchmark框架在集群上跑不通可能是因为`SOLVER.IMS_PER_BATCH`没有被作为一个参数传入，以及tee的使用也会导致GPU卡死



## Pure bugs

Q1: "TypeError: int() argument must be a string, a bytes-like object or a number, not 'Image'" when using cropimage lambda function:<br> `cropimage = lambda x, bbox: np.array(Image.fromarray(x.astype(np.uint8)).crop(bbox), x.dtype)`
<br>A1: 这是由于bbox太小，导致扣出来一个空的区域，这样的话就会导致在转换的时候出现错误

<hr>

Q2: "__CudaPopCallFunctionError" 并且有提示gcc版本过低的信息(ABI 不兼容)
<br>A2: 问题出在版本不匹配上，根据github中：https://github.com/facebookresearch/maskrcnn-benchmark/issues/367 中的提示，应该保证NVCC的版本和CUDATOOLKIT的版本完全一致，比如9.2对9.2，9.2对9.0就会出现错误。检查CUDATOOLKIT方法就是：conda list | grep cuda。此外ABI不兼容的时候，要自己编译GCC，使用40个线程大概只需要20分钟到30分钟，编译链接：http://www.xieqiang.site/2017/07/31/install-gcc-5.4-without-root/。

<hr>

Q3: 在tmux中使用opencv显示图片(imshow)的时候显示": cannot connect to X server :28.0"，但是不使用tmux就可以显示。
<br>A3: 这是因为tmux无法模拟，具体可以看：[tmux-opencv-imshow-question](https://stackoverflow.com/questions/39840184/python-code-crashes-with-cannot-connect-to-x-server-when-detaching-sshtmux-se)


