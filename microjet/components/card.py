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
                margin-top:20px;
                padding-top:20px;
                border-top:1px solid #f1f5f9;
            ">
                {footer_html}
            </div>
            """

        return f"""
        <div

            onmouseover="
                this.style.transform='translateY(-4px)';
                this.style.boxShadow='0 20px 40px rgba(0,0,0,.08)';
            "

            onmouseout="
                this.style.transform='translateY(0)';
                this.style.boxShadow='0 1px 3px rgba(0,0,0,.08)';
            "

            style="
                background:#ffffff;

                border:1px solid #e2e8f0;

                border-radius:20px;

                padding:32px;

                transition:all .25s ease;

                box-shadow:
                0 1px 3px rgba(0,0,0,.08);

                overflow:hidden;
            "
        >

            {self.render_children()}

            {footer_html}

        </div>
        """