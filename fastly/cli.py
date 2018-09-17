# coding=utf-8
"""
fastly - Fastly Command Line Utility
"""
import os
import sys
import json
import click
import fastly
import json
from helpers import output

from _version import __version__ as fastly_version


api = fastly.API(key=os.environ['FASTLY_API_KEY'])


@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
@click.option('--csv', type=bool)
def snippets(service, version):
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
def snippet(service, version ,name):
    snippet_line = "id: {id}\nname: {name}\npriority: {priority}\ntype: {type}\nupdated_at: {updated_at}\ndynamic: {dynamic}\ncontent:\n{content}"
    print snippet_line.format( **api.snippet(service, version, name).attrs )

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
def dictionaries(service, version):
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
def dictionary(service, version, name):
    dictionary_line = "id: {id}\nname: {name}\ncreated_at: {created_at}\nupdated_at: {updated_at}"
    print dictionary_line.format( **api.dictionary(service, version, name).attrs )


@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
@click.option('--id', required=True)
def dictionaryitems(service, version, id):
    dictionaryitems_line = "{dictionary_id},{item_key},{item_value},{created_at},{updated_at}"
    print dictionaryitems_line.replace('{','').replace('}','')
    for dictionaryitem in api.dictionaryitems(service, version, id).attrs:
        print dictionaryitems_line.format(
            **dictionaryitem 
        )


@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
@click.option('--id', required=True)
@click.option('--key', required=True)
def dictionaryitem(service, version, id, key):
    dictionaryitem_line = "dictionary_id: {dictionary_id}\nitem_key: {item_key}\nitem_value: {item_value}\ncreated_at: {created_at}\nupdated_at: {updated_at}"
    print dictionaryitem_line.format( **api.dictionaryitem(service, version, id, key).attrs )


@click.group()
def main():
    if "FASTLY_API_KEY" not in os.environ:
        raise Exception("FASTLY_API_KEY is not exist in environment variables!")


main.add_command(snippets)
main.add_command(snippet)
main.add_command(dictionaries)
main.add_command(dictionary)
main.add_command(dictionaryitems)
main.add_command(dictionaryitem)

