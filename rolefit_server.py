"""Serve RoleFit locally so browser clipboard and module loading work."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser
from threading import Thread


ROOT = Path(__file__).resolve().parent
PORTS = (8765, 8766, 8767)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt, *args):
        print("RoleFit:", fmt % args)


def main():
    server = None
    for port in PORTS:
        try:
            server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
            break
        except OSError:
            continue
    if server is None:
        raise SystemExit("Ports 8765–8767 are busy. Close the other local server and try again.")

    url = f"http://127.0.0.1:{server.server_port}/rolefit-ai.html"
    print(f"RoleFit is running at {url}")
    print("This server listens only on this computer. Press Ctrl+C to stop it.")
    worker = Thread(target=server.serve_forever, daemon=True)
    worker.start()
    webbrowser.open(url)
    try:
        while worker.is_alive():
            worker.join(timeout=1)
    except KeyboardInterrupt:
        print("\nStopping RoleFit server…")
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
