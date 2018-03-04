---
title: Blog website deployment record
---


## Why I want to write personal blog?


Actually I don't really know why I need a blog to record my ideas, exploration, and struggle learning way. That's just someday when I was visiting other's blog, the beautiful style attracted me really a lot, and recently there are remarkable changes in my workflow, all of these drives me to write them down.

I have tried to write blogs formerly, for several times. But I finally cannot insist cause the publication tools are not easy to use, i.e. Hexo or Haskell. This time, I use the CSS and html-template files from that beautiful repostority, and then I code a `Render` class in python to generate all my html files from markdown ones directly, no more depencies needed. This work costed me about 12 hours, and brings me much enjoyment. And then I bought a domain `hypotheses.cc` from namesilo(About 8.99 dollars, 56.7 Yuan in RMB), get all stuffs done and then push it on Github. The final visual effect looks very close to the original blog, and I really like it.



## How to deploy?


**Aim: Make sure your website works on your local machine**

- Firstly, we need to modify `config.py` to set necessary paths, it will be used in `build.py`.
- Then, write your markdown posts, note the format is strict. You should follow:
	- All posts md file names are beginning with `Year-Month-Day-Your-Post-Name.md`
	- All posts md files start with `---\ntitle: Your post title\n---\n`
	- Make sure all your meta md files exist and are coincident with the code logic
- Run `python3 build.py` to generate all your html static files
- Run `python3 -m http.server 8001` and visit `http://localhost:8001` to check your website


**Aim: Deploy to github**

- Firstly, you need a custom domain. After you get it from domain service provider, you should set it a `AAAA` record: i.e. `AAAA blog.hypotheses.cc sydney0.github.io`
- Secondly, you should add one `CNAME` in your reposority which contains the top domain name i.e. `hypotheses.cc`
- Thirdly, go to your reposority setting, change the domain setting to `blog.hypotheses.cc` and wait about 5 minutes
- Note, when you use the native github domain, if you set your css path in `index.html` as `'/css/default.css'`, it will induce one error that github could not find the file on `sydney0zq.github.io/css/default.css`, but the actual path is `sydney0zq.github.io/hypotheses/css/default.css`, but if you modify your template to adapt this troublesome thing, you will get stuck in chaos. So the best way to solve it is just using your custom domain instead of the default one.


## Coda


In this blog, I add my wishlist and resume. Maybe I could add more tabs to record my life. After one month in Beijing, I realize it is so hard to do research but I still love it as long as I am not being pushed. And I would like to search for beautiful things as my primary goal.


Best wishes.





# Appendix


**My 2018 Plan**

1. 在12点前睡觉，早上8点之前起床

2. 每周至少三次锻炼

3. 读最起码10本经典或者有名的书，做完笔记

    a. 给佳西亚的一封信

    b. 深度学习花书

    c. 郎小平的经济书籍

    d. 2部小说

    e. 失控

    ...

4. 听完吴军的谷歌方法论，做完笔记和反思

5. 将存款合理规划，按照比例分配

6. 积极找女朋友

7. 保护眼睛

---

方法：

1. 提升效率和保持习惯，将手机放在其他地方

2. 设定闹钟，可以先回去然后在小区/学校跑圈

3. 找到空余时间去看书，避免时间浪费，找到重心

4. 应该系统性的思考和总结

5. 设定规则去投资，不要乱投，也不能投太多

6. 拓展朋友圈和抓住机会

7. 每隔1h出去休息眼睛，硬性要求

---
行动：

Just do them, not delay.

