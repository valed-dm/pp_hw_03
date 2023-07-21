"""Scoring API main file"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import logging
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer

from handlers.method_handler import method_handler
from helpers.codes import BAD_REQUEST, ERRORS, OK


class MainHTTPHandler(BaseHTTPRequestHandler):
    """Handles api POST requests"""

    store = None

    @staticmethod
    def get_request_id(headers):
        """Provides request id"""

        return headers.get('HTTP_X_REQUEST_ID', uuid.uuid4().hex)

    def do_POST(self):
        """Process api POST request"""

        response, code = {}, OK
        context = {"request_id": self.get_request_id(self.headers)}
        request = None
        data_string = ""

        try:
            data_string = self.rfile.read(int(self.headers['Content-Length']))
            request = json.loads(data_string)
        except TimeoutError:
            code = BAD_REQUEST

        if code != BAD_REQUEST:
            logging.info("%s: %s %s", self.path, data_string, context["request_id"])

            response, code = method_handler(
                request=request,
                headers=self.headers,
                context=context
            )

        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        if code not in ERRORS:
            r = {"response": response, "code": code}
        else:
            r = {"error": response or ERRORS.get(code, "Unknown Error"), "code": code}

        context.update(r)
        logging.info(context)
        self.wfile.write(json.dumps(r).encode(encoding='utf-8'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="server port, log file setup")
    parser.add_argument("-p", "--port", action="store", type=int, default=8080)
    parser.add_argument("-l", "--log", action="store", default=None)
    args = parser.parse_args()
    logging.basicConfig(filename=args.log, level=logging.INFO,
                        format='[%(asctime)s] %(levelname).1s %(message)s', datefmt='%Y.%m.%d %H:%M:%S')
    server = HTTPServer(("localhost", args.port), MainHTTPHandler)
    logging.info("Starting server at %s", args.port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
