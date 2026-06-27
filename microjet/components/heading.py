class Heading:
    def __init__(self, text, level=1):
        self.text = text
        self.level = level

    def render(self):

        sizes = {
            1: "text-5xl font-bold tracking-tight",
            2: "text-4xl font-bold tracking-tight",
            3: "text-3xl font-semibold",
            4: "text-2xl font-semibold",
            5: "text-xl font-medium",
            6: "text-lg font-medium",
        }

        cls = sizes.get(
            self.level,
            sizes[1]
        )

        return f"""
<h{self.level}
style="
    text-align:center;
    margin-bottom:16px;
"
>
{self.text}
</h{self.level}>
"""