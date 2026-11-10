import json
import os
import socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        resposta = {
            "mensagem": "Eu amo fazer esse lab dockerrrr.",
            "instancia": os.getenv("APP_NAME", "app-local"),
            "container": socket.gethostname(),
        }
        corpo = json.dumps(resposta, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()