from .component import Component


class Image(Component):

    def __init__(
        self,
        src,
        alt="",
        width="100%",
        height="auto",

        rounded="lg",
        fit="cover",

        shadow=True,
        bordered=False,

        device="all"
    ):

        self.src = src
        self.alt = alt

        self.width = width
        self.height = height

        self.rounded = rounded
        self.fit = fit

        self.shadow = shadow
        self.bordered = bordered

        self.device = device

    def render(self):

        radius_map = {
            "none": "0px",
            "sm": "6px",
            "md": "10px",
            "lg": "16px",
            "xl": "24px",
            "full": "999px"
        }

        radius = radius_map.get(
            self.rounded,
            "16px"
        )

        border = (
            "border:1px solid #e2e8f0;"
            if self.bordered
            else ""
        )

        shadow = (
            "box-shadow:0 10px 30px rgba(0,0,0,.12);"
            if self.shadow
            else ""
        )

        return f"""
        <img
            src="{self.src}"
            alt="{self.alt}"

            loading="lazy"

            style="
                width:{self.width};
                height:{self.height};

                object-fit:{self.fit};

                border-radius:{radius};

                {border}
                {shadow}

                transition:.25s ease;
            "

            onmouseover="
                this.style.transform='scale(1.02)';
            "

            onmouseout="
                this.style.transform='scale(1)';
            "
        />
        """