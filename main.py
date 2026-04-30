import http.server
import socketserver
import socket

def get_local_ip():
    # Пытаемся определить локальный IP адрес устройства
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Адрес не обязательно должен быть доступен, это нужно для определения интерфейса
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

PORT = 8000
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("0.0.0.0", PORT), handler) as httpd:
    local_ip = get_local_ip()
    print(f"✅ Сервер запущен!")
    print(f"🔗 Локальная ссылка: http://localhost:{PORT}")
    print(f"🌐 Ссылка для других устройств в сети: http://{local_ip}:{PORT}")
    print("\nНажмите Ctrl+C для остановки.")
    httpd.serve_forever()
