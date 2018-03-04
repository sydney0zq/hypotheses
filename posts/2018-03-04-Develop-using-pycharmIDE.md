---
title: Develop python projects using PyCharm IDE
---

## What develop tools I used before?

I am a Linuxer for a very long time since I was a freshman in my college school. The simple but powerful tools help me to do creative things, whatever hard or easy of them.

Python, this popular and scientific language, plays an important role when I am in my sophomore year. My first python program is a scraper to pull down FF digest every day and show them in the terminal on my Lenovo laptop, which is thick and heavy. The code and design pattern looks really a bullshit, but I was still very excited cause it worked fine.

And then I read **vbird**'s book, [鳥哥的 Linux 私房菜](http://linux.vbird.org). This book contains everything, from basics to advances, feeding me the key to open Linux palace. I began to write code in `Vim`, to run scripts in terminal and compile source files by `gcc`. At that time, I was addicted to different Linux system installations, althought it looks really boring in current view.

But recently I am reproducing [GOTURN](https://github.com/davheld/GOTURN), a tracking model in Computer Vision(CV) domain. I have write all modules and think it supposes to work. But it failed, the estimated bounding box likes to shrink, which means my model learns nothing. My mentor rebukes me for the terrible results. I also have done a lot of vision checking, but in a way of writing them into image files and downloading them to check. This routine is inefficiency and not clean, for it needs modify origin source code.


## Why I decide to use PyCharm?

After days, the ECCV 2018 is coming to an end. But my results is not good, training such a model costs so much time. What's worse, the C++ version project is hard to deploy on GPU-Cluster system, a enormous computing center supporting `MXNET` best. I reconstruct my code by a principle of my senior's project, `SiamFC-Tensorflow`. I visualize everything in datalayer, and create class more reusable. Finally my project works, the model could output reasonable bounding box of the being tracked object. But the loss value still likes to shaking, maybe I should dig more to solve it. In the re-development of GOTURN, I could find PyCharm is amazing.

---

PyCharm's pros:

- Set conda virtual environment conveniently
- Easy to use visualization tools, such as OpenCV, matplotlib etc.
- Code offline
- Conveniently sync source code
- Could use a subset of database
- Auto-completion and error check

PyCharm's cons:

- Too much wave
- A little fat
- Not beautiful as terminal


Anyway, I love PyCharm, it helps indeed.


## Coda

My English is so poor when I am writing this blog. I should exercise more on purpose.


