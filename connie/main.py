import click
from connie.commands import add
from connie.commands import delete
from connie.commands import print_df

@click.group()
def cli():
    """
    Hi, connie here: what can I do for you?
    """
    pass


cli.add_command(add)
cli.add_command(delete)
cli.add_command(print_df)

if __name__ == "__main__":
    cli()
