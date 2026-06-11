from .router import Router
from .server import run_server

class App:
    def __init__(self):
        self.router = Router()

    def route(self, path, component):
        self.router.add_route(path, component)

    def run(self, host="127.0.0.1", port=2011):
        run_server(self.router, host, port)
