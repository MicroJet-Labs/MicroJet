class Button:
    def __init__(self, text):
        self.text = text

    def render(self):
        return f"<button>{self.text}</button>"
