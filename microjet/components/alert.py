from .component import Component

class Alert(Component):
    def __init__(
        self,
        *children,
        variant="info",
        closable=False,
        **props
    ):
        super().__init__(*children, **props)

        self.variant = variant
        self.closable = closable

    def render(self):

        variants = {
            "success": {
                "bg": "#dcfce7",
                "color": "#166534",
                "border": "#86efac"
            },
            "error": {
                "bg": "#fee2e2",
                "color": "#991b1b",
                "border": "#fca5a5"
            },
            "warning": {
                "bg": "#fef3c7",
                "color": "#92400e",
                "border": "#fcd34d"
            },
            "info": {
                "bg": "#dbeafe",
                "color": "#1e40af",
                "border": "#93c5fd"
            }
        }

        style = variants.get(
            self.variant,
            variants["info"]
        )

        close_btn = ""

        if self.closable:
            close_btn = """
            <button
                onclick="this.parentElement.remove()"
                style="
                    background:none;
                    border:none;
                    cursor:pointer;
                    font-size:18px;
                    margin-left:auto;
                "
            >
                ×
            </button>
            """

        return f"""
        <div
            style="
                background:{style['bg']};
                color:{style['color']};
                border:1px solid {style['border']};
                border-radius:10px;
                padding:14px 16px;
                display:flex;
                align-items:center;
                gap:10px;
                margin:10px 0;
            "
        >
            <div style="flex:1;">
                {self.render_children()}
            </div>

            {close_btn}
        </div>
        """