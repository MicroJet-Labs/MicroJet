from pathlib import Path
from .component import Component

class Logo(Component):

    def __init__(self, size=80):
        self.size = size

    def render(self):

        svg_path = (
            Path(__file__).parent.parent
            / "assets"
            / "microjet-rocket.svg"
        )

        svg = svg_path.read_text(encoding="utf-8")

        return f"""
        <div style="
            width:{self.size}px;
    height:{self.size}px;
    margin:0 auto;
    display:flex;
    justify-content:center;
    align-items:center;
        ">
            {svg}
        </div>
        """