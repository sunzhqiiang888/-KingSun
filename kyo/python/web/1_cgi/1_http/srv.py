#!/usr/bin/env python3


from http.server import HTTPServer, SimpleHTTPRequestHandler


if __name__ == "__main__":
    def main():
        HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler).serve_forever()

    main()
