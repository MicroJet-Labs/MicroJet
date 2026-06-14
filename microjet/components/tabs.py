from .component import Component


class Tab(Component):
    def __init__(self, title, *children):
        super().__init__(*children)
        self.title = title


class Tabs(Component):
    def __init__(self, *tabs):
        self.tabs = tabs

    def render(self):

        tabs_id = f"tabs_{id(self)}"

        headers = ""
        contents = ""

        for index, tab in enumerate(self.tabs):

            active = index == 0

            btn_style = """
            background:#2563eb;
            color:white;
            """ if active else """
            background:transparent;
            color:#64748b;
            """

            display = "block" if active else "none"

            headers += f"""
            <button
                class="{tabs_id}_btn"
                onclick="openTab_{tabs_id}(event,'{tabs_id}_{index}')"
                style="
                    padding:10px 16px;
                    border:none;
                    border-radius:10px;
                    cursor:pointer;
                    transition:.2s;
                    {btn_style}
                "
            >
                {tab.title}
            </button>
            """

            contents += f"""
            <div
                id="{tabs_id}_{index}"
                class="{tabs_id}_content"
                style="
                    display:{display};
                    padding:20px 0;
                "
            >
                {tab.render_children()}
            </div>
            """

        return f"""
        <div>

            <div
                style="
                    display:flex;
                    gap:8px;
                    padding:6px;
                    background:#f8fafc;
                    border-radius:12px;
                    width:max-content;
                "
            >
                {headers}
            </div>

            {contents}

        </div>

        <script>
        function openTab_{tabs_id}(evt,id){{
        
            document
            .querySelectorAll('.{tabs_id}_content')
            .forEach(tab=>{{
                tab.style.display='none';
            }});

            document
            .querySelectorAll('.{tabs_id}_btn')
            .forEach(btn=>{{
                btn.style.background='transparent';
                btn.style.color='#64748b';
            }});

            document
            .getElementById(id)
            .style.display='block';

            evt.currentTarget.style.background='#2563eb';
            evt.currentTarget.style.color='white';
        }}
        </script>
        """