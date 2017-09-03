import click
import sys
import os.path
from click_example.commands.cloudflare_grp.cmd import cloudflare
from click_example.commands.uptime_grp.cmd import uptimerobot

# Based on https://stackoverflow.com/questions/34643620/
# how-can-i-split-my-click-commands-each-with-a-set-of-sub-commands-into-multipl
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


@click.group()
@click.version_option()
def cli():
    pass


cli.add_command(cloudflare)
cli.add_command(uptimerobot)


if __name__ == '__main__':
    cli()
