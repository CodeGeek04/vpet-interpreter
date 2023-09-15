import interpreter
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/interpreter/parse':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            voice_command = json.loads(post_data)
            try:
                interpreter.parse(voice_command)
                self.send_response(200)
            except Exception as e:
                print(f'Error parsing voice command: {e}')
                self.send_response(500)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def parseVoiceCommand(voiceCommand: str):
    # Pass the voice command to the interpreter
    try:
        interpreter.parse(voiceCommand)
    except Exception as e:
        print(f'Error parsing voice command: {e}')

if __name__ == '__main__':
    run()
