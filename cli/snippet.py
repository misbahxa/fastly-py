import os
import click
import fastly

api = fastly.API(key=os.environ['FASTLY_API_KEY'])

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
def listall(service, version):
    snippet_line = "{id},{name},{priority},{type},{updated_at},{dynamic}"
    print(snippet_line.replace('{','').replace('}',''))
    for snippet in api.snippets(service, version):
        print( snippet_line.format(
            **snippet.attrs
            )
        )

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
@click.option('--name', required=True)
def show(service, version ,name):
    try:
        snippet_line = "id: {id}\nname: {name}\npriority: {priority}\ntype: {type}\nupdated_at: {updated_at}\ndynamic: {dynamic}\ncontent:\n{content}"
        print( snippet_line.format( 
            **api.snippet(service, version, name).attrs
            )
        )
    except fastly.errors.NotFoundError:
        print("Snippet name %s does not exists." % name)

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
@click.option('--name', required=True)
def delete(service, version ,name):
    try:
        snipitem = api.snippet(service, version, name)
        snippet_line = "id: {id}\nname: {name}\npriority: {priority}\ntype: {type}\nupdated_at: {updated_at}\ndynamic: {dynamic}\ncontent:\n{content}"
        print( snippet_line.format(**snipitem.attrs) )
        if raw_input('Proceed deleting the above item? (Y/n)') == 'Y':
            print(snipitem.delete()['status'])
    except fastly.errors.NotFoundError:
        print("Snippet name %s does not exists." % name)


@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
@click.option('--name', required=True)
@click.option('--vcl_type', required=True)
@click.option('--dynamic', default=1)
@click.option('--file', required=True)
def add(service, version, name, vcl_type, dynamic, file):
    snippet_line = "id: {id}\nname: {name}\npriority: {priority}\ntype: {type}\nupdated_at: {updated_at}\ndynamic: {dynamic}\ncontent:\n{content}"
    content = open(file, 'r').read()
    body = { 'name': name, 'dynamic': dynamic, 'type': vcl_type, 'content': content }
    print(body)
    try:
        print( snippet_line.format( 
            **api.snippetpost(service, version, body)
            )
        )
    except fastly.errors.UnprocessableEntityError:
        try:
            if api.snippet(service, version, name).attrs:
                print("Snippet %s already exists." % name)
            else:
                print("Unknown error.")
        except:
            print("422 Unprocessable Entity. Something went wrong, please check if the version is not in used or locked.")

       


    
