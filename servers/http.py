#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: @090h
"""
Links


https://github.com/selwin/python-user-agents

"""
import BaseHTTPServer
from time import asctime
from urlparse import urlparse
from user_agents import parse as ua_parse
import logging


class ReqHandler(BaseHTTPServer.BaseHTTPRequestHandler):


    def do_GET(self):
        parsed_path = urlparse(self.path)

        msg = """CLIENT VALUES:
              client_address=%s (%s)
              command=%s
              path=%s
              real path=%s
              query=%s
              request_version=%s
              """ % (self.client_address, self.address_string(), self.command, self.path,
               parsed_path.path,parsed_path.query, self.request_version,)

        msg += """SERVER VALUES:
              server_version=%s
              sys_version=%s
              protocol_version=%s
              """ % (self.server_version, self.sys_version,self.protocol_version,)


        msg += '\nHEADERS:\n'
        for name, value in sorted(self.headers.items()):
            msg += ('\t\t%s=%s\n' % (name, value.rstrip()))

        #OS guesing feature
        if self.headers.has_key('user-agent'):
            user_agent = ua_parse(self.headers['user-agent'])
            msg += """\nUser-Agent guessing:
                Browser: %s %s
                OS: %s %s
                Device: %s

                PC: %s
                Mobile: %s
                Tablet: %s

                Touch: %s
                Bot: %s\n""" % \
            (user_agent.browser.family, user_agent.browser.version_string,
             user_agent.os.family,user_agent.os.version_string,
             user_agent.device.family,

             user_agent.is_pc, user_agent.is_mobile,user_agent.is_tablet,

             user_agent.is_touch_capable,user_agent.is_bot,
            )

        self.send_response(200)
        self.end_headers()

        self.wfile.write(msg)
        #self.wfile.write('OK')
        #logging.info(message)
        return

    def do_POST(self):
        self.do_GET()

    def do_PUT(self):
        self.do_GET()

    def do_HEAD(self):
        self.do_GET()

if __name__ == '__main__':
    #TODO: Move it to args
    host = '0.0.0.0'
    port = 9090
    logging.basicConfig(filename='http_server.log',level=logging.DEBUG)

    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((host, port), ReqHandler)
    print asctime(), "Server Starts - http://%s:%s/" % (host, port)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print asctime(), "Server Stops - %s:%s" % (host, port)