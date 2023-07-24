# Simple Python HTTP Server

This is a basic Python HTTP server that listens on port 8080 and serves different responses based on the requested URLs.

## Description

The server responds to the following URLs:
- `/`: The root URL that returns a 200 OK status and displays "Welcome to the server!" in an HTML format.
- `/ping`: Returns a 200 OK status and displays "Pong" as plain text.
- Any other URL: Responds with a 404 Not Found error and displays "Page not found" in plain text.

## How to Run

1. Make sure you have Python installed on your system.
2. Save the `server.py` file to your desired directory.
3. Open a terminal or command prompt and navigate to the directory where `server.py` is saved.
4. Run the server with the following command:
5. The server will start running, and you can access it by opening your web browser and navigating to `http://localhost:8080`.
6. To test the `/ping` URL, access `http://localhost:8080/ping`.
