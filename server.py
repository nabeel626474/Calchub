import http.server
import socketserver
import os

PORT = 5000
HOST = "0.0.0.0"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle clean URLs and extensionless requests
        path = self.translate_path(self.path)
        
        # If the path is a directory but a .html file with the same name exists, serve the file
        # This fixes the "tools/" vs "tools.html" conflict
        if os.path.isdir(path) and os.path.exists(path.rstrip('/') + ".html"):
            self.path = self.path.rstrip('/') + ".html"
        elif not os.path.exists(path) and not path.endswith('/'):
            if os.path.exists(path + ".html"):
                self.path += ".html"
        
        return super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

# Allow port reuse to avoid "Address already in use" errors
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer((HOST, PORT), CustomHandler) as httpd:
    print(f"Serving on http://{HOST}:{PORT}")
    httpd.serve_forever()
