from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.console import Group
from rich import box

class Display:
    def __init__(self) -> None:
        self.command_width: int = 25
        self.outer_width: int = 130

        # style scheme
        self.primary_style: str = "blue"
        self.header_style = "dim white"
        self.description_style = "white"

    def get_height(self, category_name, commands):
        """Get the expected height of panel"""
        # Calculations: 2 (:Panel borders) + 2 (:Table header/divider) + N (rows)
        return 4 + len(commands)

    def box(self, category, commands, extra_padding=0):
        """Panel for each subdomain"""
        table = Table(show_header=True, header_style=f"bold {self.header_style}", box=None, expand=True)
        table.add_column(header="Command", style=self.primary_style, width=self.command_width, justify='right')
        table.add_column(header="Description",style=self.description_style)

        for item in commands:
            table.add_row(item['command'], item['description'])

        # Adding padding as empty rows in the table to stretch the panel
        for _ in range(extra_padding):
            table.add_row("", "")

        return Panel(
            table,
            title=f"[{self.primary_style}]{category}[/{self.primary_style}]",
            title_align="left",
            border_style=self.primary_style,
        )

    def get_ascii_panel(self, json_data, key):
        """Extracts ASCII array from json_data, joins it, and returns a Panel."""
        if key in json_data and json_data[key]:
            text = "\n".join(json_data[key][0]["ascii"])
            return Panel(text, expand=False, box=box.SIMPLE_HEAD)
        return None

    def display_bento(self, json_data):
        """Panel of the panels"""
        # Get the preconfigured style for domain
        if "STYLE" in json_data:
            self.command_width = int(json_data["STYLE"]["command_width"])
            self.outer_width = int(json_data["STYLE"]["outer_width"])
            self.primary_style = json_data["STYLE"]["primary_color"]
            del json_data["STYLE"]

        console = Console(width=self.outer_width)

        # Get the ASCII art for header
        header_grid = Table.grid()
        header_grid.add_column(ratio=1, justify='left') # Column for Logo
        header_grid.add_column(ratio=2) # Column for Title

        logo_panel = self.get_ascii_panel(json_data, "LOGO")
        title_panel = self.get_ascii_panel(json_data, "TITLE")
        if title_panel:
            title_panel.subtitle = "CheatBox "

        # Display the Logo and title
        if logo_panel or title_panel:
            header_grid.add_row(logo_panel, title_panel)
            console.print(header_grid)

            if "LOGO" in json_data: del json_data["LOGO"]
            if "TITLE" in json_data: del json_data["TITLE"]

        cats = list(json_data.keys()) # category
        left_cats = cats[::2]
        right_cats = cats[1::2]

        # Calculate total heights of each column
        left_height = sum(self.get_height(cat, json_data[cat]) for cat in left_cats)
        right_height = sum(self.get_height(cat, json_data[cat]) for cat in right_cats)

        left_panels = []
        right_panels = []

        # Build Left Column
        for i, cat in enumerate(left_cats):
            padding = 0
            # If this is the last box and the left side is shorter, add padding
            if i == len(left_cats) - 1 and left_height < right_height:
                padding = right_height - left_height
            left_panels.append(self.box(cat, json_data[cat], padding))

        # Build Right Column
        for i, cat in enumerate(right_cats):
            padding = 0
            # If this is the last box and the right side is shorter, add padding
            if i == len(right_cats) - 1 and right_height < left_height:
                padding = left_height - right_height
            right_panels.append(self.box(cat, json_data[cat], padding))

        outer_grid = Table.grid(expand=True, padding=(0,1,0,0))
        outer_grid.add_column(ratio=1)
        outer_grid.add_column(ratio=1)
        outer_grid.add_row(Group(*left_panels), Group(*right_panels))
        console.print(outer_grid)

