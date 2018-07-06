# -*- coding: utf-8 -*-
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright (C) 2017-2018 Huawei Inc
#
# Author heyu 00448261

# -*- coding: utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import time

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def say_info(self, words):

    def say_error(self,words):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Localtime: {0}\r\n".format(time.asctime()))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        try:
            data = json.loads(self.rfile.read(int(self.headers['content-length'])))
            rep={"result":"success", "data":data}
            print("--data: {0}".format(data))


        except Exception as e:
            rep={"result":"error", "data":"{0}".format(e)}

        rep.update({"time":time.asctime()})
        self.wfile.write(json.dumps(rep))
        print("--reply:{0}".format(rep))

    def handle(self, data,**kwargs):
        """

        :param data:
        :param kwargs:
        :return:
        """
        if hasattr(self, "handle_func"):
            self.say_info("entering handle function")
            self.handle_func(data,**kwargs)
        else:
            self.say_info("no handle function, abandon data")

    @classmethod
    def register_handle_func(cls, func):
        if not func:
            return
        if hasattr(cls, 'handle_func'):
            print "[*] already has a handle_func, replaced"
            setattr(cls, ' handle_func', func)
        else:
            setattr(cls, 'handle_func', func)
            print "[*] handle_func registered"


class CustomHTTPServer(HTTPServer):
    def __init__(self, host="0.0.0.", port=9876, register_func=None):
        CustomHTTPRequestHandler.register_handle_func(register_func)
        HTTPServer.__init__(self, (host, port), CustomHTTPRequestHandler)

def main():
    server = CustomHTTPServer('127.0.0.1', 8000)
    server.serve_forever()


if __name__ == '__main__':
    main()
