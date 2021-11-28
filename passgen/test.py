import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")
    
@app.command()
def bye(name: str):
    typer.echo(f"bye {name}")
    
    

app()