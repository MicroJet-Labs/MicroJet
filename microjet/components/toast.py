from .component import Component


class Toast(Component):
    def __init__(
        self,
        *children,
        variant="info",
        duration=3000,
        position="top-right",
        **props
    ):
        super().__init__(*children, **props)

        self.variant = variant
        self.duration = duration
        self.position = position

    def render(self):

        variants = {
            "success": "#16a34a",
            "error": "#dc2626",
            "warning": "#f59e0b",
            "info": "#2563eb"
        }

        positions = {
            "top-right":
                "top:20px;right:20px;",

            "top-left":
                "top:20px;left:20px;",

            "bottom-right":
                "bottom:20px;right:20px;",

            "bottom-left":
                "bottom:20px;left:20px;"
        }

        bg = variants.get(
            self.variant,
            "#2563eb"
        )

        pos = positions.get(
            self.position,
            positions["top-right"]
        )

        toast_id = f"mj_toast_{id(self)}"

        return f"""
        <div
            id="{toast_id}"
            style="
                position:fixed;
                {pos}
                background:{bg};
                color:white;
                padding:14px 18px;
                border-radius:12px;
                min-width:260px;
                max-width:420px;
                display:flex;
                align-items:center;
                gap:10px;
                box-shadow:
                    0 10px 25px rgba(0,0,0,.15);
                z-index:9999;
                animation:mjToastIn .25s ease;
            "
        >
            {self.render_children()}
        </div>

        <style>
        @keyframes mjToastIn {{

            from {{
                opacity:0;
                transform:translateY(-12px);
            }}

            to {{
                opacity:1;
                transform:translateY(0);
            }}
        }}

        @keyframes mjToastOut {{

            from {{
                opacity:1;
            }}

            to {{
                opacity:0;
            }}
        }}
        </style>

        <script>
        setTimeout(function(){{

            const toast =
                document.getElementById(
                    '{toast_id}'
                );

            if(toast){{

                toast.style.animation =
                    'mjToastOut .25s ease';

                setTimeout(function(){{
                    toast.remove();
                }},250);
            }}

        }}, {self.duration});
        </script>
        """