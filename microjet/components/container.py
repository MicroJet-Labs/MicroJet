class Container:
    def __init__(self, *children):
        self.children = children

    def render(self):
        return "<div class='container'>" + "".join(
            c.render() for c in self.children
        ) + "</div>"