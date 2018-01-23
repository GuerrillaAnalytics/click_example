import click


@click.group()
@click.pass_context
def command1(ctx):
    pass


@command1.group('zone')
@click.pass_context
def command1_zone():
    pass


@command1_zone.command('add')
@click.option('--jumpstart', '-j', default=True)
@click.option('--organization', '-o', default='')
@click.argument('url')
@click.pass_obj
def command1_zone_add(ctx, url, jumpstart, organization):
    pass


################################################################################

@command1.group('record')
def cloudflare_record():
    pass


@cloudflare_record.command('add')
@click.option('--ttl', '-t')
@click.argument('domain')
@click.argument('name')
@click.argument('type')
@click.argument('content')
@click.pass_obj
def cloudflare_record_add(ctx, domain, name, type, content, ttl):
    pass


@cloudflare_record.command('edit')
@click.option('--ttl', '-t')
@click.argument('domain')
@click.argument('name')
@click.argument('type')
@click.argument('content')
@click.pass_obj
def cloudflare_record_edit(ctx, domain):
    pass
