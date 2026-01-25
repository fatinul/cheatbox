import typer
from typing import Optional
from pick import pick

from .data import Data
from .display import Display

app = typer.Typer(help="Cheatbox - Cheatsheet in Bentobox", context_settings={"help_option_names" : ["-h", "--help"]})

@app.command()
def list():
    """Browse and display cheatsheets"""
    data = Data()
    domain_data = data.run()
    Display().display_bento(domain_data)

@app.command()
def search(query: str = typer.Argument(..., help="Search query for fuzzy search")):
    """Search through available cheatsheets using fuzzy matching"""
    from pathlib import Path
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"

    domains = sorted([
        file.stem for file in data_dir.glob("*.json")
        if file.name != "ascii.json"
    ])

    data = Data()
    results = data.fuzzy_search(query, domains, threshold=0.2)

    if not results:
        typer.echo(f"❌ No cheatsheets found matching '{query}'")
        return

    if len(results) == 1:
        data.domain = results[0]
        domain_data = data.read_domain()
        Display().display_bento(domain_data)
    else:
        selected_cheat, _ = pick(
            options=results,
            title=f"🔍 Search results for '{query}'",
            indicator="→"
        )
        data.domain = selected_cheat
        domain_data = data.read_domain()
        Display().display_bento(domain_data)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        list()

if __name__ == "__main__":
    app()
