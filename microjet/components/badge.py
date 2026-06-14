from .component import Component


class Badge(Component):
    def __init__(
        self,
        *children,
        variant="primary",
        pill=False,
        **props
    ):
        super().__init__(*children, **props)

        self.variant = variant
        self.pill = pill

    def render(self):
        variants = {
            "primary": {
                "bg": "#2563eb",
                "color": "#ffffff"
            },
            "secondary": {
                "bg": "#64748b",
                "color": "#ffffff"
            },
            "success": {
                "bg": "#16a34a",
                "color": "#ffffff"
            },
            "danger": {
                "bg": "#dc2626",
                "color": "#ffffff"
            },
            "warning": {
                "bg": "#f59e0b",
                "color": "#ffffff"
            },
            "info": {
                "bg": "#0ea5e9",
                "color": "#ffffff"
            },
            "light": {
                "bg": "#f1f5f9",
                "color": "#334155"
            }
        }

        style = variants.get(
            self.variant,
            variants["primary"]
        )

        radius = "999px" if self.pill else "8px"

        return f"""
        <span
            style="
                display:inline-flex;
                align-items:center;
                gap:4px;
                padding:4px 10px;
                background:{style['bg']};
                color:{style['color']};
                border-radius:{radius};
                font-size:12px;
                font-weight:600;
                line-height:1.5;
            "
        >
            {self.render_children()}
        </span>
        """