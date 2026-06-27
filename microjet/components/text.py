from .component import Component

class Text(Component):

    def __init__(
        self,
        text,
        variant="default",
        font_size=None
    ):
        self.text = text
        self.variant = variant
        self.font_size = font_size

    def render(self):

        styles = {

            "default": """
                color:#334155;
                font-size:16px;
                line-height:1.75;
                font-weight:400;
            """,

            "muted": """
                color:#64748b;
                font-size:14px;
                line-height:1.6;
                font-weight:400;
            """,

            "small": """
                color:#64748b;
                font-size:12px;
                line-height:1.5;
                font-weight:400;
            """,

            "lead": """
                color:#475569;
                font-size:20px;
                line-height:1.8;
                font-weight:400;
            """,

            "large": """
                color:#0f172a;
                font-size:18px;
                line-height:1.7;
                font-weight:600;
            """
        }

        style = styles.get(
            self.variant,
            styles["default"]
        )

        font_size = ""

        if self.font_size:
            font_size = f"font-size:{self.font_size}px;"

        return f"""
        <p
            style="
                text-align:center;
                margin:0;
                {style}
                {font_size}
            "
        >
            {self.text}
        </p>
        """