import os
import click
import fastly

api = fastly.API(key=os.environ['FASTLY_API_KEY'])

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
def listall(service, version):
    snippet_line = "{id},{name},{priority},{type},{updated_at},{dynamic}"
    print snippet_line.replace('{','').replace('}','')
    for snippet in api.snippets(service, version):
        print snippet_line.format(
            **snippet.attrs
        )

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
@click.option('--name', required=True)
def show(service, version ,name):
    snippet_line = "id: {id}\nname: {name}\npriority: {priority}\ntype: {type}\nupdated_at: {updated_at}\ndynamic: {dynamic}\ncontent:\n{content}"
    print snippet_line.format( **api.snippet(service, version, name).attrs )