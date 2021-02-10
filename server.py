import http.server
import socketserver


class RequestHandler(http.server.SimpleHTTPRequestHandler):

    def get(self):

        if self.path == '/':
            self.path = "index.html"

        return http.server.SimpleHTTPRequestHandler.do_GET(self)


handler_object = RequestHandler
PORT = 8000

server = socketserver.TCPServer(("", PORT), handler_object)
server.serve_forever()
