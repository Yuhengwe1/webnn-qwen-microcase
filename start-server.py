import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler
# 强制手动添加映射
handler.extensions_map.update({
    '.js': 'application/javascript',
    '.mjs': 'application/javascript',
    '.jspi.mjs': 'application/javascript',
})

port = 8000
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()