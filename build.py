#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 qiang.zhou <qiang.zhou@yz-gpu029.hogpu.cc>
# Created on 01 14:54

import markdown
import re
import os.path as osp
import glob
from config import RENDER_CONFIG, TEMPLATE_CONFIG


def read(fn):
    with open(fn, "r") as f:
        return f.read()


get_date = lambda x: "".join([ y+"-" for y in x.split('/')[-1].split('-')[:3]])[:-1]
add_break = lambda x: x.replace('\n', '\n<br>')


class Render:
    def __init__(self):
        self.metamds = RENDER_CONFIG['metamds']
        self.postdir = RENDER_CONFIG['postdir']
        self.postlist = sorted(glob.glob(osp.join(self.postdir, "*.md")), reverse=True)
        self.template_meta = read(TEMPLATE_CONFIG['meta'])
        self.template_index = read(TEMPLATE_CONFIG['index'])
        self.template_post = read(TEMPLATE_CONFIG['post'])
        self.template_postitem = read(TEMPLATE_CONFIG['post-item'])
        self.indexfn = RENDER_CONFIG['indexfn']

    def rend_post(self):
        """Default html template has four placeholder to replace
            - $htmltitle$
            - $title$
            - $body$
            - $date$
        """
        posthtmllist = [ x[:-3]+".html" for x in self.postlist ]
        template_post_ = self.template_post
        for i, post in enumerate(self.postlist):
            template_post = template_post_
            with open(post, "r") as f:
                _, title, _ = f.readline(), f.readline().replace('title: ', '').rstrip('\n'), f.readline()
                postbody = markdown.markdown(f.read())
            repdict = {'$title$': title, '$htmltitle$': title,
                       '$body$': postbody, '$date$': get_date(post)}
            for key in repdict:
                template_post = template_post.replace(key, repdict[key])
            with open(posthtmllist[i], "w") as f:
                f.write(template_post)

    def rend_index(self):
        post_itembody = ""
        template_index = self.template_index
        for post in self.postlist:
            template_postitem_ = self.template_postitem
            with open(post, "r") as f:
                _, title = f.readline(), f.readline().replace('title: ', '').rstrip('\n')
            repdict = {'$url$': "/{}html".format(post[:-2]), '$title$': title, '$date$': get_date(post)}
            #print (repdict)
            for key in repdict:
                template_postitem_ = template_postitem_.replace(key, repdict[key])
            post_itembody += template_postitem_
        template_index = template_index.replace('$body$', post_itembody)
        with open(self.indexfn, "w") as f:
            f.write(template_index)

    def rend_meta(self):
        metahtmllist = [x[:-3] + ".html" for x in self.metamds]
        template_meta_ = self.template_meta
        for i, meta in enumerate(self.metamds):
            template_meta = template_meta_
            with open(meta, "r") as f:
                _, title, _ = f.readline(), f.readline().replace('title: ', '').rstrip('\n'), f.readline()
                metabody = markdown.markdown(f.read())
            repdict = {'$title$': title, '$body$': metabody}
            for key in repdict:
                template_meta = template_meta.replace(key, repdict[key])
            with open(metahtmllist[i], "w") as f:
                f.write(template_meta)

    def rend_all(self):
        self.rend_meta()
        self.rend_post()
        self.rend_index()


if __name__ == "__main__":
    r = Render()
    r.rend_all()







