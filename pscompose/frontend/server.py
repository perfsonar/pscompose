import os
import posixpath
from urllib.parse import unquote
import http.server

# BaseHTTPServer
# from SimpleHTTPServer import SimpleHTTPRequestHandler

# modify this to add additional routes
STATIC_ROUTES = (
    # [url_prefix]
    "/pages",
    "/partials",
    "/lib",
    "/app",
    "/components",
    "/css",
    "/mockups",
    "/dummy_api"
)


def normalize_path(path, root):
    # normalize path and prepend root directory
    path = path.split("?", 1)[0]
    path = path.split("#", 1)[0]
    path = posixpath.normpath(unquote(path))
    words = path.split("/")
    words = filter(None, words)

    path = root
    for word in words:
        drive, word = os.path.splitdrive(word)
        head, word = os.path.split(word)
        if word in (os.curdir, os.pardir):
            continue
        path = os.path.join(path, word)
    return path


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        """translate path given routes"""

        # set default root to cwd
        root = os.getcwd()

        # this is an SPA app. By default, vend index.html for all routes
        output_path = os.path.join(root, "app/%s/index.html" % path)
        # unless the route is listed in STATIC_ROUTES. In that case...
        for pattern in STATIC_ROUTES:
            if path.startswith(pattern):
                # remove the static section from the url
                # and then normalize the path to the real file on disk
                output_path = normalize_path(path, root)
                break
        print("reading file from %s" % output_path)
        return output_path


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8000
    server = http.server.HTTPServer((HOST, PORT), RequestHandler)
    print("Serving HTTP on %s:%s" % (HOST, PORT))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    print("\nExiting on Interrupt")
    server.server_close()
