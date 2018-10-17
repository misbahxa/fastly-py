import os
import click
import fastly

api = fastly.API(key=os.environ['FASTLY_API_KEY'])

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
def listall(service, version):
    dictionary_line = "{id},{name},{created_at},{updated_at}"
    print dictionary_line.replace('{','').replace('}','')
    for dictionary in api.dictionaries(service, version):
        print dictionary_line.format(
            **dictionary.attrs 
        )

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
@click.option('--name', required=True)
def show(service, version, name):
    dictionary_line = "dictionary_id: {id}\nname: {name}\ncreated_at: {created_at}\nupdated_at: {updated_at}"
    print dictionary_line.format( **api.dictionary(service, version, name).attrs )