from .component import Component


class Avatar(Component):
    def __init__(
        self,
        src=None,
        alt="Avatar",
        name="",
        size="md",
        rounded=True,
        **props
    ):
        super().__init__(**props)

        self.src = src
        self.alt = alt
        self.name = name
        self.size = size
        self.rounded = rounded

    def render(self):
        sizes = {
            "xs": "24px",
            "sm": "32px",
            "md": "48px",
            "lg": "64px",
            "xl": "96px"
        }

        size = sizes.get(self.size, "48px")
        radius = "50%" if self.rounded else "12px"

        if self.src:
            return f"""
            <img
                src="{self.src}"
                alt="{self.alt}"
                style="
                    width:{size};
                    height:{size};
                    border-radius:{radius};
                    object-fit:cover;
                    display:block;
                "
            />
            """

        initial = (
            self.name[0].upper()
            if self.name
            else "?"
        )

        return f"""
        <div
            style="
                width:{size};
                height:{size};
                border-radius:{radius};
                background:#2563eb;
                color:white;
                display:flex;
                align-items:center;
                justify-content:center;
                font-weight:bold;
                font-size:calc({size}/2.5);
                user-select:none;
            "
        >
            {initial}
        </div>
        """