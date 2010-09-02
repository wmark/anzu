#!/usr/bin/env python

from anzu.testing import AsyncHTTPTestCase, LogTrapTestCase
from anzu.web import Application, RequestHandler
import os
import pycurl
import re
import unittest
import urllib

class HelloWorldRequestHandler(RequestHandler):
    def get(self):
        self.finish("Hello world")

class SSLTest(AsyncHTTPTestCase, LogTrapTestCase):
    def get_app(self):
        return Application([('/', HelloWorldRequestHandler)])

    def get_httpserver_options(self):
        # Testing keys were generated with:
        # openssl req -new -keyout anzu/test/test.key -out anzu/test/test.crt -nodes -days 3650 -x509
        test_dir = os.path.dirname(__file__)
        return dict(ssl_options=dict(
                certfile=os.path.join(test_dir, 'test.crt'),
                keyfile=os.path.join(test_dir, 'test.key')))

    def test_ssl(self):
        def disable_cert_check(curl):
            # Our certificate was not signed by a CA, so don't check it
            curl.setopt(pycurl.SSL_VERIFYPEER, 0)
        self.http_client.fetch(self.get_url('/').replace('http', 'https'),
                               self.stop,
                               prepare_curl_callback=disable_cert_check)
        response = self.wait()
        self.assertEqual(response.body, "Hello world")
