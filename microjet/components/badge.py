from .component import Component


class Badge(Component):
    def __init__(
        self,
        *children,
        variant="default",
        pill=True,
        group=False,
        **props
    ):
        super().__init__(*children, **props)

        self.variant = variant
        self.pill = pill
        self.group = group

    def render(self):

        if self.group:
            return f"""
            <div
                style="
                    display:flex;
                    flex-wrap:wrap;
                    justify-content:center;
                    align-items:center;
                    gap:8px;
                    margin-top: 20px;
                "
            >
                {self.render_children()}
            </div>
            """

        variants = {
            "default": {
                "bg": "#eff6ff",
                "color": "#2563eb",
                "border": "#bfdbfe"
            },
            "success": {
                "bg": "#ecfdf5",
                "color": "#16a34a",
                "border": "#bbf7d0"
            },
            "danger": {
                "bg": "#fef2f2",
                "color": "#dc2626",
                "border": "#fecaca"
            },
            "warning": {
                "bg": "#fffbeb",
                "color": "#d97706",
                "border": "#fde68a"
            },
            "secondary": {
                "bg": "#f8fafc",
                "color": "#475569",
                "border": "#e2e8f0"
            }
        }

        style = variants.get(
            self.variant,
            variants["default"]
        )

        radius = "999px" if self.pill else "10px"

        return f"""
        <span
            style="
                display:inline-flex;
                align-items:center;
                justify-content:center;

                padding:6px 12px;

                background:{style['bg']};
                color:{style['color']};

                border:1px solid {style['border']};

                border-radius:{radius};

                font-size:12px;
                font-weight:600;
            "
        >
            {self.render_children()}
        </span>
        """