import typer
from typing import Optional
from pick import pick

from .data import Data
from .display import Display

app = typer.Typer(help="Cheatbox - Cheatsheet in Bentobox", context_settings={"help_option_names" : ["-h", "--help"]})

@app.command()
def list():
    domain = Data().run()
    Display().display_bento(domain)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        list()

if __name__ == "__main__":
    app()
