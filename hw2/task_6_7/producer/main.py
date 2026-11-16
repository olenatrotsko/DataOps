
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from threading import Thread
import time

SHARED_FILE = Path("/shared/messages.txt")


def write_messages():
    SHARED_FILE.parent.mkdir(parents=True, exist_ok=True)

    counter = 0
    while True:
        counter += 1
        message = f"Message #{counter} from producer"
        with SHARED_FILE.open("a") as file:
            file.write(message + "\n")

        print(f"Written: {message}", flush=True)
        time.sleep(5)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"Hello from producer!"

        self.send_response(200)
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    Thread(target=write_messages, daemon=True).start()
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
