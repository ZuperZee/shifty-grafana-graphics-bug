from http.server import HTTPServer, SimpleHTTPRequestHandler


class CORSHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        return super().end_headers()


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, CORSHTTPRequestHandler)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
