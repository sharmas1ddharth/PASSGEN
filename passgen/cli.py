"""CLI interface for the app"""
from typing import Optional
import typer
# from passgen import __version__


app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"PASSGEN, v=0.1.0")
        raise typer.Exit()
    
@app.callback()
def main(version: Optional[bool] = typer.Option(
    None,
    "--version",
    "-v",
    help="Shows application version and name.",
    callback = _version_callback,
    is_eager=True
)) -> None:
    return
    
app()