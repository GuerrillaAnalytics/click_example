"""
Click command group called command2.
"""
import click


@click.group()
@click.pass_context
def command2(ctx):
    pass


@command2.command('add')
@click.option('--alert', '-a', default=True)
@click.argument('name')
@click.argument('url')
@click.pass_obj
def command2_add(ctx, name, url, alert):
    pass


@command2.command('delete')
@click.argument('names', nargs=-1, required=True)
@click.pass_obj
def command2_delete(ctx, names):
    pass
