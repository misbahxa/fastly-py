import os
import click

from cli import dictionaryitem as dictitem
from cli import dictionary as dic
from cli import snippet as snip
from cli import version as vers


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

@click.group()
def version():
    pass

# Entry Point
entrypoint.add_command(dictionary)
entrypoint.add_command(dictionaryitem)
entrypoint.add_command(snippet)
entrypoint.add_command(version)

# Dictionary sub commands
dictionary.add_command(dic.show)
dictionary.add_command(dic.listall)

# Dictionary Item sub commands
dictionaryitem.add_command(dictitem.show)
dictionaryitem.add_command(dictitem.listall)
dictionaryitem.add_command(dictitem.add)
dictionaryitem.add_command(dictitem.delete)

# Snippet sub commands
snippet.add_command(snip.show)
snippet.add_command(snip.listall)
snippet.add_command(snip.add)
snippet.add_command(snip.delete)

# Version sub commands
version.add_command(vers.show)
version.add_command(vers.listall)
version.add_command(vers.activeversion)
version.add_command(vers.clone)