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

