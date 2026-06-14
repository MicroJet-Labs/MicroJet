from .component import Component


class MenuItem:
    def __init__(self, text, href="#"):
        self.text = text
        self.href = href


class Dropdown(Component):
    def __init__(self, trigger, *items):
        self.trigger = trigger
        self.items = items

    def render(self):

        dropdown_id = f"dropdown_{id(self)}"

        menu = ""

        for item in self.items:

            menu += f"""
            <a
                href="{item.href}"
                style="
                    display:block;
                    padding:10px 14px;
                    color:#334155;
                    text-decoration:none;
                    transition:.2s;
                "
                onmouseover="
                    this.style.background='#f8fafc'
                "
                onmouseout="
                    this.style.background='transparent'
                "
            >
                {item.text}
            </a>
            """

        return f"""
        <div
            style="
                position:relative;
                display:inline-block;
            "
        >

            <div
                onclick="toggle_{dropdown_id}()"
                style="
                    cursor:pointer;
                "
            >
                {self.trigger.render()}
            </div>

            <div
                id="{dropdown_id}"
                style="
                    display:none;
                    position:absolute;
                    top:110%;
                    left:0;
                    min-width:220px;
                    background:white;
                    border:1px solid #e5e7eb;
                    border-radius:12px;
                    overflow:hidden;
                    box-shadow:
                        0 10px 25px rgba(0,0,0,.08);
                    z-index:9999;
                "
            >
                {menu}
            </div>

        </div>

        <script>
        function toggle_{dropdown_id}(){{
        
            const menu =
                document.getElementById(
                    '{dropdown_id}'
                );

            if(menu.style.display==='block'){{
                menu.style.display='none';
            }}
            else {{
                menu.style.display='block';
            }}
        }}

        document.addEventListener(
            'click',
            function(e){{
            
                const root =
                    document.getElementById(
                        '{dropdown_id}'
                    );

                if(
                    root &&
                    !root.parentElement.contains(
                        e.target
                    )
                ){{
                    root.style.display='none';
                }}
            }}
        );
        </script>
        """