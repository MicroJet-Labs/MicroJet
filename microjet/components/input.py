from .component import Component

class Input(Component):
    def __init__(
        self,
        placeholder="",
        value="",
        input_type="text",
        name="",
        disabled=False,
        **props
    ):
        super().__init__(**props)

        self.placeholder = placeholder
        self.value = value
        self.input_type = input_type
        self.name = name
        self.disabled = disabled

    def render(self):
        disabled = "disabled" if self.disabled else ""

        return f"""
        <input
            type="{self.input_type}"
            name="{self.name}"
            value="{self.value}"
            placeholder="{self.placeholder}"
            {disabled}
            style="
                width:100%;
                padding:12px 14px;
                border:1px solid #d1d5db;
                border-radius:8px;
                outline:none;
                font-size:14px;
                box-sizing:border-box;
            "
        />
        """