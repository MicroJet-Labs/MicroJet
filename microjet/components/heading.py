class Heading:
    def __init__(self, text, level=1):
        self.text = text
        self.level = level

    def render(self):
        return f"<h{self.level}>{self.text}</h{self.level}>"