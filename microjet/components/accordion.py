from .component import Component


class Item(Component):
    def __init__(self, title, *children):
        super().__init__(*children)
        self.title = title


class Accordion(Component):
    def __init__(self, *items, multiple=False):
        self.items = items
        self.multiple = multiple

    def render(self):

        accordion_id = f"acc_{id(self)}"

        items_html = ""

        for i, item in enumerate(self.items):

            items_html += f"""
            <div
                style="
                    border:1px solid #e5e7eb;
                    border-radius:12px;
                    margin-bottom:10px;
                    overflow:hidden;
                    background:white;
                "
            >

                <button
                    onclick="toggle_{accordion_id}('{i}')"
                    style="
                        width:100%;
                        padding:14px 18px;
                        border:none;
                        background:#f8fafc;
                        text-align:left;
                        cursor:pointer;
                        font-size:15px;
                        font-weight:600;
                    "
                >
                    {item.title}
                </button>

                <div
                    id="{accordion_id}_{i}"
                    style="
                        display:none;
                        padding:16px;
                    "
                >
                    {item.render_children()}
                </div>

            </div>
            """

        close_others = ""

        if not self.multiple:
            close_others = f"""
            document
            .querySelectorAll('[id^="{accordion_id}_"]')
            .forEach(el=>{{
                el.style.display='none';
            }});
            """

        return f"""
        <div>
            {items_html}
        </div>

        <script>
        function toggle_{accordion_id}(id){{

            const target =
                document.getElementById(
                    '{accordion_id}_' + id
                );

            const open =
                target.style.display === 'block';

            {close_others}

            if(!open){{
                target.style.display='block';
            }}
        }}
        </script>
        """