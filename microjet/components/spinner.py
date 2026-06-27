from .component import Component


class Spinner(Component):
    def __init__(
        self,
        *children,
        size="md",
        color="#2563eb",
        **props
    ):
        super().__init__(*children, **props)

        self.size = size
        self.color = color

    def render(self):

        sizes = {
            "xs": "16px",
            "sm": "24px",
            "md": "40px",
            "lg": "56px",
            "xl": "72px"
        }

        spinner_size = sizes.get(
            self.size,
            "40px"
        )

        children_html = ""

        if hasattr(self, "render_children"):
            children_html = self.render_children()

        return f"""
        <div
            style="
                display:flex;
                flex-direction:column;
                align-items:center;
                justify-content:center;
                gap:12px;
            "
        >
            <div
                style="
                    width:{spinner_size};
                    height:{spinner_size};
                    border:4px solid #e5e7eb;
                    border-top:4px solid {self.color};
                    border-radius:50%;
                    animation:mjSpin .8s linear infinite;
                "
            ></div>

            {children_html}
        </div>

        <style>
        @keyframes mjSpin {{

            from {{
                transform:rotate(0deg);
            }}

            to {{
                transform:rotate(360deg);
            }}
        }}
        </style>
        """