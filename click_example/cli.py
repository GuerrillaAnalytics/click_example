"""
Based on
https://stackoverflow.com/questions/34643620/
how-can-i-split-my-click-commands-each-with-a-set-of-sub-commands-into-multipl

"""
import click
import sys
import os.path


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from click_example.commands.command1_grp.cmd import command1
from click_example.commands.command2_grp.cmd import command2


@click.group()
@click.version_option()
def cli():
    pass


# add each group here
# declare the group is package and define function with same name
cli.add_command(command1)
cli.add_command(command2)


if __name__ == '__main__':
    cli()
