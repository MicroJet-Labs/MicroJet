class Component:
    def __init__(self, *children, **props):
        self.children = children
        self.props = props

    def render_children(self):
        html = ""

        for child in self.children:
            if hasattr(child, "render"):
                html += child.render()
            else:
                html += str(child)

        return html

    def render(self):
        return ""