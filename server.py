import http.server
import socketserver

PORT = 8080

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Set response status code
            self.send_response(200)

            # Set response headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Set the response content for the root URL
            response_content = "Welcome to the server!"

            # Send the response content as bytes
            self.wfile.write(response_content.encode('utf-8'))

        elif self.path == '/ping':
            # Set response status code
            self.send_response(200)

            # Set response headers
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            # Set the response content for /ping
            response_content = "Pong"

            # Send the response content as bytes
            self.wfile.write(response_content.encode('utf-8'))

        else:
            # For any other URLs, send a 404 error response
            self.send_error(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response_content = "Page not found"
            self.wfile.write(response_content.encode('utf-8'))

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print("Server running at port", PORT)
    httpd.serve_forever()
