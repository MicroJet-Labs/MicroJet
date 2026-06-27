class Div:
    def __init__(self, *children):
        self.children = children

    def render(self):
        body = "".join(c.render() for c in self.children)
        return f"<div>{body}</div>"
