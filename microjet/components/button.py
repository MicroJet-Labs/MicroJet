from .component import Component

class Button(Component):
    def __init__(
        self,
        text,
        variant="primary",
        size="md"
    ):
        self.text = text
        self.variant = variant
        self.size = size

    def render(self):

        colors = {
            "primary": "#2563eb",
            "secondary": "#64748b",
            "success": "#16a34a",
            "danger": "#dc2626"
        }

        color = colors.get(self.variant, "#2563eb")

        return f"""
        <button
            style="
                background:{color};
                color:white;
                border:none;
                padding:10px 16px;
                border-radius:8px;
                cursor:pointer;
            "
        >
            {self.text}
        </button>
        """