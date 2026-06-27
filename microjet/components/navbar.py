from .component import Component


class Navbar(Component):
    def __init__(
        self,
        *children,
        sticky=False,
        **props
    ):
        super().__init__(*children, **props)

        self.sticky = sticky

    def render(self):

        position = ""

        if self.sticky:
            position = """
            position:sticky;
            top:0;
            z-index:1000;
            """

        return f"""
        <nav
            style="
                {position}
                display:flex;
                justify-content:space-between;
                align-items:center;
                padding:14px 24px;
                background:white;
                border-bottom:1px solid #e5e7eb;
                box-shadow:0 2px 10px rgba(0,0,0,0.05);
            "
        >
            {self.render_children()}
        </nav>
        """


class NavbarBrand(Component):
    def render(self):

        return f"""
        <div
            style="
                font-size:22px;
                font-weight:700;
            "
        >
            {self.render_children()}
        </div>
        """


class NavbarMenu(Component):
    def render(self):

        return f"""
        <div
            style="
                display:flex;
                gap:10px;
                align-items:center;
            "
        >
            {self.render_children()}
        </div>
        """


class NavbarItem(Component):
    def __init__(
        self,
        text,
        href="#",
        **props
    ):
        super().__init__(**props)

        self.text = text
        self.href = href

    def render(self):

        return f"""
        <a
            href="{self.href}"
            style="
                text-decoration:none;
                color:#334155;
                font-weight:500;
                padding:8px 12px;
                border-radius:8px;
                transition:.2s;
            "
            onmouseover="
                this.style.background='#f1f5f9'
            "
            onmouseout="
                this.style.background='transparent'
            "
        >
            {self.text}
        </a>
        """