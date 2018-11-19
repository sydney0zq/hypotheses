#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 2016-12-25 root <root@VMdebian>

import BaseHTTPServer
import pickle

randpath = '/data/splited/randcopy.log'
with open(randpath, "r") as f:
    li = pickle.load(f)
    f.close()

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        page = self.create_page()
        self.send_page(page)

    def create_page(self):
        lucknum = li.pop()
        filename = "./q" + "%04d" % lucknum
        with open(randpath, 'w') as randlog:
            pickle.dump(li, randlog)
            randlog.close()
        with open(filename, "r") as f:
            page = f.read()
            f.close()
            return page
    def send_page(self, page):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)

if __name__ == "__main__":
    serverAddress = ('', 5555)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
