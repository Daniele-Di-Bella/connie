import click
import connie.commands
import connie.visualization

@click.group()
def cli():
    """
    Hi, connie here: what can I do for you?
    """
    pass


cli.add_command(connie.commands.add)
cli.add_command(connie.commands.delete)
cli.add_command(connie.commands.print_df)
cli.add_command(connie.commands.clear_closed)
cli.add_command(connie.visualization.net_map)

if __name__ == "__main__":
    cli()
