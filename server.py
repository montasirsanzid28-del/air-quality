#!/usr/bin/env python3
"""
Simple HTTP server for the Air Quality Index App
Run this file to start the server, then open http://localhost:8000 in your browser
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# Change to the app directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow API calls
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

print(f"Starting Air Quality App server...")
print(f"Go to: http://localhost:{PORT}")
print(f"Press Ctrl+C to stop the server")

# Open browser automatically
webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
