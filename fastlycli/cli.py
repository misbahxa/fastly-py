import os
import click

from fastlycli import dictionaryitem as dictitem
from fastlycli import dictionary as dic
from fastlycli import snippet as snip


@click.group()
def entrypoint():
    if "FASTLY_API_KEY" not in os.environ:
        raise Exception("FASTLY_API_KEY is not exist in environment variables!")

@click.group()
def dictionary():
    pass

@click.group()
def dictionaryitem():
    pass

@click.group()
def snippet():
    pass

entrypoint.add_command(dictionary)
entrypoint.add_command(dictionaryitem)
entrypoint.add_command(snippet)

dictionary.add_command(dic.show)
dictionary.add_command(dic.listall)

dictionaryitem.add_command(dictitem.show)
dictionaryitem.add_command(dictitem.listall)
dictionaryitem.add_command(dictitem.add)
dictionaryitem.add_command(dictitem.delete)

snippet.add_command(snip.show)
snippet.add_command(snip.listall)