class Image:
    def __init__(self, src, alt=""):
        self.src = src
        self.alt = alt

    def render(self):
        return f'<img src="{self.src}" alt="{self.alt}" />'