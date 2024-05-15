import click
from connie.commands import add


@click.group()
def cli():
    pass


cli.add_command(add)

if __name__ == "__main__":
    cli()
