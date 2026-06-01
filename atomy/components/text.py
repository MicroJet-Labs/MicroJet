class Text:
    def __init__(self, text):
        self.text = text

    def render(self):
        return f"<p>{self.text}</p>"
