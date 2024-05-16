import click
from connie.commands import add


@click.group()
def cli():
    """
    Hi, connie here: what can I do for you?
    """
    pass


cli.add_command(add)

if __name__ == "__main__":
    cli()
