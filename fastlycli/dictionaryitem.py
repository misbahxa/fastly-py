import os
import sys
import click
import fastly
import urllib

api = fastly.API(key=os.environ['FASTLY_API_KEY'])


@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
@click.option('--dictionary_id', required=True)
def listall(service, version, dictionary_id):
    dictionaryitems_line = "{dictionary_id},{item_key},{item_value},{created_at},{updated_at}"
    print dictionaryitems_line.replace('{','').replace('}','')
    for dictionaryitem in api.dictionaryitems(service, version, dictionary_id):
        print dictionaryitems_line.format(
            **dictionaryitem.attrs
        )

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
@click.option('--dictionary_id', required=True)
@click.option('--item_key', required=True)
def show(service, version, dictionary_id, item_key):
    dictionaryitem_line = "dictionary_id: {dictionary_id}\nitem_key: {item_key}\nitem_value: {item_value}\ncreated_at: {created_at}\nupdated_at: {updated_at}"
    print dictionaryitem_line.format( **api.dictionaryitem(service, version, dictionary_id, item_key).attrs )

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
@click.option('--dictionary_id', required=True)
@click.option('--item_key', required=True)
def delete(service, version, dictionary_id, item_key):
    dictionaryitem_line = "dictionary_id: {dictionary_id}\nitem_key: {item_key}\nitem_value: {item_value}\ncreated_at: {created_at}\nupdated_at: {updated_at}"
    dictitem = api.dictionaryitem(service, version, dictionary_id, item_key)
    print dictionaryitem_line.format( **dictitem.attrs )
    dictitem.attrs['item_key'] = urllib.quote(dictitem.attrs['item_key'])
    if raw_input('Proceed deleting the above item? (Y/n)') == 'Y':
        dictitem.delete()

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
@click.option('--dictionary_id', required=True)
@click.option('--item_key', required=True)
@click.option('--item_value', required=True)
def add(service, version, dictionary_id, item_key, item_value):
    dictitem = api.dictionaryitems(service, version, dictionary_id)
    body = "item_key=%s&item_value=%s" % (item_key, item_value)
    dictitem.add(body)