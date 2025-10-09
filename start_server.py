#!/usr/bin/env python3
"""
Simple HTTP Server for hosting HTML project offline
Works on any PC with Python installed
"""

import http.server
import socketserver
import webbrowser
import os
import sys

# Configuration
PORT = 8000
HOST = 'localhost'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve files with proper MIME types"""
    
    def end_headers(self):
        # Add CORS headers to allow local file access
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

def start_server():
    """Start the HTTP server"""
    
    # Change to the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if index.html exists
    if not os.path.exists('index.html'):
        print("❌ Error: index.html not found in the current directory!")
        print(f"Current directory: {script_dir}")
        input("Press Enter to exit...")
        return
    
    try:
        # Create server
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            print("🚀 Starting offline server...")
            print(f"📁 Serving files from: {script_dir}")
            print(f"🌐 Server running at: http://{HOST}:{PORT}")
            print(f"📄 Your project: http://{HOST}:{PORT}/index.html")
            print("\n" + "="*50)
            print("✅ Server is running! Your project is now accessible offline.")
            print("🔗 Open this link in any browser: http://localhost:8000/index.html")
            print("="*50)
            print("\n📝 Instructions:")
            print("• Keep this window open while using the project")
            print("• Copy this entire folder to any PC to run offline")
            print("• Works on Windows, Mac, and Linux")
            print("• Press Ctrl+C to stop the server")
            print("\n🎯 Opening your project in the default browser...")
            
            # Open browser automatically
            try:
                webbrowser.open(f'http://{HOST}:{PORT}/index.html')
            except Exception as e:
                print(f"⚠️  Could not open browser automatically: {e}")
                print(f"🔗 Please manually open: http://{HOST}:{PORT}/index.html")
            
            print("\n⏳ Server is running. Press Ctrl+C to stop...")
            
            # Start serving
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"❌ Port {PORT} is already in use!")
            print("💡 Try closing other applications or restart your computer.")
        else:
            print(f"❌ Error starting server: {e}")
        input("Press Enter to exit...")
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user.")
        print("👋 Thanks for using the offline server!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    print("🌐 HTML Project Offline Server")
    print("=" * 30)
    start_server()
