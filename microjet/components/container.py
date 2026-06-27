from .component import Component

class Container(Component):

    def __init__(
        self,
        *children,
        title=None,
        size="default"
    ):
        super().__init__(*children)

        self.title = title
        self.size = size

    def render(self):

        sizes = {
            "sm": "640px",
            "md": "768px",
            "lg": "1024px",
            "default": "1280px",
            "xl": "1400px",
            "full": "100%"
        }

        max_width = sizes.get(
            self.size,
            sizes["default"]
        )

        title_html = ""

        if self.title:
            title_html = f"""
            <div
                style="
                    margin-bottom:24px;
                "
            >
                <h2
                    style="
                        font-size:2rem;
                        font-weight:700;
                        color:#0f172a;
                    "
                >
                    {self.title}
                </h2>
            </div>
            """

        return f"""
        <section
            style="
                width:100%;
                max-width:{max_width};
                margin:48px auto;
                padding:0 24px;
                box-sizing:border-box;
            "
        >
            {title_html}

            {self.render_children()}

        </section>
        """