from .component import Component


class Head:
    def __init__(self, *columns):
        self.columns = columns


class Row:
    def __init__(self, *cells):
        self.cells = cells


class Table(Component):
    def __init__(
        self,
        head,
        *rows,
        striped=True,
        hover=True,
        bordered=False
    ):
        self.head = head
        self.rows = rows
        self.striped = striped
        self.hover = hover
        self.bordered = bordered

    def render(self):

        headers = ""

        for column in self.head.columns:
            headers += f"""
            <th
                style="
                    padding:14px 16px;
                    text-align:left;
                    background:#f8fafc;
                    font-weight:600;
                    border-bottom:1px solid #e5e7eb;
                "
            >
                {column}
            </th>
            """

        body = ""

        for index, row in enumerate(self.rows):

            bg = ""

            if self.striped and index % 2:
                bg = "background:#f8fafc;"

            cells = ""

            for cell in row.cells:
                cells += f"""
                <td
                    style="
                        padding:14px 16px;
                        border-bottom:1px solid #f1f5f9;
                    "
                >
                    {cell}
                </td>
                """

            hover_attr = ""

            if self.hover:
                hover_attr = """
                onmouseover="
                    this.style.background='#eef2ff'
                "
                onmouseout="
                    this.style.background=''
                "
                """

            body += f"""
            <tr
                style="{bg}"
                {hover_attr}
            >
                {cells}
            </tr>
            """

        border = ""

        if self.bordered:
            border = """
            border:1px solid #e5e7eb;
            """

        return f"""
        <div
            style="
                overflow-x:auto;
                border-radius:12px;
            "
        >
            <table
                style="
                    width:100%;
                    border-collapse:collapse;
                    background:white;
                    {border}
                "
            >
                <thead>
                    <tr>
                        {headers}
                    </tr>
                </thead>

                <tbody>
                    {body}
                </tbody>
            </table>
        </div>
        """