from .component import Component


class Button(Component):

    def __init__(
        self,
        text,
        variant="default",
        size="default",
        align=None
    ):
        self.text = text
        self.variant = variant
        self.size = size
        self.align = align

    def render(self):

        variants = {

            "default": """
                background:#2563eb;
                color:white;
                border:none;
            """,

            "destructive": """
                background:#dc2626;
                color:white;
                border:none;
            """,

            "outline": """
                background:white;
                color:#0f172a;
                border:1px solid #e2e8f0;
            """,

            "secondary": """
                background:#f1f5f9;
                color:#0f172a;
                border:none;
            """,

            "ghost": """
                background:transparent;
                color:#0f172a;
                border:none;
            """,

            "link": """
                background:transparent;
                color:#2563eb;
                border:none;
                text-decoration:underline;
            """
        }

        sizes = {

            "sm": """
                padding:8px 14px;
                font-size:13px;
            """,

            "default": """
                padding:10px 18px;
                font-size:14px;
            """,

            "lg": """
                padding:14px 24px;
                font-size:16px;
            """
        }

        wrapper_style = ""

        if self.align == "center":
            wrapper_style = """
                display:flex;
                justify-content:center;
                width:100%;
            """

        elif self.align == "right":
            wrapper_style = """
                display:flex;
                justify-content:flex-end;
                width:100%;
            """

        elif self.align == "left":
            wrapper_style = """
                display:flex;
                justify-content:flex-start;
                width:100%;
            """

        return f"""
        <div style="{wrapper_style}">
            <button

                onmouseover="
                    this.style.transform='translateY(-2px)';
                    this.style.opacity='0.95';
                    this.style.boxShadow='0 8px 20px rgba(0,0,0,.12)';
                "

                onmouseout="
                    this.style.transform='translateY(0)';
                    this.style.opacity='1';
                    this.style.boxShadow='0 1px 2px rgba(0,0,0,.05)';
                "

                style="
                    display:inline-flex;
                    align-items:center;
                    justify-content:center;

                    gap:8px;

                    font-weight:600;

                    border-radius:12px;

                    cursor:pointer;

                    transition:all .2s ease;

                    box-shadow:
                    0 1px 2px rgba(0,0,0,.05);

                    {sizes.get(
                        self.size,
                        sizes['default']
                    )}

                    {variants.get(
                        self.variant,
                        variants['default']
                    )}
                "
            >
                {self.text}
            </button>
        </div>
        """