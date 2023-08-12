import http.server


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        return "text/plain"


if __name__ == "__main__":
    http.server.test(HandlerClass=CustomHTTPRequestHandler)

