from .component import Component


class Sidebar(Component):
    def __init__(
        self,
        *children,
        width="260px",
        fixed=True,
        **props
    ):
        super().__init__(*children, **props)

        self.width = width
        self.fixed = fixed

    def render(self):

        position = ""

        if self.fixed:
            position = """
            position:fixed;
            left:0;
            top:0;
            height:100vh;
            """

        return f"""
        <aside
            style="
                {position}
                width:{self.width};
                background:white;
                border-right:1px solid #e5e7eb;
                padding:20px;
                box-sizing:border-box;
                overflow-y:auto;
            "
        >
            {self.render_children()}
        </aside>
        """


class SidebarHeader(Component):
    def render(self):

        return f"""
        <div
            style="
                display:flex;
                align-items:center;
                gap:12px;
                margin-bottom:20px;
                padding-bottom:16px;
                border-bottom:1px solid #e5e7eb;
            "
        >
            {self.render_children()}
        </div>
        """


class SidebarItem(Component):
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
                display:block;
                padding:12px 16px;
                color:#334155;
                text-decoration:none;
                border-radius:8px;
                margin-bottom:4px;
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


class SidebarGroup(Component):
    def __init__(
        self,
        title,
        *children,
        **props
    ):
        super().__init__(*children, **props)

        self.title = title

    def render(self):

        return f"""
        <div style="margin-top:20px;">
            <div
                style="
                    font-size:12px;
                    font-weight:700;
                    color:#64748b;
                    text-transform:uppercase;
                    margin-bottom:8px;
                "
            >
                {self.title}
            </div>

            {self.render_children()}
        </div>
        """