class Link:
    def __init__(self, text, href):
        self.text = text
        self.href = href

    def render(self):
        return f'<a href="{self.href}">{self.text}</a>'