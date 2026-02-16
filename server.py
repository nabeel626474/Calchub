import http.server
import socketserver
import os

PORT = 5000
HOST = "0.0.0.0"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle the root path
        if self.path == '/':
            self.path = '/index.html'
        
        # Priority 1: Handle /tools or /tools/ by serving tools.html
        # This resolves the conflict with the tools/ directory
        if self.path.rstrip('/') == '/tools':
            self.path = '/tools.html'
            return super().do_GET()

        # Priority 2: Try appending .html to extensionless requests
        path_on_disk = self.translate_path(self.path)
        if not os.path.exists(path_on_disk) and not os.path.splitext(self.path)[1]:
            if os.path.exists(path_on_disk + ".html"):
                self.path += ".html"

        return super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer((HOST, PORT), CustomHandler) as httpd:
    print(f"Serving on http://{HOST}:{PORT}")
    httpd.serve_forever()
