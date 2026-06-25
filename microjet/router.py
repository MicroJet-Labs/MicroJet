class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, component):
        self.routes[path] = component

    def get(self, path):
        return self.routes.get(path)
