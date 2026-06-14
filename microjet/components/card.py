from .component import Component

class Card(Component):
    def __init__(
        self,
        *children,
        footer=None,
        **props
    ):
        super().__init__(*children, **props)

        self.footer = footer

    def render(self):

        footer_html = ""

        if self.footer:

            if hasattr(self.footer, "render"):
                footer_html = self.footer.render()
            else:
                footer_html = str(self.footer)

            footer_html = f"""
            <div style="
                border-top:1px solid #e5e7eb;
                padding-top:12px;
                margin-top:12px;
            ">
                {footer_html}
            </div>
            """

        return f"""
        <div style="
            background:white;
            border:1px solid #e5e7eb;
            border-radius:12px;
            padding:20px;
            box-shadow:0 2px 8px rgba(0,0,0,0.08);
        ">
            {self.render_children()}
            {footer_html}
        </div>
        """