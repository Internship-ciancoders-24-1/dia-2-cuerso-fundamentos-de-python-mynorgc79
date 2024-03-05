import click

from clients import commands as clients_commands

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}

cli.add_commands(clients_commands.all)