from .component import Component

class Modal(Component):
    def __init__(
        self,
        modal_id,
        *children,
        title="",
        width="500px",
        **props
    ):
        super().__init__(*children, **props)

        self.modal_id = modal_id
        self.title = title
        self.width = width

    def render(self):

        return f"""
        <div
            id="{self.modal_id}"
            style="
                display:none;
                position:fixed;
                top:0;
                left:0;
                width:100%;
                height:100%;
                background:rgba(0,0,0,0.5);
                z-index:9999;
                justify-content:center;
                align-items:center;
            "
        >
            <div
                style="
                    background:white;
                    width:{self.width};
                    max-width:90%;
                    border-radius:12px;
                    padding:24px;
                    box-shadow:0 10px 30px rgba(0,0,0,0.2);
                "
            >
                <div
                    style="
                        display:flex;
                        justify-content:space-between;
                        align-items:center;
                        margin-bottom:16px;
                    "
                >
                    <h2 style="margin:0;">
                        {self.title}
                    </h2>

                    <button
                        onclick="closeModal('{self.modal_id}')"
                        style="
                            border:none;
                            background:none;
                            font-size:22px;
                            cursor:pointer;
                        "
                    >
                        ×
                    </button>
                </div>

                <div>
                    {self.render_children()}
                </div>
            </div>
        </div>

        <script>
        function openModal(id){{
            document.getElementById(id).style.display='flex';
        }}

        function closeModal(id){{
            document.getElementById(id).style.display='none';
        }}
        </script>
        """