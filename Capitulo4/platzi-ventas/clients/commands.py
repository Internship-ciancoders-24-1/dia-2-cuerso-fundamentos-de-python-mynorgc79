import click 

@click.group
def clients():
    pass

@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
#    create va a crear un nuevo cliente 
    pass
    

@clients.command()
@click.pass_context
def list(ctx):
    pass


@clients.command()
@click.pass_context
def update(ctx,client_uid):
    pass


@clients.command()
@click.pass_context
def delete(ctx,client_uid):
    pass


all = clients